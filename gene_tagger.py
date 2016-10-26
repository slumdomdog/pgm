# !/usr/bin/python

import sys

__author__ = "Justin"


class GeneTagger(object):
    """
    The class takes in a test file and tags each word in the file with a label.
    """

    def __init__(self):


    def tag(self, test_file):
        """
        The work horse method of the class which tags each word with a label.
        :param test_file:
        :return:
        """
        # the tagger will always produce the argmax of posterior dist, which implies there should be a dict of dict \
        # so that the argmax of posterior dist can be easily found.

    def writeOutput(self, output):
        """
        write results to output object.
        :param output:
        :return:
        """

def usage():
    sys.stderr.write("""
    use command line: python gene_tagger.py > gene_tagger_output \n
    """)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        sys.exit(2)
    try:
        input = file(sys.argv[1], "r")
    except IOError:
        sys.stderr.write("the file cannot be read \n")
        sys.exit(1)

    tagger = GeneTagger()
    tagger.tag(input)
    # need to redirect the results to another file.
    tagger.writeOutput(sys.stdout)