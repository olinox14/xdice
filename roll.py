"""
Usage:
    roll [options] <expr>

Options:
    -s               Numeric score only

    -h --help        Displays help message
    --version        Displays current pydice version
"""
import sys

import dice

def print_ex(string, exit_code=0):
    """ print and exit """
    print(string)
    sys.exit(exit_code)

# Parse arguments
args = sys.argv[1:]

if "-h" in args:
    print_ex(__doc__)

if "-v" in args:
    print_ex("pydice {}".format(dice.__VERSION__))

score_only = False
if "-s" in args:
    score_only = True
    args.remove("-s")

if len(args) != 1:
    print_ex("pydice CLI: invalid arguments\n" + __doc__, 1)

pattern_string = args[0]

# Run pydice
ps = dice.roll(pattern_string)

if score_only:
    print(ps)
else:
    print("{}\t({})".format(ps, ps.format()))
