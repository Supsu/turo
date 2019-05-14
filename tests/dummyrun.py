"""
Dummy program for testing runner
"""

import sys

def main(args):
    input = args[0]
    if input == 1:
        return 0
    else:
        return 1

main(sys.argv)