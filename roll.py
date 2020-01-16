#! python3
"""
Usage:
    roll [options] <expr>

Options:
    -n --num_only    Numeric score only (Verbose result default)
    -h --help        Displays help message
    --version        Displays current xdice version
"""
import argparse
import xdice


def main():
    """Main command line entry point."""
    parser = argparse.ArgumentParser(
        prog="roll", description="Command Line Interface to the xdice library."
    )
    parser.add_argument(
        "expression",
        nargs="+",
        help="Mathematical expression containing dice format <n>d<s> objects.",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Prints the xdice library version string and exits.",
    )
    parser.add_argument(
        "-n",
        "--num_only",
        action="store_true",
        help="Prints numeric result only.  Otherwise full verbose result is returned.",
    )
    args = parser.parse_args()

    if args.version:
        print("Version {}".format(xdice.__VERSION__))
    else:
        if args.expression:
            expr = "".join(args.expression)
            ps = xdice.roll(expr)
            if args.num_only:
                print(ps)
            else:
                print("{}\t({})".format(ps, ps.format(True)))


if __name__ == "__main__":
    main()
