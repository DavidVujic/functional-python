words = [
    {"id": 1, "name": "hello"},
    {"id": 2, "name": "pythonic"},
    {"id": 3, "name": "world"},
]


def find_word(word: str, words: list):
    for w in words:
        if w["name"] == word:
            return w

    return None


def find_word_functional(word: str, words: list):
    res = filter(lambda w: w["name"] == word, words)

    return next(res, None)
