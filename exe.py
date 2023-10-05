from django.shortcuts import render
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv
import io
from django.core.validators import FileExtensionValidator 
from django.db import models

##creating values
x_values = []
y_values = []

##open and read file
with open('sample_data.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x_values.append(int(row[0]))
        y_values.append(int(row[1]))

##size and layout
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

##labels
plt.title('Graph of Your Data')
plt.xlabel('x values')
plt.ylabel('y values')

##plots a line graph
plt.plot(x_values, y_values)

##plots a scatter plot
plt.scatter(x_values, y_values)

##creates a buffer
buf = io.BytesIO()

##copies plot into buffer
plt.savefig(buf, format='png')
buf.seek(0)

##show png
img_tag = plt.getElementById('fig')
img_tag.src = "img_str"
buf.close()