# This python program was built to take a bunch of 
# documents as input and determine how much of a target 
# document is similar to the other documents by 
# using various algorithms
import os

print("here is the current directory for parsing documents: " + os.getcwd())

file1 = open("./example.txt", "r")

text = file1.read() #this text file now holds the entire string from example.txt

print(text)