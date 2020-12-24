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

    text = ""
    flag_ul = 0
    flag_ol = 0
    flag_p = 0
    with open("{}".format(markdownFile), "r") as markdown:
        with open("{}".format(outputFile), "w+") as html:
            for line in markdown.read().split("\n"):
                aux_text = text
                text = titles(text, line)
                text, flag_ul = ul(text, line, flag_ul)
                text, flag_ol = ol(text, line, flag_ol)
                if aux_text == text:
                    text, flag_p = p(text, line, flag_p)

            html.write(text)

    sys.exit(0)


def p(text, line, flag):
    pHtml = ["<p>"]
    pHtmlEnd = ["</p>"]
    breakHtml = ["<br/>"]

    if flag == 2:
        text += pHtmlEnd[0] + '\n'
        flag = 0
        return text, flag

    if line:
        if flag == 0:
            text += pHtml[0] + '\n'
        if flag == 1:
            text += breakHtml[0] + '\n'
        text += line + '\n'
        flag = 1
    elif not line and flag == 1:
        text += pHtmlEnd[0] + '\n'
        flag = 0
    return text, flag


def titles(text, line):
    headingsHtml = ["<h1>", "<h2>", "<h3>", "<h4>", "<h5>", "<h6>"]
    headingsHtmlEnd = ["</h1>", "</h2>", "</h3>", "</h4>", "</h5>", "</h6>"]
    headingsMarkdown = ["# ", "## ", "### ", "#### ", "##### ", "###### "]
    for i in range(len(headingsMarkdown) - 1, -1, -1):
        if headingsMarkdown[i] in line:
            text += line.replace(
                headingsMarkdown[i], headingsHtml[i])
            text += headingsHtmlEnd[i] + '\n'
            break
    return text


def ul(text, line, flag):
    listMarkdown = ["- "]
    listHtml = ["<ul>", "<li>"]
    listHtmlEnd = ["</ul>", "</li>"]

    if listMarkdown[0] in line:
        if flag == 0:
            text += listHtml[0] + '\n'
        flag = 1
        text += line.replace(listMarkdown[0], listHtml[1])
        text += listHtmlEnd[1] + '\n'
    elif listMarkdown[0] not in line and flag == 1:
        text += listHtmlEnd[0] + '\n'
        flag = 0
    return text, flag


def ol(text, line, flag):
    listMarkdown = ["* "]
    listHtml = ["<ol>", "<li>"]
    listHtmlEnd = ["</ol>", "</li>"]

    if listMarkdown[0] in line:
        if flag == 0:
            text += listHtml[0] + '\n'
        flag = 1
        text += line.replace(listMarkdown[0], listHtml[1])
        text += listHtmlEnd[1] + '\n'
    elif listMarkdown[0] not in line and flag == 1:
        text += listHtmlEnd[0] + '\n'
        flag = 0
    return text, flag


if __name__ == "__main__":
    markdownToHtml()
