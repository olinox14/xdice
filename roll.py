"""
Usage:
    roll [options] <expr>

Options:
    -n               Numeric score only
    -v               Verbose result

    -h --help        Displays help message
    --version        Displays current xdice version
"""
import sys

import xdice

def _print_and_exit(string, exit_code=0):
    """ print and exit """
    print(string)
    sys.exit(exit_code)

# Parse arguments
args = sys.argv[1:]

if "-h" in args:
    _print_and_exit(__doc__)

if "--version" in args:
    _print_and_exit("xdice {}".format(xdice.__VERSION__))

score_only = False
if "-n" in args:
    score_only = True
    args.remove("-n")

verbose = False
if "-v" in args:
    verbose = True
    args.remove("-v")

if len(args) != 1:
    _print_and_exit("xdice CLI: invalid arguments\n" + __doc__, 1)

pattern_string = args[0]

# Run xdice
ps = xdice.roll(pattern_string)

if score_only:
    print(ps)
else:
    print("{}\t({})".format(ps, ps.format(verbose)))
