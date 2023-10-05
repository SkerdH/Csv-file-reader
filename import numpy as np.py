import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = .25
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
IT = [12, 30, 1, 8, 22]
ECE = [28, 6, 16, 5, 10]
CSE = [29, 3, 24, 25, 17]

# Set position of bar on X axis
graphtest = []
i = 0
while i < 5:
        test = [i for i in range(5)]
        graphtest.append(test)
        i += 1
l = 0
while l < 5:    
        graphtest[l] = ([x + barWidth for x in graphtest[l-1]])
        l +=1
#print(listtest[1])

#listtest[2] = np.append([x + barWidth for x in listtest[0]])
#br3 = [x + barWidth for x in br2]
#listtest.tolist()
counter = 0
br = []
print(graphtest)
'''
while counter < (5):
     listtest= np.append([x+barWidth for x in listtest[counter-1]])
     counter +=1
     print(listtest)
'''
# Make the plot
count2 = 0
while count2 < 5:
        plt.bar(graphtest[count2], IT, color ='r', width = barWidth, edgecolor ='grey', label ='IT')
        count2 += 1
        print(count2)
 
# Adding Xticks
plt.xlabel('Branch', fontweight ='bold', fontsize = 15)
plt.ylabel('Students passed', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(5)],
        ['2015', '2016', '2017', '2018', '2019'])
 
plt.legend()
plt.show()