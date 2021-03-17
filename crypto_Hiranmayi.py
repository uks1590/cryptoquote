import random
import os

def random_line(fname):
    lines = open(fname).read().splitlines()
    myquote = random.choice(lines)
    return myquote

if os.path.exists("randomQuote.html"):
  os.remove("randomQuote.html")

html_txt = """<html>
<head>
<title>Page Title</title>
</head>
<body>"""
html_txt += "<p>" + random_line('Quotes_excel_hiranmayi.txt')
html_txt += "</p> </body></html>"

file1 = open('randomQuote.html','w')
file1.write(html_txt)
file1.close()

