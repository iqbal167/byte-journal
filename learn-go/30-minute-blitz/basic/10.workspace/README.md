# Go Workspace

Go Workspace is a project that contains multiple Go modules.

Init the workspace:
Used to initialize the workspace with the specified modules.
```bash
go work init ./app ./utils
```

Add the modules to the workspace:
Used to add the modules to the workspace.
```bash
go work use ./app ./utils
```

Add all modules in the workspace:
Used to add all modules in the workspace.
```bash
go work use -r .
```

Sync the workspace:
Used to sync the workspace with the modules.
```bash
go work sync
```
## Notes

- The `go.work` file is used to manage the workspace.
- The `go.work` file is not committed to the repository. add it to the `.gitignore` file.

## Use Case

- Used to manage multiple Go modules in a single project.
- Used to manage the dependencies of the modules in the workspace.
- Used to manage the version of the modules in the workspace.
- Used to avoid the version conflict of the modules in the workspace.
- Do not use the workspace to manage the dependencies of the modules in the project.
- Do not use the workspace to manage the version of the modules in the project.
- Do not use the workspace if the project is stable.
