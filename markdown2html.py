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
    headingsHtmlEnd = ["</h1>", "</h2>", "</h3>", "</h4>", "</h5>", "</h6>"]
    headingsMarkdown = ["# ", "## ", "### ", "#### ", "##### ", "###### "]
    listMarkdown = ["- "]
    listHtml = ["<ul>", "<li>"]
    listHtmlEnd = ["</ul>", "</li>"]

    text = ""
    ul_flag = 0
    with open("{}".format(markdownFile), "r") as markdown:
        with open("{}".format(outputFile), "w+") as html:
            for line in markdown.read().split("\n"):
                for i in range(len(headingsMarkdown) - 1, -1, -1):
                    if headingsMarkdown[i] in line:
                        text += line.replace(
                            headingsMarkdown[i], headingsHtml[i])
                        text += headingsHtmlEnd[i] + '\n'
                        break
                if listMarkdown[0] in line:
                    if ul_flag == 0:
                        text += listHtml[0] + '\n'
                    ul_flag = 1
                    text += line.replace(listMarkdown[0], listHtml[1])
                    text += listHtmlEnd[1] + '\n'
                elif listMarkdown[0] not in line and ul_flag == 1:
                    text += listHtmlEnd[0] + '\n'
                    ul_flag = 0

            html.write(text)

    sys.exit(0)


if __name__ == "__main__":
    markdownToHtml()
