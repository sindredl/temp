# -*- coding: utf-8 -*-


# x er lik tekst og tallet 10, binær variabelen får tildelt teksten binary som verdi. osv 
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who know %s." % (binary, do_not)

# Printer det x og y variablene har blitt tildelt.
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e


