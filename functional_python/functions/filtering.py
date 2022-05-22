"""
Even if the Python Zen rules includes the phrase:
"There should be one-- and preferably only one --obvious way to do it.",
there seems to be at least three ways of solving things quite often.

An example is filtering a list:

"""

words = [
    {"id": 1, "name": "hello"},
    {"id": 2, "name": "pythonic"},
    {"id": 3, "name": "world"},
]


# good?
def find_word_with_a_for_loop(word: str, words: list) -> dict | None:
    for w in words:
        if w["name"] == word:
            return w

    return None


# yes good, but ...
def find_word_with_filter(word: str, words: list) -> dict | None:
    res = filter(lambda w: w["name"] == word, words)

    return next(res, None)


# Probably Pythonic!
def find_word_with_comprehension(word: str, words: list) -> dict | None:
    res = (w for w in words if w["name"] == word)

    return next(res, None)
