#!/usr/bin/env python3
"""Fetch root skewer.yaml files from Skupper example repositories."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


ORG = "skupperproject"
DEFAULT_BRANCH = "main"
DEFAULT_OUTPUT_DIR = "skewer-yamls"


STATIC_REPOS = [
    "skupper-example-activemq",
    "skupper-example-ansible",
    "skupper-example-bookinfo",
    "skupper-example-camel-integration",
    "skupper-example-console",
    "skupper-example-containers",
    "skupper-example-declarative",
    "skupper-example-dmz",
    "skupper-example-ftp",
    "skupper-example-fuse-online",
    "skupper-example-gateway",
    "skupper-example-grpc",
    "skupper-example-hello-world",
    "skupper-example-http",
    "skupper-example-http-load-balancing",
    "skupper-example-iperf",
    "skupper-example-kafka",
    "skupper-example-kubecon2020",
    "skupper-example-mongodb-replica-set",
    "skupper-example-mysql",
    "skupper-example-patient-portal",
    "skupper-example-podman",
    "skupper-example-policy",
    "skupper-example-postgresql",
    "skupper-example-private-to-private",
    "skupper-example-prometheus",
    "skupper-example-public-to-private",
    "skupper-example-rabbitmq",
    "skupper-example-redis",
    "skupper-example-tcp",
    "skupper-example-tcp-echo",
    "skupper-example-template",
    "skupper-example-trade-zoo",
    "skupper-example-yaml",
]


def github_get_json(url: str, token: str | None) -> tuple[object, dict[str, str]]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "fetch-skewer-yamls",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = Request(url, headers=headers)
    with urlopen(request) as response:
        body = response.read().decode("utf-8")
        headers = {key.lower(): value for key, value in response.headers.items()}
    return json.loads(body), headers


def discover_repos(org: str, token: str | None) -> list[str]:
    repos: list[str] = []
    page = 1

    while True:
        url = f"https://api.github.com/orgs/{quote(org)}/repos?per_page=100&page={page}"
        data, _headers = github_get_json(url, token)
        if not isinstance(data, list):
            raise RuntimeError(f"Unexpected GitHub API response for {url}")
        if not data:
            break

        for repo in data:
            name = repo.get("name", "")
            if "example" in name.lower():
                repos.append(name)
        page += 1

    return sorted(set(repos))


def read_repo_file(path: Path) -> list[str]:
    repos: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        repos.append(line.rsplit("/", 1)[-1])
    return repos


def iter_repos(args: argparse.Namespace) -> Iterable[str]:
    if args.repo:
        return [repo.rsplit("/", 1)[-1] for repo in args.repo]
    if args.repos_file:
        return read_repo_file(args.repos_file)
    if args.static:
        return STATIC_REPOS
    return discover_repos(args.org, args.token)


def fetch_file(url: str, token: str | None) -> bytes:
    headers = {"User-Agent": "fetch-skewer-yamls"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(url, headers=headers)
    with urlopen(request) as response:
        return response.read()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch skewer.yaml from Skupper repos with 'example' in the name."
    )
    parser.add_argument("--branch", default=DEFAULT_BRANCH, help="Branch or tag to fetch")
    parser.add_argument("--org", default=ORG, help="GitHub organization")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(DEFAULT_OUTPUT_DIR),
        help="Directory for renamed YAML files",
    )
    parser.add_argument(
        "--repo",
        action="append",
        help="Repo name or owner/name to fetch; repeatable. Skips discovery when used.",
    )
    parser.add_argument(
        "--repos-file",
        type=Path,
        help="Newline-delimited repo names or owner/name values. Skips discovery when used.",
    )
    parser.add_argument(
        "--static",
        action="store_true",
        help="Use the built-in static repo list instead of discovering repos from GitHub.",
    )
    parser.add_argument(
        "--token",
        help="GitHub token for higher API rate limits. Also accepts GITHUB_TOKEN.",
    )
    args = parser.parse_args()

    if not args.token:
        import os

        args.token = os.environ.get("GITHUB_TOKEN")

    args.output_dir.mkdir(parents=True, exist_ok=True)

    repos = list(iter_repos(args))
    if not repos:
        print("No matching repositories found.", file=sys.stderr)
        return 1

    fetched = 0
    missing: list[str] = []
    failed: list[tuple[str, str]] = []

    for repo in repos:
        branch = quote(args.branch, safe="")
        url = f"https://raw.githubusercontent.com/{quote(args.org)}/{quote(repo)}/{branch}/skewer.yaml"
        target = args.output_dir / f"{repo}.yaml"
        try:
            content = fetch_file(url, args.token)
        except HTTPError as error:
            if error.code == 404:
                missing.append(repo)
            else:
                failed.append((repo, f"HTTP {error.code}"))
            continue
        except URLError as error:
            failed.append((repo, str(error.reason)))
            continue

        target.write_bytes(content)
        fetched += 1
        print(f"fetched {repo} -> {target}")

    print(f"\nFetched {fetched} file(s) from branch '{args.branch}'.")
    if missing:
        print(f"Missing skewer.yaml or branch for {len(missing)} repo(s):")
        for repo in missing:
            print(f"  {repo}")
    if failed:
        print(f"Failed for {len(failed)} repo(s):", file=sys.stderr)
        for repo, reason in failed:
            print(f"  {repo}: {reason}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
