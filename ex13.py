#!/usr/bin/python

from sys import argv

script, first, second, third = argv

myprefix = raw_input("What word shall I add each word you passed in? ")

print "The script is called:", script
print "Your first variable is:", myprefix + first
print "Your second variable is:", myprefix + second
print "Your third variable is:", myprefix + third
