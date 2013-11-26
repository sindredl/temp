# -*- coding: utf-8 -*-

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheese!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
	
print "We can just give the fucntion numbers directly:"
cheese_and_crackers(20, 30)


#Gir de direkte verdier, og putter verdiene på cheese_and_crakcers som er definert i toppen.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Plusser sammen to tall til cheese_count og boxes_of_crackers.
print "We can even do math inside too:"
cheese_and_crackers(10 + 20,  5 + 6)

#Bruker de direkte verdiene gitt og plusser på 100 og 1000.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def func1(age):
	print "I am %r years old, but" % age
	name1 = raw_input("Can you guess my name? \n >:")
	
	myName = "Sindre"
	notMyName = "Alfhill"
	if(name1 == myName):
		print "%s is indeed my name!" % name1
		
	elif(name1 == notMyName):
		print "Nice try, %s Is a cool name, but unfortunately not mine :(" % name1
		
	else :
		print " %r Is unfortunately not my name.. \n Did you forget capital first letter?" % name1
		

func1("22")

