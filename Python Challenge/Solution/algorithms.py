import sys
import re
import utils as u
import math as m
import csv
import pprint 
import statistics as s

#1 - The Middle Average Algorithm
def middleaverage():
    count = 0
    total = 0
    minimum = sys.maxsize
    maximum = -sys.maxsize
    value = int(u.read("Value: "))
    while value != -1:
        count+=1
        total += value
        minimum = min(minimum,value)
        maximum = max(maximum,value)
        value = int(u.read("Value: "))
    if count >=2:
        print(f'Middle average = {total/(count-2):.2f}')
    else:
        print(f'Count = {count}; you must enter more than 2 values!')
        
#2- The Longest Dry Spell Algorithm
def longestdryspell():
    maximum = -sys.maxsize
    count = 0
    rain = int(u.read("Rainfall: "))
    while rain != -1:
        if rain == 0:
            count +=1
        else:
            maximum = max(maximum,count)
            count = 0
        rain = int(u.read("Rainfall: "))
    maximum = max(maximum,count)
    print(f'Longest dry spell = {maximum}')
        
#3 - The Number to Words Algorithm
def shownum(num):
    numNames = [ "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ]
    tensNames = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundreds = int(num/100)
    rest = num % 100
    tens = int(rest / 10)
    ones = rest % 10
    word = ""
    print(f'{hundreds} - {rest} - {tens} - {ones}')
    if hundreds > 0:
        word += numNames[hundreds] + " hundred "
    if hundreds > 0 and rest > 0:
        word += "and "
    if tens >= 2:
        word += tensNames[tens]+" "+numNames[ones]
    elif num == 0:
        word="zero"
    else:
        word += numNames[rest]
    print(word.strip())
    
def numbertoword():
    num = int(u.read("Number: "))
    while num != -1:
        shownum(num)
        num = int(u.read("Number: "))
        
#4 - The File Encryption Algorithm
def fileencryption():
    filename = u.read("File: ")
    infile = open(filename,"r")

    regex = u.read("Pattern: ")
    replace = u.read("Replacement: ")
    content = ""
    for line in infile:
        found = re.findall(regex,line)
        if(found):
            replaced = re.sub(regex,replace,line)    
            content += replaced
        else:
            content += line        
    infile.close()   
    outfile = open(filename,'w')
    outfile.write(content)
    outfile.close()
    
#5 - The IPv4 to Binary Algorithm

def binary(ip):    
    listip = ip.split('.')    
    binarylist = []
    for decoctet in listip:
        dec = int(decoctet)        
        binarylist.append(u.binaryoctet(dec)) 
    return binarylist

def flatbinarylist(binarylist,n):    
    flat = u.mergelist(binarylist)
    i = n
    while i < len(flat):
        flat[i] = 0
        i+=1
    return flat
    
def listtostring(flatlist):
    i = 0
    binary = ""
    decimal = ""
    while i < 32:
        binary += ''.join(str(e) for e in flatlist[i:i+8])
        binary +="."
        decimal += str(u.decimaloctet(flatlist[i:i+8]))
        decimal += "."
        i+=8
    return binary.strip("."), decimal.strip(".")

def maskbinary(flatlist,n):
    i = 0
    while i < len(flatlist):
        if i <= n:
            flatlist[i] = 1
        else:
            flatlist[i] = 0
        i +=1
    return flatlist
        
def networking():
    n = int(u.read("Prefix: "))
    ip = u.read("IPv4: ")
    cidr = ip+"/"+str(n)
    s = int((32 - n) / 2)   #usable subnets
    h = 32 - s              #usable hosts
    flatlist = flatbinarylist(binary(ip),n)
    binarynetwork, decimalnetwork = listtostring(flatlist)      
    flatmaskbinarylist = maskbinary(flatlist,n)
    binarynetworkmask, decimalnetworkmask = listtostring(flatmaskbinarylist)
    t = u.formattedtable("CIDR",cidr)
    t.add_row(['Binary Address',binarynetwork])
    t.add_row(['Network Address',decimalnetwork])
    t.add_row(['Binary Mask',binarynetworkmask])
    t.add_row(['Network Mask',decimalnetworkmask])
    t.add_row(['Usable Subnets',s])
    t.add_row(['Usable Hosts',h])
    print(t)
    
    
#6 - The Binary Search Algorithm:
def binary_search(numbers, e):  
    low = 0  
    high = len(numbers) - 1  
    mid = 0    
    while low <= high:          
        mid = (high + low) // 2   
        if numbers[mid] < e:  
            low = mid + 1   
        elif numbers[mid] > e:  
            high = mid - 1 
        else:  
            return mid  
    return -1  
     
def binarySearch():
    first = int(u.read("First = "))
    last  = int(u.read("Last = "))
    step  = int(u.read("Step = "))
    size  = int(u.read("Size = "))
    numbers = u.randomlist(first,last,step,size)
    numbers.sort()
    print(numbers)   
    e = int(u.read("Search for: "))
    pos = binary_search(numbers, e)
    if pos != -1:
        print(f'{e} is found at position {pos}')
    else:
        print(f'{e} does not exist in the list {pos}')
        
#7 - The Stretch of 2-Vowels Algorithm:
def vowelcount(segment):
    count = 0
    for c in segment:
       if c in "aioeu":
           count +=1
    return count

def match(word):
    for segment in word.split("z"):
        if(vowelcount(segment) == 2):
            return True
    return False

def macthcount(sentence):
    count = 0
    for word in sentence.split(" "):
        if match(word):
            count +=1
    return count

def matches():
    sentence = u.read("String: ")
    while sentence != "*":
        print(f'Matching words = {vowelcount(sentence.lower())}')
        sentence = u.read("String: ")

#8 - The Shapes Algorithm:
def arguments():
    radius = float(u.read("Radius = "))
    sides = float(u.read("Sides = "))
    return radius, sides 

def areavolume(radius):
    area = m.pi*pow(radius,2)
    volume = (4/3)*m.pi*pow(radius,3)
    return area, volume 

def shapearea(sides):
    if sides == 3:
        area = (m.sqrt(3)/4) * pow(sides,2)
        return "Triangle area = {:.3f}".format(area)
    elif sides == 4:
        area = pow(sides,2)
        return "Square area = {:.3f}".format(area) 
    elif sides == 5:
        area = (1/4)*(m.sqrt(5*(5+2*m.sqrt(5))))*pow(sides,2)
        return "Regular Pentagon area = {:.3f}".format(area)
    elif sides == 6:
        area = ((3*m.sqrt(3))/2)*m.pow(sides,2)
        return "Regular Hexagon area = {:.3f}".format(area) 
    elif sides == 7:
        area = (7/4)*m.pow(sides,2)*(1/m.tan(180/7))
        return "Regular Heptagon area = {:.3f}".format(area) 
    elif sides == 8:
        area = 2*(1+m.sqrt(2))*pow(sides,2)
        return "Regular Octagon area = {:.3f}".format(area)
    else:
        return "Shape is beyond calculation context"

def shapes():
    radius, sides = arguments()
    c_area, s_volume = areavolume(radius)
    shape = shapearea(sides)
    print(f'Circle area = {c_area:.3f}')
    print(f'Sphere volume = {s_volume:.3f}')
    print(shape)
    
    
#9 - The Cities Statistics Algorithm:
def csv_dictionary(csvfile):
    with open("worldcities.csv","r", encoding="utf8") as f:
        d = dict(filter(None, csv.reader(f))) 
    return d

def matchingcities(cities):
    matches = {}
    for key in cities.keys():
        if len(cities[key].strip()) > 0:
            if int(cities[key]) >= 1000000:
                matches.update({key:cities[key]})  
    return matches, len(matches.keys())

def stats(population):
    mean = s.mean(population)
    variance = s.variance(population)
    stdv = s.stdev(population)
    return mean, variance, stdv

def citiesstatistics():
    csvfile = u.read("CSV File: ")
    cities  = csv_dictionary(csvfile)
    pp = pprint.PrettyPrinter(indent=2,width=40) 
    matches, count = matchingcities(cities)
    pp.pprint(matches)
    print(f'Cities with population greater than 1 million: {count}')
    mean, variance, stdv = stats(list(map(int,matches.values())))
    print(f'Mean = {mean:.3f}')
    print(f'Variance = {variance:.3f}')
    print(f'Standard Deviation = {stdv:.3f}')
    
#10 - The Satellite Orbital Speed Algorithm:
def satellitespeed():
    G = 6.67*pow(10,-11)        #coefficient of gravity in Nm2/kg2
    M = 5.9722*pow(10,24)       #earth mass in Kg
    R = 6371                    #earth radius in KM
    x = int(u.read("x = "))
    y = int(u.read("y = "))
    d = m.sqrt(pow(x,2) + pow(y,2)) + R   #satellite distance from earth
    v = m.sqrt(G*(M/d))
    print(f'Satellite at position ({x},{y}) speed v = {v} m/s')