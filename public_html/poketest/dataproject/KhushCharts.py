import matplotlib.pyplot as plt
import matplotlib.axis as ax
csv = open("acceptance.csv", "r")
data = csv.read()

#List Processing
dataList = data.split("\n")
for item in dataList:
    dataList[dataList.index(item)] = item.split(",")
dataList = dataList[2:len(dataList)-1]

#Data Lists Creation (each includes the number of individuals enrolled in college by the respective race and gender or the type of college
year, twoyear, fouryear, males, females, white, black, hispanic, asian, islanders, native, multiracial = ([] for i in range(12))
for item in dataList:
    year.append(float(item[0]))
    males.append(float(item[7]))
    females.append(float(item[9]))
    white.append(float(item[11]))
    black.append(float(item[14]))
    hispanic.append(float(item[17]))
    asian.append(float(item[19]))
    islanders.append(float(item[21]))
    native.append(float(item[24]))
    multiracial.append(float(item[27]))

#Plot #1: Gender
fig, axs = plt.subplots(2,figsize=(10,15))
axs[0].plot(year,males,label="Males")
axs[0].plot(year,females,label="Females")
axs[0].legend(loc='upper left')
axs[0].set_title("% of Young Adults in College by Gender")
axs[0].set_xlabel("Year")
axs[0].set_ylabel("% Young Adults in College")
#Plot #2: Race
axs[1].plot(year,black,label = "Black")
axs[1].plot(year,white,label = "White")
axs[1].plot(year,hispanic,label = "Hispanic")
axs[1].plot(year[19:],asian[19:],label = "Asian")
axs[1].legend(loc='upper left')
axs[1].set_title("% Of Young Adults in College by Race")
axs[1].set_xlabel("Year")
axs[1].set_ylabel("% Young Adults in College")
open("admissions.png", "w")
plt.savefig("admissions.png")