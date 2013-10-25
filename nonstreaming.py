"""Iteratively parses a file.

Benchmark for edn.loads.

  nonstreaming.py PATH_TO_LINE_SEPARATED_EDN

Parses just the first line, then the first two lines, then the first three,
and so on until it's parsed all of them.

Uses the non-streaming approach, wrapping all the lines in a list so they can
be parsed as a single edn element.

Prints out the number of lines parsed and the time taken in seconds in CSV
format.

c.f. streaming.py
"""

from datetime import datetime
import sys

from edn import loads


def time_edn(f):
    start = datetime.now()
    loads(f)
    end = datetime.now()
    return (end - start).total_seconds()

contents = open(sys.argv[1], 'r').read().splitlines()

for i in range(1, len(contents)):
    buf = '[' + ''.join(contents[:i]) + ']'
    t = time_edn(buf)
    print '%s,%s' % (i, t)
    sys.stderr.write('%s,%s\n' % (i, t))
    if i > 100:
        break

