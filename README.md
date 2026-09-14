# Operw

Operw is a simple project workflow and build tool.

It provides a small set of commands for creating, building, testing, publishing, and installing projects through an `operw.toml` configuration file.

## Commands

```text
operw help
operw version
operw init [project_name] [location]

operw run build
operw run test
operw run publish
operw run install
```

### `help`

Show available commands.

```bash
operw help
```

### `version`

Show the current Operw version.

```bash
operw version
```

### `init`

Create an empty project.

```bash
operw init [project_name] [location]
```

Both arguments are optional.

Example:

```bash
operw init MyProject .
```

### `run`

Run a workflow defined in `operw.toml`.

```bash
operw run [workflow]
```

Available workflows:

```text
build
test
publish
install
```

Examples:

```bash
operw run build
operw run test
operw run publish
operw run install
```

## Configuration

Operw uses `operw.toml` as its project configuration file.

```toml
[build]
compiler = "gcc"
source = ["src/main.c"]
target = "build/a.out"
flags = []

[test]
start = ["./build/a.out"]

[publish]
author = "codingmc"
source = ["src/main.c"]
ignore_file = "build"
repository = "https://github.com/user/project"
branch = "main"

[install]
git_method = []
wget_method = []
```

### Build

The `[build]` section contains the configuration for compiling the project.

| Key        | Type   | Description          |
| ---------- | ------ | -------------------- |
| `compiler` | string | C compiler to use    |
| `source`   | array  | Source files         |
| `target`   | string | Output executable    |
| `flags`    | array  | Compiler flag groups |

### Test

The `[test]` section defines how the built program is executed.

| Key     | Type  | Description                                     |
| ------- | ----- | ----------------------------------------------- |
| `start` | array | Command and arguments used to start the program |

### Publish

The `[publish]` section contains project publishing information.

| Key           | Type   | Description                 |
| ------------- | ------ | --------------------------- |
| `author`      | string | Project author              |
| `source`      | array  | Files to publish            |
| `ignore_file` | string | File or directory to ignore |
| `repository`  | string | Git repository              |
| `branch`      | string | Git branch                  |

### Install

The `[install]` section defines project download/install sources.

| Key           | Type  | Description                 |
| ------------- | ----- | --------------------------- |
| `git_method`  | array | Git repositories to clone   |
| `wget_method` | array | Files to download with wget |

## Project Structure

A project initialized with Operw may look like:

```text
MyProject/
├── src/
│   └── main.c
├── include/
│   └── main.h
├── build/
├── operw.toml
├── README.md
└── CHANGELOG.txt
```

## Status

Operw is currently under development.
