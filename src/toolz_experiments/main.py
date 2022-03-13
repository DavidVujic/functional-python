import re
import toolz
from toolz_experiments import common
from toolz_experiments import helpers


def is_common_word(word):
    return word in common.words


# threading -> combining parts just like LEGO


def most_frequent_words(words: list):
    return toolz.thread_last(
        words,
        lambda words: map(lambda s: s.lower(), words),
        lambda words: toolz.remove(is_common_word, words),
        # alternate syntax with less verbosity (toolz.remove, is_common_word),
        toolz.frequencies,
        lambda d: sorted(d.items(), key=lambda item: item[1]),
        lambda seq: toolz.tail(20, seq),
    )


def longest_words(words: list):
    return toolz.thread_last(
        words,
        set,
        lambda seq: sorted(seq, key=len),
        lambda seq: toolz.tail(20, seq),
        lambda seq: toolz.groupby(len, seq),
    )


def is_palindrome(coll):
    return list(coll) == list(reversed(coll))


def longest_palindrome(words: list):
    return toolz.thread_last(
        words,
        set,
        lambda words: filter(is_palindrome, words),
        lambda words: sorted(words, key=len),
        toolz.last,
    )


def main():
    path = "http://www.gutenberg.org/files/2701/2701-0.txt"
    book = helpers.slurp(path)

    # Extract words: caracters or quotes
    words = re.compile("[\\w|']+").findall(book)
    toolz.count(words)

    # Figure out the title of the book
    list(toolz.take(20, words))

    most_frequent_words(words)
    longest_words(words)
    longest_palindrome(words)
