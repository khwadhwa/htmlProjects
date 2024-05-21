#! /usr/bin/python3
print("Content-Type: text/html\n\n")

import matplotlib.pyplot as plt

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
#Text formats for substitution into the base HTML
header = '<h1>_HEADER_</h1>'
tab = " " * 4
ka = '<center><p>Many interesting trends can be seen in these graphs. For example, as male college rates were high prior to the 1990s, they were overtaken by women in 1990, who have maintained a 15% higher college admissions rate to the modern day. Race is also a key factor, and shows to emphasize the importance and accessibility of college to various racial groups. While Asian admissions rates have been traditionally high, a significant rise can be noticed in the hispanic population after 2010 as a result of new financial aid programs put out by FAFSA. All the other groups exhibit a slightly upwards trend, as college becomes more critical to modern society.</p></center>'
da = "<center><p>Unequal student debt affects students of color with higher interest rates and inflexible repayment plans. Employment discrimination after graduation adds to the burden of debt, perpetuating racial inequalities. This cycle of debt hinders financial stability and socio-economic progress. We must prioritize equitable access to education to ensure all students have equal opportunities to succeed.</p></center>"
ba = "<center><p>Accessing college tends to require lots of money. Because of this, many families are not able to afford to pay for such universities. Thus, undergraduate students that are in great financial need are eligible for pell grants.<br><br>What is a pell grant?<br>Federal pell grants are financial aid gifted to students to help them pay for education. Unlike loans, they are not required to be paid back (under most conditions). Eligibility for one depends on the circumstances of your attendance to school and your family's ability to economically support itself. Remaining eligible for a pell grant is mainly based on submitting a Free Application for Federal Student Aid (FAFSA) form.<br><br>There are numerous limiting conditions to receiving a pell grant, including your history in the educational system and not having any record of a sexual offense. Age is also a major factor: in general, the more young you are, the higher your eligibility for one can be. The graph below presents this idea by showing the distribution of pell grants sorted by age 2-3 years ago. <br><br>The actual numbers of the distribution are as follows:<br>19 or younger (1,491,762)<br>20 to 23 (2,141,351)<br>24 to 30 (1,395,596)<br>31 to 40 (804,106)<br>41 and Older (388,589)<br>(Total Number of People: 6,221,404)</p></center>"
p = "<center><p>Welcome to our homepage! We are DP3 (Daniel, Khush, and Barron), and our data examines the discrepencies related to race and sex in college admissions and how these demographics have changed over time.</p></center>"
hpimg ='<br><br><img src="college.jpg">'

#Khush's Chart (Overlooking the Admission Rates as a Percentage of Young Adults enrolled in College)
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
    axs[1].plot(year[2:],hispanic[2:],label = "Hispanic",color="#964B00")
    axs[1].plot(year[19:],asian[19:],label = "Asian",color="#FFD700")
    axs[1].legend(loc='upper left')
    axs[1].set_title("% Of Young Adults in College by Race")
    axs[1].set_xlabel("Year")
    axs[1].set_ylabel("% Young Adults in College")
    open("admissions.png", "w")
    plt.savefig("admissions.png")
  
#Barron's Chart (Depicts the distributiuon of Pell Grants to various Age Groups)  
def barronChart():
    with open('fig17a.csv', 'r') as text:
        data = text.read()
        data = data.split('\n')

    #removing terms and symbols that are not needed
    data[0] = data[0][len('"Figure SA-17A.')+1:]
    data[0] = data[0][:len(data[0])-2]
    data[1] = data[1][1:]
    data = data[:len(data)-6]

    #unorthodox method to split last term into list without removing commas from number
    data[len(data)-1] = data[len(data)-1].split('"')
    data[len(data)-1] = data[len(data)-1][:-1]
    data[len(data)-1][0] = data[len(data)-1][0][:-1]
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
    plt.figure(figsize = (15,10))
    plt.pie(axis, labels = categories, colors = ['firebrick', 'indianred', 'lightcoral', 'lightpink', 'pink'], autopct ='%1.0f%%')
    font = {'family':'monospace','color':'darkblue','size':15,'weight':'bold'}
    plt.title(data[0], fontdict = font)
    legend = plt.legend(title = data[1], loc = 'lower center')
    title = legend.get_title()
    title.set_color('blue')
    title.set_size(12)
    title.set_weight('bold')
    plt.savefig("pellgrant.png")

#Daniel's Chart(Examines the post-College debt of individuals, broken down by race)
def danielChart():
    #Open csv file & convert to a list
    file = open("fig-16.csv")
    file_content = file.read().split("\n")
    file_content = file_content[:len(file_content) - 1]
    file.close()

    #Title
    main_title = file_content[0]

    #Debt Lists
    asian_debt = []
    black_debt = []
    hispanic_debt = []
    white_debt = []
    all_debts = []

    #Loop through file_content to extract each race's info
    for i in range(1, len(file_content)):
        file_content[i] = file_content[i].split(",")
        if file_content[i][0] == "Asian":
            asian_debt = file_content[i]
        if file_content[i][0] == "Black":
            black_debt = file_content[i]
        if file_content[i][0] == "Hispanic":
            hispanic_debt = file_content[i]
        if file_content[i][0] == "White":
            white_debt = file_content[i]

    #Remove percent signs from strings and convert strings to integers
    for i in range(1, len(asian_debt)):
        asian_debt[i] = int(asian_debt[i].replace("%", ""))
        black_debt[i] = int(black_debt[i].replace("%", ""))
        hispanic_debt[i] = int(hispanic_debt[i].replace("%", ""))
        white_debt[i] = int(white_debt[i].replace("%", ""))

    #All Debts Data (To make extracting data easier)
    all_debts = [asian_debt, black_debt, hispanic_debt, white_debt]

    fig, axs = plt.subplots(5, figsize=(10, 20))
    barnum = 0

    #Bar colors: yellow, black, orange, gray
    barcolors = ["#FFD700", "#000000", "#FFA500", "#808080"]

    #Bar Graph (Race v.s Debt% Per Race)
    races = []
    debt = []
    for i in range(len(all_debts)):
        races.append(all_debts[i][0])
        debt.append(all_debts[i][1])
    axs[barnum].bar(races, debt, edgecolor = "red")
    axs[barnum].set_title(main_title)
    axs[barnum].set_xlabel("Races")
    axs[barnum].set_ylabel("% of College Debt")
    barnum += 1

    #(Race debt categories)
    xaxis = file_content[1][2:]
    index = 1
    for label in xaxis[1:]:
        build = ""
        for c in label:
            if c == "t":
                break
            if c.isdigit():
                build += c
        xaxis[index] = build
        index += 1

    for race in all_debts:
        axs[barnum].bar(xaxis, race[2:len(race)], color = barcolors[barnum-1], edgecolor = "red")
        axs[barnum].set_title(race[0] + " Debt")
        axs[barnum].set_xlabel("Debt")
        axs[barnum].set_ylabel("Percent")
        barnum += 1

    #Vertical Space Between Graphs
    plt.subplots_adjust(hspace=0.5)

    plt.savefig("debt.png")


#navigation bar
def createNavBar():
    navbar = '''<nav>
            <ul>
                <li><a href='collegeData.py'>Homepage</a></li>
                <li><a href='debt.html'>Debt (Daniel)</a></li>
                <li><a href='admissions.html'>Admissions (Khush)</a></li>
                <li><a href="pellgrants.html">Pell Grants (Barron)</a></li>
            </ul>
        </nav>\n'''
    return navbar[:len(navbar)-1]
#Creation of the homepage
hpbody = createNavBar() + "\n" + tab*2 + header.replace("_HEADER_","Homepage") + "\n" + tab*2 + p + "\n" + tab*2 + hpimg
homepage = starter.replace("_TITLE_","DP3 DataProject").replace("_BODY_",hpbody)
print(homepage)

#Creation of the charts from each of our functions
khushChart()
barronChart()
danielChart()

#Image strings with paths
kcp = '<center><img src="admissions.png" alt="College Admissions Charts by Gender and Race"></center>'
dcp = '<center><img src="debt.png" alt="College Debt Chart by Race"></center>'
bcp = '<center><img src="pellgrant.png" alt ="Pell Grant Recipients"></center>'
#Creation of subpages
ahtml = open("admissions.html", "w")
admissionsbody = createNavBar() + "\n" + tab*2 + header.replace("_HEADER_","Admissions (Khush)") + "\n" + tab*2 + ka + "\n" + tab*2 + kcp
afinal = starter.replace("_TITLE_","Admissions (Khush)").replace("_BODY_",admissionsbody)
print(afinal, file=ahtml)
ahtml.close()

bhtml = open("pellgrants.html", "w")
pellbody = createNavBar() + "\n" + tab*2 + header.replace("_HEADER_","Pell Grants (Barron)") + "\n" + tab*2 + ba + "\n" + tab*2 + bcp
bfinal = starter.replace("_TITLE_","Debt (Daniel)").replace("_BODY_",pellbody)
print(bfinal, file=bhtml)
bhtml.close()

dhtml = open("debt.html", "w")
databody = createNavBar() + "\n" + tab*2 + header.replace("_HEADER_","Debt (Daniel)") + "\n" + tab*2 + da + "\n" + tab*2 + dcp
dfinal = starter.replace("_TITLE_","Debt (Daniel)").replace("_BODY_",databody)
print(dfinal, file=dhtml)
dhtml.close()
