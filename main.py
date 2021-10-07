from urllib.request import urlopen
import re
import toolz
import common
import helpers


def is_common_word(word):
    return word in common.words


def remove_common(strings):
    return toolz.remove(is_common_word, strings)


def sort_by_value(d: dict):
    return sorted(d.items(), key=lambda item: item[1])


# threading -> combining parts just like LEGO


def most_frequent_words(words: list):
    return toolz.thread_last(
        words,
        #  helpers.to_lower,
        lambda words: map(lambda s: s.lower(), words),
        remove_common,
        toolz.frequencies,
        # sort_by_value,
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
