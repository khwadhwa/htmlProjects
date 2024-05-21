#! /usr/bin/python3
print("Content-Type: text/html\n\n")

import matplotlib.pyplot as plt
import matplotlib.axis as ax

starter = '''<!DOCTYPE HTML5>
    <head>
        <meta charset="UFT-8">
        <meta name="viewport" content="width=device-width, initial scale=1">
        <link href="css.css" rel="stylesheet" type="text/css">
        <title>_TITLE_</title>
    </head>
    <body>
        _BODY_
    </body>'''

header = '<h1>_HEADER_</h1>'
tab = " " * 4
ka = '<p>'
da = ''
ba = ''
p = "<p>Welcome to our homepage! We are DP3 (Daniel, Khush, and Barron), and our data examines the discrepencies related to race and sex in college admissions and how these demographics have changed over time.</p>"

def khushChart():
    csv = open("acceptance.csv", "r")
    data = csv.read()

    #List Processing
    dataList = data.split("\n")
    for item in dataList:
        dataList[dataList.index(item)] = item.split(",")
    dataList = dataList[2:len(dataList)-1]

    #Data Lists Creation (each includes the number of individuals enrolled in college by the respective race and gender or the type of college
    year, males, females, white, black, hispanic, asian = ([] for i in range(7))
    for item in dataList:
        year.append(float(item[0]))
        males.append(float(item[7]))
        females.append(float(item[9]))
        white.append(float(item[11]))
        black.append(float(item[14]))
        hispanic.append(float(item[17]))
        asian.append(float(item[19]))

    #Plot #1: Gender
    fig, axs = plt.subplots(2,figsize=(10,15))
    axs[0].plot(year,males,label="Males",color="#000000")
    axs[0].plot(year,females,label="Females",color="#d62976")
    axs[0].legend(loc='upper left')
    axs[0].set_title("% of Young Adults in College by Gender")
    axs[0].set_xlabel("Year")
    axs[0].set_ylabel("% Young Adults in College")
    #Plot #2: Race
    axs[1].plot(year,black,label = "Black",color="#000000")
    axs[1].plot(year,white,label = "White",color="#808080")
    axs[1].plot(year,hispanic,label = "Hispanic",color="#964B00")
    axs[1].plot(year[19:],asian[19:],label = "Asian",color="#FFD700")
    axs[1].legend(loc='upper left')
    axs[1].set_title("% Of Young Adults in College by Race")
    axs[1].set_xlabel("Year")
    axs[1].set_ylabel("% Young Adults in College")
    open("admissions.png", "w")
    plt.savefig("admissions.png")
    
def barronChart():
    with open('fig17a.csv', 'r') as text:
        data = text.read()
        data = data.split('\n')

    #removing terms and symbols that are not needed
    data[0] = data[0][len('"Figure SA-17A.')+1:]
    data[0] = data[0][:len(data[0])-2]
    data[1] = data[1][1:]
    data = data[:len(data)-6]
    print(data)

    #unorthodox method to split last term into list without removing commas from number
    data[len(data)-1] = data[len(data)-1].split('"')
    data[len(data)-1] = data[len(data)-1][:-1]
    data[len(data)-1][0] = data[len(data)-1][0][:-1]
    for c in data:
        print(c)
    axis = []
    categories = []
    for i in range(len(data)):
        if '%' in data[i]: #ditto
            data[i] = data[i].split('"')
            data[i] = data[i][:-1]
            data[i][0] = data[i][0][:-1]
            axis += [data[i][0][data[i][0].find('(')+1:data[i][0].find('%')]]
            categories += [data[i][0][:data[i][0].find('(')]]
    #setting up percentages and labels
            
    #creating pie chart
    import matplotlib.pyplot as fig17
    fig17.figure(figsize = (15,10))
    fig17.pie(axis, labels = categories, colors = ['firebrick', 'indianred', 'lightcoral', 'lightpink', 'pink'], autopct ='%1.0f%%')
    font = {'family':'monospace','color':'darkblue','size':15,'weight':'bold'}
    fig17.title(data[0], fontdict = font)
    legend = fig17.legend(title = data[1], loc = 'lower center')
    title = legend.get_title()
    title.set_color('blue')
    title.set_size(12)
    title.set_weight('bold')
    fig17.savefig("pellgrant.png")

#navigation bar
def createNavBar():
    navbar = '''
        <nav>
            <ul>
                <li><a href='makeWebsite.py'>Home</a></li>
                <li><a href='Debt.html'>Debt (Daniel)</a></li>
                <li><a href='Admissions.html'>Admissions (Khush)</a></li>
                <li><a href="PellGrants.html">Pell Grants (Barron)</a></li>
            </ul>
        </nav>\n'''
    return navbar[:len(navbar)-1]

hpbody = createNavBar() + "\n" + tab + header.replace("_HEADER_","Homepage") + "\n" + tab + p
homepage = starter.replace("_TITLE_","DP3 DataProject").replace("_BODY_",hpbody)

print(homepage)

khushChart()

