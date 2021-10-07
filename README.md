# Functional Python
Experimenting with writing functional Python using the toolz library.

## What I wish to learn
 Exploring functional concepts in Python using the [toolz](https://toolz.readthedocs.io/en/latest/index.html) library.
 I am using examples from the excellent talk [Clojure in a nutshell](https://www.youtube.com/watch?v=C-kF25fWTO8) by James Trunk.
 I’m exploring, by translating the Clojure code used in his talk into Python.

## What I’ve actually learned
I’ve learned that it isn’t that difficult to apply functional concepts when writing Python code.
What I’m thinking of is the ability to compose functions in a very minimalistic way.
With this, it is probably also easier to keep functions stateless and simplistic.

Also, I really like the possibility to write composed functions into oneliners,
by using the very much Clojure inspired thread_first and thread_last functions of the _toolz_ library.

__Is this approach Pythonic?__ It depends, I guess. Overusing the features of the toolz library
will probably break quite a few of the Python Zen* rules.

_(run “import this” in a Python shell if you haven’t read the zen parts of Python yet)._
