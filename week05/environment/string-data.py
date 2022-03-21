#!/bin/python

myString = "This is a string"  # assign value to variable
print(myString)    # print variable
print(type(myString)) # print datatype of variable
print(myString + "is of the data type " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name?")
print(name)

color = input("What is your favourite colour? ")
animal = input("What is your favourite animal? ")
print("{}, you lika a {} {}!".format(name,color,animal))

