"""Iteratively parses a file.

Benchmark for edn.load.

  streaming.py PATH_TO_LINE_SEPARATED_EDN

Parses just the first line, then the first two lines, then the first three,
and so on until it's parsed all of them.

Uses the streaming approach, parsing using edn._parsley.iterGrammar.

Prints out the number of lines parsed and the time taken in seconds in CSV
format.

c.f. nonstreaming.py
"""

from datetime import datetime
from StringIO import StringIO
import sys

from edn import load


def time_edn(f):
    start = datetime.now()
    list(load(f))
    end = datetime.now()
    return (end - start).total_seconds()


contents = open(sys.argv[1], 'r').read().splitlines()

for i in range(1, len(contents)):
    buf = StringIO(''.join(contents[:i]))
    t = time_edn(buf)
    print '%s,%s' % (i, t)
