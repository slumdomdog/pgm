#! /usr/bin/python

__author__ = "Justin Yang"

import sys
from collections import defaultdict
import math


def simple_corpus_iterator(corpus_file):
    """
    a simple implementation of generator pattern to iterate through the input corpus file
    """
    l = corpus_file.readline()
    while l:
        line = l.strip()
        if line:
            yield line
        else:
            yield None
        l = corpus_file.readline()


class EmisCal(object):
    """
    calculate the emission probability based on count file.
    what properties need to be initialized???
    """

    def __init__(self):
        self.emis_prob = defaultdict(tuple)
        self.count = defaultdict(int)
        self.cond_count = defaultdict(int)

    def compute(self, count_file):
        """
        Compute the emission probabilities of the specified count file
        rare words have been replaced.
        need to compute n(x) and n(x, y) p(y|x) = n(x, y) / n(x). x: words, y: tags, tags are either 0 or wordtag.
        need to compute emission probabilities of n-grams as well.
        Note: try to use iterator to go through the file.
        """
        line_generator = simple_corpus_iterator(count_file)
        for line in line_generator: # the generator has excluded blank lines, there is no need to process again here.
            fields = line.split(" ")
            counts = float(fields[0])
            tag = fields[2]
            word = fields[-1]
            if fields[1] == "WORDTAG":
                self.count[word] += counts
                self.cond_count[tuple(word, tag)] = counts
        for word, count in self.cond_count:
            cur_post = self.emis_prob[word]
            if cur_post:
                self.emis_prob[word] = [cur_post, float(count) / self.count[word]]
            else:
                self.emis_prob[word] = [float(count) / self.cond_count[word]]


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
        input = file(sys.argv[1], "r")  # this is a file object
    except IOError:
        sys.stderr.write("Error: cannot read count file %s.\n" %arg)
        sys.exit(1)

    # initialize a emission probability calculator
    Cal = EmisCal()
    # Calculate emission probability
    Cal.compute(input)
    # Write the probability





