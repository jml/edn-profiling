"""Generate some edn records for profiling."""

import decimal
import random
import sys

import edn


DICTIONARY_FILE = '/usr/share/dict/words'

def load_words(dictionary):
    with open(dictionary, 'r') as dictionary_file:
        return [x.strip() for x in dictionary_file.readlines()]


WORDS = load_words(DICTIONARY_FILE)


def random_words(n):
    for i in range(n):
        word = random.choice(WORDS)
        try:
            yield word.decode('ascii')
        except UnicodeDecodeError:
            continue


def random_decimal():
    value = random.randint(-500000, 500000) / 100.0
    return decimal.Decimal(value).quantize(decimal.Decimal('0.01'))


def make_element():
    return {edn.Keyword('foo'): ' '.join(random_words(3)),
            edn.Keyword('bar'): random_decimal()}



num = int(sys.argv[1])
for i in range(num):
    print edn.dumps(make_element())
