from sys import exit

def over(soOver):
    print soOver, "Game Over!"
    exit(0)



def  home():
	print "You've now come home, and you can rest in peace and watch TV."
	print "So if you wan't to go out tonight, you should have at least 1000 NOK"
	print "How much money do you currently have?"
	
	next = raw_input(":~~~")
	if next.isdigit():
		cash = int(next)
	else:
		over("That kind of money won't be good for any beer.")
		
	if cash < 1000:
		print "Sorry dude, you'll have to spare it for food..."
		exit(0)
	else:
		over("You're rich! lets go buy beer.")



def cafeteria():
	print "You've come to the cafeteria."
	print "You can go in and out of the cafeteria again or you can go home."
	print "What do you wan't do do?"
	
	next = raw_input(":~~~")
	
	if "cafeteria" in next:
		cafeteria()
	elif "home" in next:
		home()
	else:
		over("Sorry, can't go anywhere else now, please wait for further development.\n or seek updates from author: sindredl@msn.com.")
	





def school_hall():
	print "You've now entered the school hall."
	print "The way home is behind you and the cafeteria is to your left"
	print "Where do you wan't to you go?"
	
	next = raw_input(":~~~")
	
	
	if  "home" in next or "behind" in next:
		home()
	elif  "cafeteria" in next or "left" in next:
		cafeteria()
	else:
		over("Not an option,")
		
school_hall()


	
