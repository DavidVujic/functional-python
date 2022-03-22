words = ["hello", "pythonic", "world"]


def find_word(word: str, words: list):
    for w in words:
        if w == word:
            return w

    return None


def find_word_functional(word: str, words: list):
    res = filter(lambda w: w == word, words)

    return next(res, None)
