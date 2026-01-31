# Go Modules and Packages

## Modules

Module is the root of a Go module. It is a directory that contains a `go.mod` file.

Create a new module by running the following command:

```bash
go mod init modules-and-packages

# OR

go mod init github.com/example/modules-and-packages
```

Manage dependencies:
Manage dependencies is the process of adding, removing, or updating dependencies of the module.

```bash
go get github.com/example/dependency
```

List all dependencies:
List all dependencies is the process of listing all dependencies of the module.

```bash
go list -m all
```

Remove or update a dependency:
Remove or update a dependency is the process of removing or updating a dependency of the module.

```bash
go mod tidy
```

Upgrade a dependency:
Upgrade a dependency is the process of upgrading a dependency to a newer version.

```bash
go get github.com/example/dependency@v1.0.0
```

Upgrade all dependencies:
Upgrade all dependencies is the process of upgrading all dependencies of the module to their latest versions.

```bash
go get -u ./...
```

Verify dependencies:
Verify dependencies is the process of verifying that all dependencies of the module are up-to-date.

```bash
go mod verify
```

Go mod why is the process of showing why a dependency is needed.
Useful when you want to understand why a dependency is needed, why a dependency is bloating the module.

```bash
go mod why github.com/example/dependency
```

Replace a dependency:
Replace a dependency is the process of replacing a dependency with a different version.

```bash
go mod replace github.com/example/dependency@v1.0.0 => github.com/example/dependency@v2.0.0
```

Usecase
- When you want to use a different version of a dependency than the one specified in the module.
- Fork a dependency and use your own version.
- Patch a dependency with a fix.

Exclude a dependency:
Exclude a dependency is the process of excluding a dependency from the module.

```bash
go mod exclude github.com/example/dependency
```

Download all dependencies:
Download all dependencies is the process of downloading all dependencies of the module. Save them in the `vendor` directory.

```bash
go mod download
```

Vendor dependencies:
Verdoring is the process of copying all dependencies into the `vendor` directory.

```bash
go mod vendor
```

Usecase:
- When you want to vendor dependencies to ensure reproducibility.
- When you want to use a specific version of a dependency.
- Audit dependencies.
- Offline use.

Graph dependencies:
Graph dependencies is the process of visualizing the dependency graph of the module.

```bash
go mod graph
```

Private dependencies:
Private dependencies is the process of using private dependencies in the module.

- Set the `GOPRIVATE` environment variable to the list of private repositories.
- Bypass the proxy for private repositories.
- Authenticate with private repositories.

## Packages

Package is a directory that contains Go source files.

Exported identifiers:
Exported identifiers is the process of identifying identifiers that can be accessed from other packages.
- Identifiers that start with a capital letter are exported.
- Identifiers that start with a lowercase letter are not exported.
- Constants, variables, types, functions, and methods.
 
Usecase:
  - When you want to expose certain identifiers to other packages.
  - When you want to hide certain identifiers from other packages.
  - When you want to use a different name for an identifier in a package.
  - When you want to use the same name for an identifier in a package as in the standard library.

Unexported identifiers:
Unexported identifiers is the process of identifying identifiers that cannot be accessed from other packages.
- Identifiers that start with a lowercase letter are not exported.
- Constants, variables, types, functions, and methods.

Usecase:
  - When you want to use an identifier in a package that is not exported.
  - When you want to use an identifier in a package that is not exported as in the standard library.

External Dependencies:
External dependencies is the process of using external dependencies in the module.

```bash
go mod install github.com/example/dependency
```