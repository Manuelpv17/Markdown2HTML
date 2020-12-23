#!/usr/bin/python3
""" It’s time to code a Markdown to HTML! """

import sys

if (len(sys.argv) < 3):
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)
markdownFile = sys.argv[1]
outputFile = sys.argv[2]

try:
    f = open("{}".format(markdownFile))
except IOError:
    print("Missing {}".format(markdownFile), file=sys.stderr)
    sys.exit(1)

sys.exit(0)
