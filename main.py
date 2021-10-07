from urllib.request import urlopen
import re
import toolz


common_words = {
    "a",
    "able",
    "about",
    "across",
    "after",
    "all",
    "almost",
    "also",
    "am",
    "among",
    "an",
    "and",
    "any",
    "are",
    "as",
    "at",
    "be",
    "because",
    "been",
    "but",
    "by",
    "can",
    "cannot",
    "could",
    "dear",
    "did",
    "do",
    "does" "either",
    "else",
    "ever",
    "every",
    "for",
    "from",
    "get",
    "got",
    "had",
    "has",
    "have",
    "he",
    "her",
    "hers",
    "him",
    "his",
    "how",
    "however",
    "i",
    "if",
    "in",
    "into",
    "is",
    "it",
    "its",
    "just",
    "least",
    "let",
    "like",
    "likely",
    "may",
    "me",
    "might",
    "most",
    "must",
    "my",
    "neither",
    "no",
    "nor",
    "now",
    "of",
    "off",
    "often",
    "on",
    "one",
    "only",
    "or",
    "other",
    "our",
    "own",
    "rather",
    "said",
    "say",
    "says",
    "she",
    "should",
    "since",
    "so",
    "some",
    "than",
    "that",
    "the",
    "their",
    "them",
    "then",
    "there",
    "these",
    "they",
    "this",
    "those",
    "tis",
    "to",
    "too",
    "twas",
    "up",
    "upon",
    "us",
    "wants",
    "was",
    "we",
    "were",
    "what",
    "when",
    "where",
    "which",
    "while",
    "who",
    "whom",
    "why",
    "will",
    "with",
    "would",
    "yet",
    "you",
    "your",
    "very",
}


def slurp(path):
    return urlopen(path).read().decode("utf-8")


def to_lower(strings):
    return map(lambda s: s.lower(), strings)


def is_common_word(word):
    return word in common_words


def remove_common(strings):
    return toolz.remove(is_common_word, strings)


def sort_by_value(d: dict):
    return sorted(d.items(), key=lambda item: item[1])


# threading -> combining parts just like LEGO


def most_frequent_words(words: list):
    return toolz.thread_last(
        words,
        # to_lower,
        lambda strings: map(lambda s: s.lower(), strings),
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
    book = slurp(path)

    # Extract words: caracters or quotes
    words = re.compile("[\\w|']+").findall(book)
    toolz.count(words)

    # Figure out the title of the book
    toolz.take(20, words)

    most_frequent_words(words)
    longest_words(words)
    longest_palindrome(words)
