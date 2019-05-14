"""
Dummy program for testing runner
"""

import sys

def main(args):
    input = args[1]
    print("dummy input: " + str(input))
    if int(input) == 1:
        sys.exit(0)
    else:
        sys.exit(7)

main(sys.argv)