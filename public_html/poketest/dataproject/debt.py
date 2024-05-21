import matplotlib.pyplot as plt

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
