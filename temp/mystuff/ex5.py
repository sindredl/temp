# -*- coding: utf-8 -*-

#Varibel setting
name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'


# Centimeter til inches/tommer
inches = 74
cm = inches * 2.54012
print "%r inches equals %r centimeters." % (inches, cm)
# Kilo til pounds.
pounds = 180
kilo = pounds * 0.453592
print "%r pounds equals %r kilos" % (pounds, kilo)





#Printing av tekst
#%s henter inn variabelen som er til høyre inn i s.
print "Let's talk about %s." % name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "His teeth are usually %s depending on the coffee." % my_teeth
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)


# Tommer og pounds til centimeter og kilo.
print "He's %d inches tall, wich is %d cm." % (my_height, cm)
print "He's %d pounds heavy,wich is %d kilos." % (my_weight, kilo)


#Printer ut alle variablene og til slutt alle variablene plusset sammen.
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
