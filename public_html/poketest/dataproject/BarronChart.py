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

site = '''<html>
  <head>
    <title>TITLE</title>
    <style>
      h1 {text-align:center;}
      p.first {text-align:left;}
      p.second {text-align:right;} 
    </style>
  </head>
  <body>
    <h1>HEADING</h1>
    <p class='first'>PARAGRAPH</p>
    <p class='second'>PARAGRAPH2</p>
  </body>
</html>'''
