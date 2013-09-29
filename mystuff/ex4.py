# -*- coding: utf-8 -*-


# Variabler
cars =100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Utskrift
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


# NameError: name 'car_pool_capacity' is not defined
# variabelen er ikke definert, altså den har ikke noe å hente ut fra den variabelen
# Grunnen til dette er at car pool variabelen er skrevet carpool_capacity og car_pool_capacity

# 2 Floating-point er desimaltall, ved å bruke dette minst et sted vil man få desimaltall
# som svar videre.



