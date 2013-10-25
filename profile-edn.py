"""Generate profiling data for edn.load."""

import cProfile
from StringIO import StringIO
import sys

from edn import load


def time_edn():
    list(load(buf))


contents = open(sys.argv[1], 'r').read().splitlines()
buf = StringIO(''.join(contents))

cProfile.run('time_edn()', 'edn-all.prof')
