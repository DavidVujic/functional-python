"""
Even if the Python Zen rules includes the phrase:
"There should be one-- and preferably only one --obvious way to do it.",
there seems to be at least three ways of solving things quite often.

An example is filtering a list:

"""

words = ["hello", "pythonic", "world"]


# good?
def find_word_with_a_for_loop(word: str, words: list) -> str:
    for w in words:
        if w == word:
            return w

    return f"no {word} for you"


# yes good, but ...
def find_word_with_filter(word: str, words: list) -> str:
    res = filter(lambda w: w == word, words)

    return next(res, f"no {word} for you")


# Probably Pythonic!
def find_word_with_comprehension(word: str, words: list) -> str:
    res = (w for w in words if w == word)

    return next(res, f"no {word} for you")


def comment():
    find_word_with_a_for_loop("pythonic", words)
    find_word_with_filter("pythonic", words)
    find_word_with_comprehension("pythonic", words)
