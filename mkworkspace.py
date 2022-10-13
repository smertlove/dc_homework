import sys
import os

class ArgcError(Exception):
    def __init__(self, uname, argc):
        self.uname = uname
        self.argc = argc

    def __str__(self) -> str:
        return f"ArgcError: \"{self.uname}\" expects 1 argument, {self.argc} were given."


def mkdirs(*paths):
    for path in paths:
        if os.path.exists(path):
            raise OSError(f"folder \"{path}\" already exists. Change directory or move/delete \"{path}\" folder.")
    for path in paths:
        os.makedirs(path)

def mkfiles(*paths):
    template = """def main():
    pass

if __name__ == \"__main__\":
    main()
"""
    for path in paths:
        f = open(f"{path}/{path}.py", "w", encoding="utf-8")
        f.write(template)
        f.close()

        open(f"{path}/readme.md", "w", encoding="utf-8").close()

def main():
    name = sys.argv[0]

    argc = len(sys.argv[1:])
    if argc != 1:
        raise ArgcError(name, argc)

    n = sys.argv[1]
    try:
        n = int(n)
    except ValueError:
        raise ValueError(f"The argument for \"{name}\" should be a positive integer.")
    
    if n < 1:
        raise ValueError(f"The argument for \"{name}\" should be a positive integer.")

    if n > 20:
        answ = input("Do you really want to make that many workspace dummies? [Y/N]: ")
        if not answ.lower().startswith("y"):
            quit("Terminating program.")
    
    paths = [f"ex{i}" for i in range(1, int(n) + 1)]
    mkdirs(*paths)
    mkfiles(*paths)
    



if __name__ == "__main__":
    main()