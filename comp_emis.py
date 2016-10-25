#! /usr/bin/python

__author__ = "Justin Yang"

import sys
from collections import defaultdict
import math


class EmisCal(object):
    """
    calculate the emission probability based on count file.
    """

    def __init__(self):


def usage():
    print """
    python comp_emis.py [count file] > [emis prob]
    read in a count file, and calculate the emission probability.
    """

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        sys.exit(2)

    try:
        input = file(sys.argv[1], "r")
    except IOError:
        sys.stderr.write("Error: cannot read count file %s.\n" %arg)
        sys.exit(1)

    # initialize a emission probability calculator

    # Calculate emission probability


    # Write the probability





