# Introduction to LinkML

## 1\. What is LinkML?

**LinkML (Linked Data Modeling Language) is an open-source language for defining the structure, relationships, and meaning of data.**

A LinkML model is written in YAML. It describes the types of things that exist in a domain, their properties, and how they relate to one another.

Unlike a programming language, LinkML does not implement application behaviour. Instead, it provides a common description of information that different programming languages, databases, and tools can use.

For example, consider a software system containing applications, services, network connections, and configuration resources.

Each component might be implemented in a different language or described by a different configuration format. LinkML can define a common model of these components without changing their implementations.

The model can then support validation, documentation, code generation, data exchange, and visualization.

This makes LinkML particularly interesting for understanding complex software systems.

## 2\. The basic concepts

LinkML uses a small set of modeling concepts.

| Concept | Purpose | Example |
| --- | --- | --- |
| Schema | Defines the complete data model | Software architecture |
| Class | Defines a type of entity | Component |
| Slot | Defines a reusable property or relationship | depends\_on |
| Attribute | Defines a property within a class | name |
| Range | Specifies an allowed value type | string, integer, Component |
| Enum | Defines permitted values | Python, Java, Go, C |
| Identifier | Uniquely identifies an entity | component-123 |
| Constraint | Restricts acceptable values | required, pattern |
| Prefix | Defines a namespace for identifiers | code, skupper |

A class is similar to a struct or class in a conventional programming language.

However, LinkML classes describe data rather than executable behaviour.

A slot can contain a primitive value, such as a string, or reference another class.

This allows relationships to become explicit parts of a model.

## 3\. A simple example

Suppose we want to describe a software component and its dependencies.

Create a file named `model.yaml`:

``` yaml
id: https://example.org/software
name: software
description: A model of software components

prefixes:
  linkml: https://w3id.org/linkml/
  software: https://example.org/software/

default_prefix: software

imports:
  - linkml:types

classes:
  Component:
    description: A software component

    attributes:
      id:
        identifier: true
        range: string

      name:
        range: string
        required: true

      language:
        range: string

      depends_on:
        range: Component
        multivalued: true
```

This schema defines a `Component` class.

Every component has an identifier and a name. It can also declare its implementation language and dependencies on other components.

The important part is:

``` yaml
depends_on:
  range: Component
  multivalued: true
```

This declares a relationship between components.

It is not merely a string field named `depends_on`. The schema says that the relationship references another `Component`.

LinkML can use this information when generating schemas, validating data, or translating the model into other representations.

## 4\. Schema versus data

There are two distinct things:

**The schema describes what can exist.**

``` text
Component
 ├── id
 ├── name
 ├── language
 └── depends_on → Component
```

**The data describes what actually exists.**

``` text
Controller
  language: Go
  depends_on:
    - Kubernetes API
    - Router

Router
  language: C
```

The same LinkML schema can describe thousands of components.

This distinction is especially useful when analysing an existing software repository.

We do not necessarily want to create a LinkML class for every Go struct, Java interface, or Python function.

Instead, we can define a relatively small set of classes that describe source-code entities.

For example:

``` text
Repository
Package
Module
Class
Interface
Function
Field
Dependency
Relationship
```

Source-code analysers can then populate these classes with information extracted from a repository.

The result is a consistent representation of different programming languages.

## 5\. Using LinkML with existing codebases

LinkML is not a source-code parser.

It cannot directly inspect a Go repository and automatically understand the application's architecture.

However, existing open-source tools can perform much of the extraction work.

| Language | Source analysis tools |
| --- | --- |
| Python | ast, LibCST |
| Java | JavaParser, Eclipse JDT |
| C | Clang, libclang |
| C++ | Clang, Tree-sitter |
| Go | go/ast, go/types, go/packages |
| Multiple languages | Tree-sitter, SCIP ecosystem |

These tools can identify entities such as functions, types, packages, and imports.

Some also support semantic information, including resolved references and type relationships.

A possible architecture is:

``` text
                  Source Code
                       |
         +-------------+-------------+
         |             |             |
        Go            Java          C
         |             |             |
       go/ast       JavaParser     Clang
         |             |             |
         +-------------+-------------+
                       |
                 Extracted Facts
                       |
                  LinkML Schema
                       |
                Validated Model
                       |
            +----------+----------+
            |          |          |
          JSON       SQLite      RDF
            |          |          |
            +----------+----------+
                       |
               Architecture Views
```

The analyser extracts facts.

LinkML defines how those facts are represented and what they mean within the model.

A database can store the extracted data, while a visualization tool can present selected relationships.

LinkML does not replace any of these tools.

It provides a common model between them.

## 6\. From source code to architecture

Consider a Go project containing:

``` go
type Connector struct {
    RoutingKey string
    Port       int
}
```

A Go analyser can identify the `Connector` struct and its fields.

We can represent the extracted information as:

``` text
Entity: Connector
  kind: struct
  language: Go

Entity: RoutingKey
  kind: field
  type: string

Relationship:
  source: Connector
  target: RoutingKey
  kind: contains
```

An equivalent Java class or C struct could produce comparable information.

This gives us a language-independent structural model.

However, source-code structure is only one part of software architecture.

For example, the existence of a `RoutingKey` field does not explain how Skupper routes application traffic.

That requires additional domain knowledge.

We might extend the model with:

``` text
Connector
  uses → RoutingKey

RoutingKey
  identifies → ApplicationService

Listener
  exposes → ApplicationService
```

These relationships describe software architecture rather than programming-language syntax.

They may be derived from source code, configuration files, Kubernetes resources, tests, or runtime observations.

The distinction matters: **a relationship inferred from a field name is not equivalent to one verified through implementation or runtime evidence.**

A useful architecture model should preserve its evidence and source locations.

## 7\. Is LinkML an ontology?

Not necessarily.

A LinkML schema is primarily a data model. It defines entities, properties, relationships, and constraints.

An ontology goes further by giving concepts formally defined meanings and potentially supporting logical inference.

LinkML can participate in ontology development because it supports semantic identifiers and mappings to technologies such as RDF and OWL.

However, writing a LinkML schema does not automatically produce a complete ontology of a software system.

For a project such as Skupper, a practical approach is to begin with a data model and progressively introduce semantic relationships.

For example:

``` text
Component
  implements → Capability

Capability
  requires → Protocol

Protocol
  supported_by → Proxy
```

These relationships could eventually support questions about architecture, compatibility, and implementation.

The model can become more semantically expressive as those questions become clearer.

## 8\. What does LinkML generate?

A LinkML schema can be transformed into several useful artifacts.

| Output | Purpose |
| --- | --- |
| JSON Schema | Validate JSON data |
| Python classes | Work with typed objects |
| Java classes | Integrate with Java applications |
| Go structs | Integrate with Go applications |
| SQL DDL | Describe relational database structures |
| RDF | Represent linked data |
| OWL | Express ontology-oriented semantics |
| Documentation | Publish the model |
| Diagrams | Visualize classes and relationships |

Generator support and feature coverage vary between targets.

C has no comparable official generator in the core toolchain.

The important feature is not any individual generator. It is the ability to maintain one model and produce different representations of it.

For example, a JSON Schema generated from LinkML could be used to validate data produced by a Go source-code analyser.

The Go application would not need to run LinkML or Python.

## 9\. Getting started

LinkML's main toolchain is implemented in Python.

Install it in a virtual environment:

``` bash
python3 -m venv .venv
source .venv/bin/activate

python -m pip install linkml
```

Check a schema:

``` bash
linkml validate model.yaml
```

Generate JSON Schema:

``` bash
gen-json-schema model.yaml > model.schema.json
```

Validate instance data:

``` bash
linkml validate \
  -s model.yaml \
  data.yaml
```

The development workflow is straightforward:

``` text
Define schema
      |
      v
Create instance data
      |
      v
Validate
      |
      v
Generate representations
      |
      v
Integrate with applications
```

The challenge is usually not learning the YAML syntax.

It is deciding which entities and relationships belong in the model.

## 10\. Applying LinkML to Skupper

Skupper provides a useful example because its architecture involves several kinds of information.

The implementation contains Go packages, types, functions, and interfaces.

Its Kubernetes integration defines resources and controllers.

Its networking components implement concepts such as listeners, connectors, routing keys, and application connections.

These are related, but they are not all represented at the same abstraction level.

A LinkML-based model could connect them.

``` text
             Skupper Repository
                     |
             Source-Code Model
                     |
          +----------+----------+
          |                     |
       Go Types             CRD Resources
          |                     |
          +----------+----------+
                     |
                Domain Model
                     |
          +----------+----------+
          |          |          |
         Site     Listener   Connector
                     |          |
                     +-----+----+
                           |
                       RoutingKey
                           |
                     Application
```

The source-code model answers questions about implementation.

The domain model answers questions about Skupper's behaviour and capabilities.

The connection between them allows architectural questions to be traced back to source code.

For example:

*Which source-code components implement the configuration and processing of a Skupper listener?*

Answering that question requires more than a LinkML schema. It requires source-code extraction, domain mappings, and evidence connecting the two.

LinkML provides a way to describe and validate those mappings consistently.

## 11\. Connecting LinkML to Blockscape

LinkML and Blockscape solve different problems.

LinkML describes information. Blockscape presents a selected view of that information.

For example, LinkML might describe a component as:

``` text
Component
  name: Listener Controller
  language: Go
  implements: Listener Management
  depends_on: Kubernetes API
```

A Blockscape model could place that component within a category:

``` text
Category: Control Plane

  Listener Controller
    dependencies:
      - Kubernetes API
```

LinkML classes do not necessarily correspond to Blockscape categories.

A class defines the type of an entity. A Blockscape category groups entities for a particular visualization.

Similarly, Blockscape stages can represent maturity, progression, or another dimension of a view without making those properties intrinsic to every LinkML entity.

This separation allows one LinkML model to support multiple Blockscape maps.

For example, the same architecture data could produce maps organized by implementation, deployment, capability, or dependency.

## 12\. When should you use LinkML?

LinkML is useful when a project needs a shared, explicit description of entities and relationships.

It is especially valuable when information comes from multiple sources or must be consumed by different tools.

For software architecture analysis, LinkML offers three important advantages.

**Consistency.** Different source-code analysers can produce data conforming to the same model.

**Extensibility.** New entity types, relationships, and constraints can be introduced as understanding improves.

**Interoperability.** The model can connect programming-language representations, configuration resources, graph data, documentation, and visualization.

There are also limitations.

LinkML does not discover software architecture automatically, execute source-code analysis, or guarantee that extracted relationships accurately describe runtime behaviour.

Those responsibilities remain with analysers, domain-specific extraction rules, and verification processes.

## Conclusion

LinkML provides a way to describe software systems independently of the languages used to implement them.

For an existing codebase, the most useful starting point is not necessarily code generation. It is defining a common model into which existing tools can extract information.

This creates a foundation for connecting source-code structure with higher-level architectural concepts.

For a system such as Skupper, the long-term opportunity is to connect implementation details, Kubernetes resources, networking behaviour, and application capabilities within one model.

LinkML defines that model. Source-code tools populate it. Databases store it. Visualization tools such as Blockscape make it easier to explore.

The result is not automatically an ontology or a complete representation of the software architecture.

It is a structured, testable foundation from which that understanding can be developed.