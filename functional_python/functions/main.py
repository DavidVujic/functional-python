words = ["hello", "pythonic", "world"]


def find_word(word: str, words: list) -> str | None:
    for w in words:
        if w == word:
            return w

    return None
