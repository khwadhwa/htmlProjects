#! /usr/bin/python3
print("Content-Type: text/html\n\n")
 
PAGE_TITLE = "Random Integer"
page ='''<!DOCTYPE html>
<html>
    <head>
        <title>_TITLE_</title>
    </head>
    <body>
        _BODY_
    </body>
</html>'''

import random

def randomList(start,end):
    output= '''
        <h3>Random Number Generator</h3>
        <ul>
            _ITEMS_
        </ul>'''
    item='<li>NUM</li>\n'
    items=""
    for i in range(10):
        item = item.replace("NUM",str(random.randint(start,end)))
        items += item
        item= item='\t    <li>NUM</li>\n'    
    items = items[0:(len(items) - 1)]
    output = output.replace("_ITEMS_",items)
    return output

def generateBody():
    body = "<h2>What is this?!?!?</h2>\n"
    body += "\t<p>OMG! Like totally the best!</p>\n"
    body += randomList(-100,100)
    #add more parts onto the body here!
    return body

page = page.replace("_TITLE_", PAGE_TITLE)
page = page.replace("_BODY_",generateBody())

print(page)
