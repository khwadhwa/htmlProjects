#! /usr/bin/python3
print("Content-Type: text/html\n\n")
PAGE_TITLE = "My Favorite Polynomial"
tab = "    "
page ='''<!DOCTYPE html>
<html>
    <head>
        <title>_TITLE_</title>
    </head>
    <body>
        _BODY_
    </body>
</html>'''

def makePolyTable(start,end):
    table='''
        <table border="1">
            <thead>
                <tr>
                    <th>x</th>
                    <th>y=4x<sup>3</sup> + 12x<sup>2</sup> + 7x</th>
                </tr>
            </thead>
            <tbody>
                _TRS_
            </tbody>
        </table>'''
    rformat="\t\t<tr><td>x</td><td>y</td></tr>\n"
    rl = ""
    for i in range(end-start+1):
        x = start + i
        y = 4*(x**3) + 12*(x**2) + 7*x
        rformat=rformat.replace("x",str(x))
        rformat=rformat.replace("y",str(y))
        rl += rformat
        rformat="\t\t<tr><td>x</td><td>y</td></tr>\n"
    rl=rl[2:len(rl)-1]
    table=table.replace("_TRS_",rl)
    return table
        

def generateBody():
    body = ""
    body += "<h1>My Favorite Polynomial</h1>\n"
    body += "\t<p>My favorite polynomial is f(x) = 4x^3 + 12x^2 + 7x. I like this polynomial because it is derived from my birthday. I was born on April 12th, 2007, and"
    body += " my facorite polynomial shows this month, date, and year in order. I also like this polynomial since the input f(19) is equal to 31635, which was the room number"
    body += " for the hotel room I stayed in during my first trip to Orlando</p>\n"
    body += makePolyTable(-20,50)
    #add more parts onto the body here!
    return body

page = page.replace("_TITLE_", PAGE_TITLE)
page = page.replace("_BODY_",generateBody())

print(page)
