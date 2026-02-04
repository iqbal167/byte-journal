# Go Command

## Basic Commands

go help
Go help is used to view help for Go commands.

go run
Go run is used to run a Go program.

go build
Go build is used to build a Go program.
Example:
go build -o app. `-o` flag is used to specify the output file name.
These are basic build environment variables:
- `GOOS`: The target operating system.
- `GOARCH`: The target architecture.
- `GOFLAGS`: Additional flags to pass to the compiler.
- `GCO_ENABLED`: Whether to enable the Go compiler optimizations.

```
go build -o app -ldflags "-w -s"
```

That command will build the Go program and remove the debugging symbols.

```
GOOS=linux GOARCH=amd64 go build -o app
```

That command will build the Go program for Linux on AMD64 architecture.

go vet
Go vet is used to check for common errors in Go code.

go doc
Go doc is used to view documentation for Go packages, functions, types, and variables.
Example:
go doc -src fmt Printf. `-src` flag is used to view the source code for the function.

go fmt
Go fmt is used to format Go code.

go fix
Go fix is used to apply Go language migrations to code.

go clean
Go clean is used to remove object files and cached files.

go tool
Go tool is used to run Go tools.
Example:
go tool dist list. Use this command to list all the supported operating systems and architectures.