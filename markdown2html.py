#!/usr/bin/python3
""" It’s time to code a Markdown to HTML! """

import sys


def markdownToHtml():
    if (len(sys.argv) < 3):
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    markdownFile = sys.argv[1]
    outputFile = sys.argv[2]

    try:
        with open("{}".format(markdownFile), "r") as f:
            pass
    except IOError:
        print("Missing {}".format(markdownFile), file=sys.stderr)
        sys.exit(1)

    headingsHtml = ["<h1>", "<h2>", "<h3>", "<h4>", "<h5>", "<h6>"]
    headingsMarkdown = ["# ", "## ", "### ", "#### ", "##### ", "###### "]

    text = ""
    with open("{}".format(markdownFile), "r") as markdown:
        with open("{}".format(outputFile), "w+") as html:
            for line in markdown.read().split("\n"):
                flag = 0
                for i in range(len(headingsMarkdown) - 1, -1, -1):
                    if headingsMarkdown[i] in line:
                        text += line.replace(
                            headingsMarkdown[i], headingsHtml[i])
                        text += headingsHtml[i] + '\n'
                        flag = 1
                        break
                if flag == 0:
                    text += line + '\n'

            html.write(text[:-1])

    sys.exit(0)


if __name__ == "__main__":
    markdownToHtml()
