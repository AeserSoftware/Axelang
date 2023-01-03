"""
Python 2 to 3 compatibility helpers.
Falcon Type - 3.5
"""

import sys

PY2 = sys.version_info[0] == 2


if PY2:
    iteritems = lambda d: d.iteritems()
else:
    iteritems = lambda d: iter(d.items())
