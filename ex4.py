#!/usr/bin/python

#set how many cars we have
cars = 100
# Each car can hold this many passengers
space_in_a_car = 4.0
# We have this many drivers todau
drivers = 30 
# ...and this many passengers.
passengers = 90
# Calculate how many cars won't be driven today
cars_not_driven = cars - drivers
# The number of drivers equals the number of cars driven
cars_driven = drivers
# Calulate the total carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# Calculate average passengers per car
average_passengers_per_car = passengers / cars_driven

print "There are:", cars , "cars available."
print "There are only", drivers ,"drivers available."
print "There will be", cars_not_driven ,"empty cars today."
print "We can transport", carpool_capacity ,"people today." 
print "We need to put about", average_passengers_per_car , "in each car."