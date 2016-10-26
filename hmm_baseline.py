# !/usr/bin/python

import sys

def usage():
    sys.stderr.write(
        """
        python hmm_baseline.py [frequency counts file] [data file] [output file]
        """
    )