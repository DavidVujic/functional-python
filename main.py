from urllib.request import urlopen
import re
import toolz

path = "http://www.gutenberg.org/files/2701/2701-0.txt"

book = urlopen(path).read().decode("utf-8")

words = re.compile("[\\w|']+").findall(book)
res = toolz.count(words)
twenty = toolz.take(20, words)
