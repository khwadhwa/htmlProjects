#! /usr/bin/python3
print("Content-Type: text/html\n\n")

data = open("pokemon.csv", "r")
data = data.read()

import copy

starter = '''<!DOCTYPE HTML>
    <head>
        <meta charset="UFT-8">
        <meta name="viewport" content="width=device-width, initial scale=1">
        <link href="style.css" rel="stylesheet" type="text/css">
        <title>_TITLE_</title>
    </head>
    <body>
        _BODY_
    </body>'''

#Paragraph variables (to be integrated later)
p1 = "<p>Though I wasn't a big Pokemon fanatic growing up, Pokemon has had a noticeable impact on my life and was a key part of my childhood. I have fond memories of waking up early during sleepovers with my cousin to watch the TV show growing up. Though I played the games on the now archaic Nintendo 2DS, it never caught on for me like it did for some of my friends. I remember Pokemon Sun and Moon, so I think it was the best, but I think that the more recent and 'immersive' Pokemon games are messing with the spirit of the story. The opening song to the TV show sums up my view on Pokemon: Chasing our destiny!</p>"
p2 = "<p>Here is a list of all the Pokemon in the 1st Generation Pokedex. You'll note that the Pokemon are classified with various stats, types, and legendary status, which define their strength. However, total power is not the only important statistic. Some battles could be influenced by the type of Pokemon, since some types do great against each other. When taking on a Pokemon battle, make sure to have a diverse array of Pokemon types to choose from and care for them! You can see lists of Pokemon types in the 'Types' subpages. All the stats are available here!</p>"
p3 = "<p>My Top 10 Pokemon study was not the most thorough. As someone with not much experience in Pokemon, my top 10 pokemon are simply those with the highest power. Disagree and would like to see an adjustment to this site? Send an email to kwadhwa50@stuy.edu and I'll consider it!</p>"
song = '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/3OIHgTyQdiAGMmpjQaNxp3?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'

dL = data.split("\n")
for i in range(len(dL)):
    dL[i] = dL[i].split(",")
dL = dL[:len(dL)-1]

def subPages(dataList):
#Generates list of appropriate subpages for uses in the program
    dataList = dataList[1:]
    subPageList = []
    for item in dataList:
        if not item[2] in subPageList:
            subPageList.append(item[2])
        if not item[3] in subPageList:
            subPageList.append(item[3])
    subPageList.remove("")
    return subPageList

def makePokemonTable(dataList):
#Constructs a table with all Pokemon using the given csv file
    table = '''    <table>
        <head>
            <title>Pokemon</title>
        </head>
        <body>
            _BODY_
        </body>
    </table>'''
    row = "\t    <tr>\n_td_\t    </tr>\n"
    tdata = "\t\t<td>_DATA_</td>\n"
    img = '<img src="_LINK_">'
    pathf = "img/front/"
    pathb = "img/back/"
    body = ""
    #The enumerate function is used to define the string number of the photo to be imported
    for a in dataList:
        temp = ""
        i = a[0]
        temp += tdata.replace("_DATA_",img.replace("_LINK_",(pathf + str(i) + ".png")))
        temp += tdata.replace("_DATA_",img.replace("_LINK_",(pathb + str(i) + ".png")))
        for b in a:
            if b == str(0):
                b = "#"
            temp += tdata.replace("_DATA_",str(b))
        body += row.replace("_td_",temp)
    table = table.replace("_BODY_",body[5:len(body)-1])
    return table

def subPageList(dataList,stype):
#Acceps the data spreadsheet and the Pokemon type as inputs and outputs a list of Pokemon with that subtype
    pokeList = []
    dataList[0][0] = "0"
    pokeList.append(dataList[0])
    for item in dataList:
        if stype == item[2] or stype == item[3]:
            pokeList.append(item)
    reptext = navBar(subPages(dL)) + "\n" + "<center><h1>" + str(stype) + "</h1></center>\n" + makePokemonTable(pokeList)
    stypehtml = open(str(stype) + ".html", "w")
    print(starter.replace("_BODY_",reptext).replace("_TITLE_",str(stype)), file=stypehtml)
    stypehtml.close()
    return pokeList[0]

def navBar(sPL):
# Some code referenced from W3Schools    
    div = '\t<div class="_CLASS_">\n_CONTENT_\t</div>\n'
    a = '\t\t<a href= "_HTML_.html">_NAME_</a>\n'
    btn = '\t\t<button class="dropbutton">Types</button>\n'
    output = ""
    temp = ""
    for item in sPL:
        temp += "\t\t" + a.replace("_HTML_",str(item)).replace("_NAME_",str(item))
    temp = "\t\t" + div.replace("_CLASS_","dropct").replace("_CONTENT_",temp).replace("</div>","\t\t</div>")
    temp = "\t" + div.replace("_CLASS_","dropbtn").replace("</div>","\t</div>").replace("_CONTENT_","\t" + btn + temp)
    output += a.replace("_HTML_.html","makePokedex.py").replace("_NAME_","Homepage")
    output += a.replace("_HTML_","allpokemon").replace("_NAME_","All Pokemon")
    output += temp
    output += a.replace("_HTML_","top10").replace("_NAME_","Top 10")
    output = div.replace("_CLASS_","navbar").replace("_CONTENT_",output)
    return output

def top10(dataList):
#Creates a dictionary to sort Pokemon by their power levels, and then outputs that to a table by referencing the csv
    dataDict = {
}
    oDL = copy.deepcopy(dataList)
    dataList = dataList[1:]
    for i in range(len(dataList)):
        dataDict.update({dataList[i][4] : dataList[i][1]})
    valueList = []
    vLL = 10
    for key in dataDict:
        if key in dataDict:
            vLL = vLL - 1
        valueList.append(key)
        
    valueList.sort(reverse = True)
    valueList = valueList[:vLL]
    valueList.insert(0,oDL[0][4])
    tableList = []
    for value in valueList:
        for item in oDL:
            if value == item[4]:
                tableList.append(item)
    table = makePokemonTable(tableList)
    return table

#Piping to other files


hpbody = navBar(subPages(dL)) + "\n" + "\t<center><h1>Khush's Pokmeon Website</h1></center>" + "\n\t" + p1 + "\n\t" + song
homepage = starter.replace("_TITLE_","Homepage").replace("_BODY_",hpbody)
print(homepage)

for item in subPages(dL):
    subPageList(dL,item)

t10code = starter.replace("_TITLE_","Top 10 Pokemon").replace("_BODY_", navBar(subPages(dL)) + "\n" + "\t<center><h1>My Top 10 Pokemon</h1></center>" + p3 + top10(dL))
t10html = open("top10.html", "w")
print(t10code, file=t10html)
t10html.close()

allpokemoncode = starter.replace("_TITLE_","Pokedex").replace("_BODY_", navBar(subPages(dL)) + "\n" + "\t<center><h1>All Pokemon/Pokedex</h1></center>" + p2 + makePokemonTable(dL))
allpokemonhtml = open("allpokemon.html", "w")
print(allpokemoncode, file=allpokemonhtml)
allpokemonhtml.close()
    
    
