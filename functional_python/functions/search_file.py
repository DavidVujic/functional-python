"""
Walk upwards directories to find a file, using the pathlib built in.

The first approach (the search_upwards function) is a nice and elegant function,
but has locked in from where to begin the search. In addition to that, it is mutating
the variable that keeps track of the current directory.

Let's refactor it by using a functional approach:

Result:
have a look in the search_file_functional.py
"""


from pathlib import Path


def search_upwards(filename: str) -> Path | None:
    d = Path.cwd()
    root = Path(d.root)

    while d != root:
        fullpath = d / filename
        if fullpath.exists():
            return fullpath
        d = d.parent

    return None


res = search_upwards(".gitignore_global")

print(res)
