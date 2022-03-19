words = ["hello", "pythonic", "world"]


def find_word(word: str, words: list) -> str | None:
    res = None
    for w in words:
        if w == word:
            res = w

    return res
