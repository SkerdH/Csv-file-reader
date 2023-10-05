import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import glob
import os.path
from random import randint

#Function to sort database by one column ignoring inputted rows 
#used to sort x-axis values without interfering with column labels
def sort_values(df, column_names, ascending=False, fixed=None):
    if fixed is None:
        return df.sort_values(column_names, ascending=ascending)
    idx = df.index.get_indexer(fixed).tolist()
    s_df = df.sort_values(column_names, ascending=ascending).T
    keep_cols = s_df.columns.difference(fixed, sort=False)
    out = s_df[keep_cols]
    for (loc, name) in zip(idx, fixed):
        out.insert(loc, name, s_df[name])
    return out.T

def create_graph(x_axis, columns):
        #Finds the most recently uploaded csv file
        files = glob.glob('test.csv')
        max_file = max(files, key=os.path.getctime)

        #Inputs the CSV file
        df = pd.read_csv(max_file,header=None)
        data = pd.DataFrame(df)
        length = len(data.columns)

        #Sorts database by x-axis
        data.rename(columns={x_axis:'axis'}, inplace=True)
        popped_col = list(data.pop('axis'))
        axis_label = popped_col[0]
        fail = ''
        while fail != 'fail':
                try:
                        popped_col = [int(i) for i in popped_col]
                        data['axis']= popped_col
                        data = sort_values(data, ['axis'], ascending=True, fixed = [0])
                except:
                        data['axis']= popped_col
                        fail = 'fail'                        

        #Takes the first row of the CSV
        row1 = df.iloc[0]

        #Reads the column chosen for x axis labels and takes it from the csv file
        col_1= list(data['axis'])
        col_1.pop(0)
        done = 0
        x_value = []
        x_val = 0
        count = 0

        #iterates over every column in the file, appends column to x_value if included in input list
        while count != length:
                if count in columns:
                        x_val = count
                        x_value.append(x_val)
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
        for i in range(length):
                colors.append('#%06X' % randint(0, 0xFFFFFF))
        while bar_counter < len(x_value):
                plt.bar(br[bar_counter], chosencol[bar_counter], color = colors[bar_counter], width = barWidth, edgecolor ='grey', label = legend[bar_counter])
                bar_counter += 1


        # Customizes The x axis label, y axis label, the size of the y axis, adds title, and finally plots the graph 
        plt.xlabel(axis_label, fontweight ='bold', fontsize = 15)
        plt.ylabel('Data Values', fontweight ='bold', fontsize = 15)
        plt.yticks(np.arange(0, max12 + 10, 10))
        bottom, top = plt.ylim()
        print("Bottom: " + str(bottom) + "\nTop: " + str(top))
        plt.xticks([r + barWidth for r in range(len(chosencol[0]))],
                y_value)
        plt.title("Your Data Graphed")
        plt.legend()

        plt.savefig("ExcelGrouping\static\graph.png")