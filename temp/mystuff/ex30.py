# -*- coding: utf-8 -*-
people = 30
cars = 40
buses = 15


if cars > people:
		print " We should take the cars."
elif cars < people:
		print "We should not take the cars."
else:
		print "We can't decide"


if buses > cars:
		print "That's too many buses."
elif buses < cars:
		print  "Maybe we could take the buses."
else:
		print "We still can't decide."


if people > buses:
		print "Allright, let's just take the buses."
else:
		print "Fine, let's just stay home then."



#Hvis en ting er sant print dette, (if) eller hvis dette er sant, print dette (elif aka elseif)
#Hvis ingen av påstandene over er sanne, print dette: (else)


if cars > people and buses < cars:
		print "It's true what you're saying that It is more cars(%d) than people(%d), \nwhile It's also more cars(%d) than buses.(%d)" % (cars, people, cars, buses)

#Hvis hver person får en bil og det da er 0 eller flere biler igjen, skriv ut følgende.
#Hvis ikke hver person får en bil hver skriv ut følgende.	
if (cars - people) >= 0:
		print "It's atleast one car for each person!"
else:
		print "We don't have a car for each person!"
		

		
