import shutil
import subprocess
import sys
import tomllib
from pathlib import Path


class Helper:
    def __init__(self, key: str, des: str):
        self.key = key
        self.des = des


helper = [
    Helper("help", "show help message"),
    Helper("version", "show newest version"),
    Helper("init", "create an empty project"),
    Helper("run", "run specific command")
]


def help():
    print("Options:")
    for i in helper:
        print(f"    {i.key} - {i.des}")


def version():
    VERSION = "1.0"
    print(f"Operw v{VERSION}")


def detect_compiler():
    for compiler in ["gcc", "clang", "cc"]:
        if shutil.which(compiler):
            return compiler

    return None


def init():
    name = sys.argv[2] if len(sys.argv) > 2 else "Unknown Project"
    loc = Path(sys.argv[3]) if len(sys.argv) > 3 else Path(".")

    if not loc.exists():
        print("Location not exists")
        return 1

    subprocess.run(["bash", "init.sh", name, str(loc)])


def run():
    if len(sys.argv) < 3:
        print("usage: operw run [specific_command]")
        return 1

    config_file = Path("operw.toml")

    if not config_file.exists():
        print("'operw.toml' not found!")
        return 1

    with open(config_file, "rb") as file:
        config = tomllib.load(file)

    name = sys.argv[2]
    workflow = config.get(name)

    if workflow is None:
        print(f"Keyword '{name}' not found")
        return 1

    if name == "build":
        build = config.get("build")

        compiler = str(build.get("compiler", detect_compiler()))
        source = build.get("source", [])
        target = str(build.get("target", ""))
        flags = build.get("flags", [])

        if not compiler:
            print("C compiler not found!")
            return 1
        subprocess.run([compiler, *source, *flags, "-o", target])

    elif name == "test":
        test = config.get("test")
        start = test.get("start", [])
        subprocess.run(start)

    elif name == "publish":
        publish = config.get("publish")

        pc = {
            "author": str(publish.get("author", "Unknown")),
            "source": publish.get("source", []),
            "ignore_file": str(publish.get("ignore_file", ".gitignore")),
            "repository": str(publish.get("repository", "")),
            "branch": str(publish.get("branch", "main"))
        }

        if pc["ignore_file"] != ".gitignore":
            print("'ignore_file' just support .gitignore")
            if not Path(".gitignore").exists():
                pc["ignore_file"] = ""

        subprocess.run(["git", "remote", "add", "origin", pc["repository"]])
        subprocess.run(["git", "add", *pc["source"]])
        subprocess.run(["git", "commit", "-m", "Initialize and Update"])
        subprocess.run(["git", "push", "-u", "origin", pc["branch"]])

    elif name == "install":
        install = config.get("install")
        git_method = install.get("git_method", [])
        wget_method = install.get("wget_method", [])

        if git_method:
            subprocess.run(["git", "clone", *git_method])

        if wget_method:
            subprocess.run(["wget", *wget_method])

    else:
        print(f"Workflow '{name}' not supported")
        return 1


def main():
    if len(sys.argv) < 2:
        print("usage: operw [command] ..")
        print("try use 'help' for more information")
        return 1

    command = sys.argv[1]

    if command == "help":
        help()
    elif command == "version":
        version()
    elif command == "init":
        init()
    elif command == "run":
        run()
    else:
        print(f"Unknown command: {command}")
        return 1


main()