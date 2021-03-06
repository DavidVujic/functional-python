"""
Walk upwards directories to find a file, using the pathlib built in.

The approach in search_file.py is a nice and elegant function,
but has locked in from where to begin the search. In addition to that, it is mutating
the variable that keeps track of the current directory.

Let's refactor it by using a functional approach:

Result:
The find_upwards function is accepting a starting point, and uses recursion
to walk directories upwards. No mutations. Also, less code. Less code, is often less problems.

When reflecting on the code and comparing the two:
the functional one is recalculating the root.
This could (should?) be another input to the function.
"""

from pathlib import Path


def search_upwards(cwd: Path, filename: str) -> Path | None:
    if cwd == Path(cwd.root):
        return None

    fullpath = cwd / filename

    return fullpath if fullpath.exists() else search_upwards(cwd.parent, filename)


search_upwards(Path.cwd(), ".gitignore_global")
