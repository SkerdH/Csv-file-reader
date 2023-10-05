import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import randint

#Inputs the CSV file
df = pd.read_csv('sample4.csv',header=None)
data = pd.DataFrame(df)

#Takes the first row of the CSV and remove the first element
row1 = df.iloc[0]
row1.pop(0)

#Asks user which column they would like to use for x axis labels and takes it from the csv file
x_lab = input("Which Columns would you like to use for your x_axis labels: ")
col_1= list(df[int(x_lab)])
col_1.pop(0)
done = 0
x_value = []
count = 0

#Asks user for input, which Collumns for X value, which collumn to input the data
while done != 'n':
    x_val = input("Which Columns would you like to use for you X values: ")
    x_value.append(x_val)
    done = input("Would you like to include anymore Columns, y/n: ")
    count += 1
#Assigns how large the graph is going to be
fig = plt.subplots(figsize =(15, 8))
y_value = col_1
barWidth = 0.25
counter = 0
list1 = []
chosencol = []
legend = []
#Takes chosen collomns and puts them into a new array
for i in x_value:
        list1 = list(df[int(i)])
        legend.append(row1[int(i)])
        list1.pop(0)
        chosencol.append(list1)
#Turns list of strings into list of integers 
chosencol = [list(map(int, i) ) for i in chosencol]
max12 = max(map(max, chosencol))
# Sets bar position on the X-Axis
br = np.arange(len(chosencol[0]))
br = []
i = 0
#Sets up a array which will hold the bar positions
while i < len(x_value):
        test = [i for i in range(len(chosencol[0]))]
        br.append(test)
        i += 1
l = 0
#Adds the bar width to the position of each bar on the array
while l < len(x_value):    
        br[l] = ([x + barWidth for x in br[l-1]])
        l +=1
#Makes the plot using a loop to allow the user for as many entries as possible
bar_counter = 0
#Add random colors to the graph
colors = []
for i in range(10):
    colors.append('#%06X' % randint(0, 0xFFFFFF))
while bar_counter < len(x_value):
        plt.bar(br[bar_counter], chosencol[bar_counter], color = colors[bar_counter], width = barWidth, edgecolor ='grey', label = legend[bar_counter])
        bar_counter += 1
# Customizes The x axis label, y axis label, the size of the y axis, adds title, and finally plots the graph 
plt.xlabel('Item choice', fontweight ='bold', fontsize = 15)
plt.ylabel('Data Values', fontweight ='bold', fontsize = 15)
plt.yticks(np.arange(0, max12 + 10, 10))
plt.xticks([r + barWidth for r in range(len(chosencol[0]))],
        y_value)
plt.title("Your Data Graphed")
plt.legend()
plt.show()
