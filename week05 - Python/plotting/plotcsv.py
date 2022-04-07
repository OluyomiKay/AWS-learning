import matplotlib.pyplot as plt
import csv 
import collections
import numpy as np

grades = []

with open('students.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
        grades.append(row[3])

counter = collections.Counter(grades)       
frequency = counter.values()
gradeset = np.unique(np.array(grades))

plt.pie(frequency,labels = gradeset,autopct = '%.2f%%')
plt.title('Grades Distribution', fontsize = 20)
plt.legend(title = "Grades:")
plt.show()