import itertools
import prettytable as pt
import random as r 

def read(prompt):
    return input(prompt)

def randomlist(first,last,step,size):
    return r.choices(list(range(first,last,step)),k=size)

def mergelist(binarylist):
    flat =list(itertools.chain(*binarylist))
    return flat

def binaryoctet(n):
    list1 = []
    zeros = [0,0,0,0,0,0,0,0]
    while n > 0:
        list1.append(int(n%2))
        n = int(n/2)
    reverse = list(reversed(list1))
    binary = zeros[len(reverse):len(zeros)]+reverse
    return binary

def decimaloctet(binarylist):
    reverse = list(reversed(binarylist))
    i = 0
    decimal = 0
    for e in reverse:
        decimal += e*pow(2,i)
        i +=1
    return decimal

def formattedtable(col1,col2):
    t = pt.PrettyTable()
    t.title = 'Network Configuration'
    t.field_names = [col1, col2]
    return t