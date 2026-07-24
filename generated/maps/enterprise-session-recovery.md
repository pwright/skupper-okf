---
title: "Enterprise Traffic Patterns"
type: BlockscapeMap
status: generated
source_path: maps/enterprise-session-recovery.bs
tags:
  - skupper
  - blockscape
---

# Enterprise Traffic Patterns

Edit: [Blockscape](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/enterprise-session-recovery.bs)

```bs full
{
  "blockscapeVersion": 1,
  "title": "Enterprise Traffic Patterns",
  "settings": {
    "theme": "light",
    "hoverScale": 1.5,
    "selectionDimOpacity": 0.2,
    "selectionDimEnabled": true,
    "tileCompactness": 1,
    "titleWrapMode": "wrap",
    "titleHoverWidthMultiplier": 1.3,
    "titleHoverTextPortion": 0.25,
    "obsidianLinksEnabled": false,
    "obsidianLinkMode": "title",
    "obsidianVault": "",
    "autoIdFromName": false,
    "seriesNavDoubleClickMs": 900,
    "showSecondaryLinks": true,
    "centerItems": false,
    "centerNoStageItems": true,
    "showReusedInMap": false,
    "colorPresets": [
      {
        "name": "Black",
        "value": "#111111"
      },
      {
        "name": "White",
        "value": "#ffffff"
      },
      {
        "name": "Red",
        "value": "#ef4444"
      },
      {
        "name": "Green",
        "value": "#22c55e"
      }
    ],
    "depColor": "#2563eb",
    "revdepColor": "#ef4444",
    "linkThickness": "m",
    "stripParentheticalNames": true
  },
  "maps": [
    {
      "id": "enterprise-session-recovery",
      "title": "Enterprise TCP Sessions and Recovery",
      "abstract": "A value-chain map distinguishing continuity of one TCP connection from recovery above TCP. Green items preserve or reconstruct substantial logical state; amber items reconnect and rebuild selected state; red items replace the connection and require explicit application recovery.",
      "categories": [
        {
          "id": "outcomes",
          "title": "Application Outcomes",
          "items": [
            {
              "id": "seamless-work-continuity",
              "name": "Seamless Continuity",
              "deps": [
                "oracle-tac-stack"
              ],
              "source": "generated/enterprise-session-recovery/seamless-work-continuity.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/seamless-work-continuity"
            },
            {
              "id": "bounded-session-resumption",
              "name": "Bounded Resumption",
              "deps": [
                "zookeeper-curator-stack",
                "mqtt-paho-stack"
              ],
              "source": "generated/enterprise-session-recovery/bounded-session-resumption.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/bounded-session-resumption"
            },
            {
              "id": "durable-processing-progress",
              "name": "Durable Progress",
              "deps": [
                "kafka-java-stack",
                "ibm-mq-jms-stack"
              ],
              "source": "generated/enterprise-session-recovery/durable-processing-progress.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/durable-processing-progress"
            },
            {
              "id": "recoverable-messaging-topology",
              "name": "Recoverable Topology",
              "deps": [
                "rabbitmq-qpid-stack",
                "mqtt-paho-stack"
              ],
              "source": "generated/enterprise-session-recovery/recoverable-messaging-topology.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/recoverable-messaging-topology"
            },
            {
              "id": "explicit-application-recovery",
              "name": "Application Recovery",
              "deps": [
                "ordinary-jdbc-stack"
              ],
              "source": "generated/enterprise-session-recovery/explicit-application-recovery.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/explicit-application-recovery"
            }
          ]
        },
        {
          "id": "software-stacks",
          "title": "Enterprise Software and Java Clients",
          "items": [
            {
              "id": "oracle-tac-stack",
              "name": "Oracle TAC (JDBC Replay + UCP)",
              "deps": [
                "transparent-work-replay"
              ],
              "color": "#2E7D32",
              "source": "generated/enterprise-session-recovery/oracle-tac-stack.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/oracle-tac-stack"
            },
            {
              "id": "ibm-mq-jms-stack",
              "name": "IBM MQ (JMS)",
              "deps": [
                "logical-session-resume",
                "durable-position-recovery"
              ],
              "color": "#388E3C",
              "source": "generated/enterprise-session-recovery/ibm-mq-jms-stack.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/ibm-mq-jms-stack"
            },
            {
              "id": "zookeeper-curator-stack",
              "name": "ZooKeeper (Curator)",
              "deps": [
                "logical-session-resume"
              ],
              "color": "#43A047",
              "source": "generated/enterprise-session-recovery/zookeeper-curator-stack.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/zookeeper-curator-stack"
            },
            {
              "id": "kafka-java-stack",
              "name": "Kafka (Java Client or Spring)",
              "deps": [
                "durable-position-recovery",
                "reconnect-and-retry"
              ],
              "color": "#7CB342",
              "source": "generated/enterprise-session-recovery/kafka-java-stack.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/kafka-java-stack"
            },
            {
              "id": "mqtt-paho-stack",
              "name": "MQTT (Paho Java)",
              "deps": [
                "logical-session-resume",
                "topology-reconstruction"
              ],
              "color": "#8BC34A",
              "source": "generated/enterprise-session-recovery/mqtt-paho-stack.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/mqtt-paho-stack"
            },
            {
              "id": "rabbitmq-qpid-stack",
              "name": "AMQP (RabbitMQ or Qpid JMS)",
              "deps": [
                "topology-reconstruction",
                "reconnect-and-retry"
              ],
              "color": "#F9A825",
              "source": "generated/enterprise-session-recovery/rabbitmq-qpid-stack.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/rabbitmq-qpid-stack"
            },
            {
              "id": "ordinary-jdbc-stack",
              "name": "JDBC (PostgreSQL or MySQL + HikariCP)",
              "deps": [
                "same-tcp-continuity",
                "connection-replacement"
              ],
              "color": "#C62828",
              "source": "generated/enterprise-session-recovery/ordinary-jdbc-stack.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/ordinary-jdbc-stack"
            }
          ]
        },
        {
          "id": "recovery-semantics",
          "title": "Recovery Semantics",
          "items": [
            {
              "id": "transparent-work-replay",
              "name": "Transparent Replay (session and work)",
              "deps": [
                "tracked-session-state",
                "transaction-outcome",
                "automatic-reconnect-failover"
              ],
              "color": "#2E7D32",
              "source": "generated/enterprise-session-recovery/transparent-work-replay.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/transparent-work-replay"
            },
            {
              "id": "logical-session-resume",
              "name": "Session Resumption",
              "deps": [
                "session-identity",
                "session-expiry-window",
                "automatic-reconnect-failover"
              ],
              "color": "#43A047",
              "source": "generated/enterprise-session-recovery/logical-session-resume.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/logical-session-resume"
            },
            {
              "id": "durable-position-recovery",
              "name": "Durable-Position Recovery",
              "deps": [
                "durable-checkpoint",
                "idempotency-and-fencing",
                "automatic-reconnect-failover"
              ],
              "color": "#7CB342",
              "source": "generated/enterprise-session-recovery/durable-position-recovery.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/durable-position-recovery"
            },
            {
              "id": "topology-reconstruction",
              "name": "Topology Reconstruction (and subscriptions)",
              "deps": [
                "durable-delivery-topology",
                "automatic-reconnect-failover"
              ],
              "color": "#F9A825",
              "source": "generated/enterprise-session-recovery/topology-reconstruction.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/topology-reconstruction"
            },
            {
              "id": "reconnect-and-retry",
              "name": "Reconnect (and retry)",
              "deps": [
                "idempotency-and-fencing",
                "retry-policy",
                "automatic-reconnect-failover"
              ],
              "color": "#FB8C00",
              "source": "generated/enterprise-session-recovery/reconnect-and-retry.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/reconnect-and-retry"
            },
            {
              "id": "connection-replacement",
              "name": "Connection Replacement",
              "deps": [
                "connection-pool",
                "failure-detection"
              ],
              "color": "#C62828",
              "source": "generated/enterprise-session-recovery/connection-replacement.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/connection-replacement"
            },
            {
              "id": "same-tcp-continuity",
              "name": "Same TCP Connection",
              "deps": [
                "heartbeat-and-keepalive",
                "tcp-connection"
              ],
              "color": "#1565C0",
              "source": "generated/enterprise-session-recovery/same-tcp-continuity.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/same-tcp-continuity"
            }
          ]
        },
        {
          "id": "protocol-state",
          "title": "State Above TCP",
          "items": [
            {
              "id": "tracked-session-state",
              "name": "Tracked Session State",
              "deps": [
                "session-identity"
              ],
              "source": "generated/enterprise-session-recovery/tracked-session-state.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/tracked-session-state"
            },
            {
              "id": "transaction-outcome",
              "name": "Known Transaction Outcome",
              "deps": [
                "idempotency-and-fencing"
              ],
              "source": "generated/enterprise-session-recovery/transaction-outcome.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/transaction-outcome"
            },
            {
              "id": "session-identity",
              "name": "Session Identity",
              "deps": [
                "broker-database-endpoints"
              ],
              "source": "generated/enterprise-session-recovery/session-identity.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/session-identity"
            },
            {
              "id": "session-expiry-window",
              "name": "Session Resume Window",
              "deps": [
                "failure-detection"
              ],
              "source": "generated/enterprise-session-recovery/session-expiry-window.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/session-expiry-window"
            },
            {
              "id": "durable-checkpoint",
              "name": "Durable Checkpoint (offset or cursor)",
              "deps": [
                "broker-database-endpoints"
              ],
              "source": "generated/enterprise-session-recovery/durable-checkpoint.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/durable-checkpoint"
            },
            {
              "id": "durable-delivery-topology",
              "name": "Durable Delivery State (and topology)",
              "deps": [
                "broker-database-endpoints"
              ],
              "source": "generated/enterprise-session-recovery/durable-delivery-topology.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/durable-delivery-topology"
            },
            {
              "id": "idempotency-and-fencing",
              "name": "Idempotency (deduplication and fencing)",
              "deps": [
                "broker-database-endpoints"
              ],
              "source": "generated/enterprise-session-recovery/idempotency-and-fencing.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/idempotency-and-fencing"
            }
          ]
        },
        {
          "id": "connection-management",
          "title": "Client Connection Management",
          "items": [
            {
              "id": "automatic-reconnect-failover",
              "name": "Automatic Reconnect (and failover)",
              "deps": [
                "failure-detection",
                "endpoint-discovery"
              ],
              "source": "generated/enterprise-session-recovery/automatic-reconnect-failover.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/automatic-reconnect-failover"
            },
            {
              "id": "failure-detection",
              "name": "Failure Detection",
              "deps": [
                "tcp-connection",
                "broker-database-endpoints"
              ],
              "source": "generated/enterprise-session-recovery/failure-detection.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/failure-detection"
            },
            {
              "id": "retry-policy",
              "name": "Bounded Retry (and backoff)",
              "deps": [
                "failure-detection"
              ],
              "source": "generated/enterprise-session-recovery/retry-policy.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/retry-policy"
            },
            {
              "id": "connection-pool",
              "name": "Connection Pool",
              "deps": [
                "failure-detection",
                "tcp-connection"
              ],
              "source": "generated/enterprise-session-recovery/connection-pool.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/connection-pool"
            },
            {
              "id": "heartbeat-and-keepalive",
              "name": "Heartbeats (and TCP keepalive)",
              "deps": [
                "tcp-connection",
                "nat-firewall-state",
                "load-balancer-proxy-timeout"
              ],
              "source": "generated/enterprise-session-recovery/heartbeat-and-keepalive.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/heartbeat-and-keepalive"
            },
            {
              "id": "endpoint-discovery",
              "name": "Endpoint Discovery",
              "deps": [
                "broker-database-endpoints",
                "network-path"
              ],
              "source": "generated/enterprise-session-recovery/endpoint-discovery.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/endpoint-discovery"
            }
          ]
        },
        {
          "id": "transport",
          "title": "TCP and Network Path",
          "items": [
            {
              "id": "tcp-connection",
              "name": "TCP Connection",
              "deps": [
                "network-path"
              ],
              "source": "generated/enterprise-session-recovery/tcp-connection.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/tcp-connection"
            },
            {
              "id": "network-path",
              "name": "Network Path",
              "deps": [],
              "source": "generated/enterprise-session-recovery/network-path.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/network-path"
            },
            {
              "id": "nat-firewall-state",
              "name": "NAT (and firewall state)",
              "deps": [
                "network-path"
              ],
              "source": "generated/enterprise-session-recovery/nat-firewall-state.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/nat-firewall-state"
            },
            {
              "id": "load-balancer-proxy-timeout",
              "name": "Idle Timeout (load balancer or proxy)",
              "deps": [
                "network-path"
              ],
              "source": "generated/enterprise-session-recovery/load-balancer-proxy-timeout.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/load-balancer-proxy-timeout"
            },
            {
              "id": "broker-database-endpoints",
              "name": "Broker (and database endpoints)",
              "deps": [
                "network-path"
              ],
              "source": "generated/enterprise-session-recovery/broker-database-endpoints.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/broker-database-endpoints"
            }
          ]
        }
      ]
    },
    {
      "id": "enterprise-traffic-patterns",
      "title": "Enterprise Traffic Patterns",
      "abstract": "A companion map for common office and enterprise traffic. It distinguishes independent exchanges, pooled connections, multiplexed streams, socket-bound sessions, reconnectable sessions, and durable recovery. Colours indicate the dominant behaviour: blue for request or pooled traffic, purple for multiplexing, red for socket-bound sessions, amber for resumable sessions, and green for durable progress.",
      "categories": [
        {
          "id": "uses",
          "title": "Enterprise Uses",
          "items": [
            {
              "id": "web-api-access",
              "name": "Web (and APIs)",
              "deps": [
                "http1",
                "http2-grpc",
                "http3-quic",
                "websocket"
              ],
              "source": "generated/enterprise-session-recovery/web-api-access.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/web-api-access"
            },
            {
              "id": "remote-access",
              "name": "Remote Access",
              "deps": [
                "ssh-sftp",
                "rdp"
              ],
              "source": "generated/enterprise-session-recovery/remote-access.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/remote-access"
            },
            {
              "id": "database-access",
              "name": "Database Access",
              "deps": [
                "direct-db",
                "redis"
              ],
              "source": "generated/enterprise-session-recovery/database-access.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/database-access"
            },
            {
              "id": "events-messaging",
              "name": "Events (and Messaging)",
              "deps": [
                "kafka",
                "amqp-jms",
                "mqtt"
              ],
              "source": "generated/enterprise-session-recovery/events-messaging.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/events-messaging"
            },
            {
              "id": "file-sharing",
              "name": "File Sharing",
              "deps": [
                "smb",
                "nfs"
              ],
              "source": "generated/enterprise-session-recovery/file-sharing.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/file-sharing"
            },
            {
              "id": "identity-naming",
              "name": "Identity (and Naming)",
              "deps": [
                "ldap",
                "kerberos",
                "dns"
              ],
              "source": "generated/enterprise-session-recovery/identity-naming.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/identity-naming"
            },
            {
              "id": "office-operations",
              "name": "Office Operations",
              "deps": [
                "mail",
                "ipp",
                "sip-rtp",
                "snmp",
                "syslog",
                "dhcp"
              ],
              "source": "generated/enterprise-session-recovery/office-operations.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/office-operations"
            }
          ]
        },
        {
          "id": "web-interactive",
          "title": "Web and Interactive",
          "items": [
            {
              "id": "http1",
              "name": "HTTP/1.1",
              "deps": [
                "pooled-reuse",
                "reconnect-retry",
                "tls",
                "tcp"
              ],
              "color": "#1976D2",
              "source": "generated/enterprise-session-recovery/http1.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/http1"
            },
            {
              "id": "http2-grpc",
              "name": "HTTP/2 (and gRPC)",
              "deps": [
                "multiplexed-session",
                "reconnect-retry",
                "tls",
                "tcp"
              ],
              "color": "#6A1B9A",
              "source": "generated/enterprise-session-recovery/http2-grpc.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/http2-grpc"
            },
            {
              "id": "http3-quic",
              "name": "HTTP/3 (QUIC)",
              "deps": [
                "independent-request",
                "multiplexed-session",
                "tls",
                "quic"
              ],
              "color": "#6A1B9A",
              "source": "generated/enterprise-session-recovery/http3-quic.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/http3-quic"
            },
            {
              "id": "websocket",
              "name": "WebSocket",
              "deps": [
                "socket-bound",
                "keepalive-timeouts",
                "tls",
                "tcp"
              ],
              "color": "#C62828",
              "source": "generated/enterprise-session-recovery/websocket.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/websocket"
            },
            {
              "id": "ssh-sftp",
              "name": "SSH (and SFTP)",
              "deps": [
                "socket-bound",
                "keepalive-timeouts",
                "tcp"
              ],
              "color": "#C62828",
              "source": "generated/enterprise-session-recovery/ssh-sftp.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/ssh-sftp"
            },
            {
              "id": "rdp",
              "name": "RDP",
              "deps": [
                "reconnectable-session",
                "tcp",
                "udp"
              ],
              "color": "#F9A825",
              "source": "generated/enterprise-session-recovery/rdp.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/rdp"
            }
          ]
        },
        {
          "id": "data-messaging",
          "title": "Data and Messaging",
          "items": [
            {
              "id": "direct-db",
              "name": "Direct DB (JDBC/native)",
              "deps": [
                "socket-bound",
                "pooled-reuse",
                "tls",
                "tcp"
              ],
              "color": "#C62828",
              "source": "generated/enterprise-session-recovery/direct-db.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/direct-db"
            },
            {
              "id": "kafka",
              "name": "Kafka",
              "deps": [
                "durable-position",
                "reconnect-retry",
                "tls",
                "tcp"
              ],
              "color": "#2E7D32",
              "source": "generated/enterprise-session-recovery/kafka.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/kafka"
            },
            {
              "id": "amqp-jms",
              "name": "AMQP (and JMS)",
              "deps": [
                "reconnectable-session",
                "durable-position",
                "tls",
                "tcp"
              ],
              "color": "#2E7D32",
              "source": "generated/enterprise-session-recovery/amqp-jms.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/amqp-jms"
            },
            {
              "id": "mqtt",
              "name": "MQTT",
              "deps": [
                "reconnectable-session",
                "keepalive-timeouts",
                "tls",
                "tcp"
              ],
              "color": "#F9A825",
              "source": "generated/enterprise-session-recovery/mqtt.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/mqtt"
            },
            {
              "id": "redis",
              "name": "Redis Protocol",
              "deps": [
                "socket-bound",
                "reconnect-retry",
                "tls",
                "tcp"
              ],
              "color": "#C62828",
              "source": "generated/enterprise-session-recovery/redis.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/redis"
            }
          ]
        },
        {
          "id": "file-identity",
          "title": "File and Identity",
          "items": [
            {
              "id": "smb",
              "name": "SMB (Samba)",
              "deps": [
                "reconnectable-session",
                "tcp",
                "dns"
              ],
              "color": "#F9A825",
              "source": "generated/enterprise-session-recovery/smb.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/smb"
            },
            {
              "id": "nfs",
              "name": "NFS",
              "deps": [
                "reconnectable-session",
                "tcp",
                "dns"
              ],
              "color": "#F9A825",
              "source": "generated/enterprise-session-recovery/nfs.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/nfs"
            },
            {
              "id": "ldap",
              "name": "LDAP",
              "deps": [
                "pooled-reuse",
                "reconnect-retry",
                "tls",
                "tcp",
                "dns"
              ],
              "color": "#1976D2",
              "source": "generated/enterprise-session-recovery/ldap.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/ldap"
            },
            {
              "id": "kerberos",
              "name": "Kerberos",
              "deps": [
                "independent-request",
                "udp",
                "tcp",
                "dns"
              ],
              "color": "#1565C0",
              "source": "generated/enterprise-session-recovery/kerberos.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/kerberos"
            }
          ]
        },
        {
          "id": "office-ops",
          "title": "Office and Operations",
          "items": [
            {
              "id": "dns",
              "name": "DNS",
              "deps": [
                "independent-request",
                "udp",
                "tcp",
                "network-path"
              ],
              "color": "#1565C0",
              "source": "generated/enterprise-session-recovery/dns.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/dns"
            },
            {
              "id": "dhcp",
              "name": "DHCP",
              "deps": [
                "independent-request",
                "udp",
                "network-path"
              ],
              "color": "#1565C0",
              "source": "generated/enterprise-session-recovery/dhcp.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/dhcp"
            },
            {
              "id": "mail",
              "name": "SMTP (and IMAP)",
              "deps": [
                "pooled-reuse",
                "reconnect-retry",
                "tls",
                "tcp"
              ],
              "color": "#1976D2",
              "source": "generated/enterprise-session-recovery/mail.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/mail"
            },
            {
              "id": "ipp",
              "name": "IPP (Printing)",
              "deps": [
                "independent-request",
                "pooled-reuse",
                "tls",
                "tcp"
              ],
              "color": "#1976D2",
              "source": "generated/enterprise-session-recovery/ipp.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/ipp"
            },
            {
              "id": "sip-rtp",
              "name": "SIP (and RTP)",
              "deps": [
                "reconnectable-session",
                "udp",
                "tcp"
              ],
              "color": "#F9A825",
              "source": "generated/enterprise-session-recovery/sip-rtp.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/sip-rtp"
            },
            {
              "id": "snmp",
              "name": "SNMP",
              "deps": [
                "independent-request",
                "udp",
                "tcp"
              ],
              "color": "#1565C0",
              "source": "generated/enterprise-session-recovery/snmp.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/snmp"
            },
            {
              "id": "syslog",
              "name": "Syslog",
              "deps": [
                "independent-request",
                "udp",
                "tcp",
                "tls"
              ],
              "color": "#1565C0",
              "source": "generated/enterprise-session-recovery/syslog.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/syslog"
            }
          ]
        },
        {
          "id": "session-behaviour",
          "title": "Session Behaviour",
          "items": [
            {
              "id": "independent-request",
              "name": "Independent Exchange",
              "deps": [
                "network-path"
              ],
              "color": "#1565C0",
              "source": "generated/enterprise-session-recovery/independent-request.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/independent-request"
            },
            {
              "id": "pooled-reuse",
              "name": "Pooled Reuse",
              "deps": [
                "tcp",
                "keepalive-timeouts"
              ],
              "color": "#1976D2",
              "source": "generated/enterprise-session-recovery/pooled-reuse.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/pooled-reuse"
            },
            {
              "id": "multiplexed-session",
              "name": "Multiplexed Session",
              "deps": [
                "tcp",
                "keepalive-timeouts"
              ],
              "color": "#6A1B9A",
              "source": "generated/enterprise-session-recovery/multiplexed-session.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/multiplexed-session"
            },
            {
              "id": "socket-bound",
              "name": "Socket-Bound Session",
              "deps": [
                "tcp",
                "keepalive-timeouts"
              ],
              "color": "#C62828",
              "source": "generated/enterprise-session-recovery/socket-bound.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/socket-bound"
            },
            {
              "id": "reconnectable-session",
              "name": "Reconnectable Session",
              "deps": [
                "reconnect-retry"
              ],
              "color": "#F9A825",
              "source": "generated/enterprise-session-recovery/reconnectable-session.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/reconnectable-session"
            },
            {
              "id": "durable-position",
              "name": "Durable Position",
              "deps": [
                "reconnect-retry"
              ],
              "color": "#2E7D32",
              "source": "generated/enterprise-session-recovery/durable-position.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/durable-position"
            },
            {
              "id": "reconnect-retry",
              "name": "Reconnect (and Retry)",
              "deps": [
                "network-path",
                "middleboxes"
              ],
              "color": "#EF6C00",
              "source": "generated/enterprise-session-recovery/reconnect-retry.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/reconnect-retry"
            }
          ]
        },
        {
          "id": "transport",
          "title": "Transport and Path",
          "items": [
            {
              "id": "tcp",
              "name": "TCP",
              "deps": [
                "network-path"
              ],
              "source": "generated/enterprise-session-recovery/tcp.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/tcp"
            },
            {
              "id": "udp",
              "name": "UDP",
              "deps": [
                "network-path"
              ],
              "source": "generated/enterprise-session-recovery/udp.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/udp"
            },
            {
              "id": "quic",
              "name": "QUIC",
              "deps": [
                "udp"
              ],
              "source": "generated/enterprise-session-recovery/quic.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/quic"
            },
            {
              "id": "tls",
              "name": "TLS",
              "deps": [
                "network-path"
              ],
              "source": "generated/enterprise-session-recovery/tls.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/tls"
            },
            {
              "id": "keepalive-timeouts",
              "name": "Keepalive (and Timeouts)",
              "deps": [
                "tcp",
                "middleboxes"
              ],
              "source": "generated/enterprise-session-recovery/keepalive-timeouts.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/keepalive-timeouts"
            },
            {
              "id": "middleboxes",
              "name": "Middleboxes (NAT, firewall, LB)",
              "deps": [
                "network-path"
              ],
              "source": "generated/enterprise-session-recovery/middleboxes.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/middleboxes"
            },
            {
              "id": "network-path",
              "name": "Network Path",
              "deps": [],
              "source": "generated/enterprise-session-recovery/network-path.md",
              "external": "https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/network-path"
            }
          ]
        }
      ]
    }
  ]
}
```
