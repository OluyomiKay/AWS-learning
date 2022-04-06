import matplotlib.pyplot as plt
import random as r

cpu = "CPU"

n = int(input("Read CPU = "))

usage = {}

i = 1
while i <= n:
    currentCPU = cpu+str(i) #Labelling CPUs
    usage[currentCPU] = r.randint(1,100)
    i += 1

X = range(len(usage))
Y = list(usage.values())
labels = list(usage.keys())

plt.bar(X,Y,tick_label=labels, width=0.4,color='green')
plt.show()