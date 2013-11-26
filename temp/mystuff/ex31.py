print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print  "2. Scream at the bear."
	
	bear = raw_input("> ")
		
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear
			
			
			
			
elif door == "2":
		print "You stare into the endless abyss at Cthulu's retina."
		print "1. Blueberries."
		print "2. Yellow jacket clothespins."
		print "3. Understanding revolvers yelling melodies."
	
	
	
		insanity = raw_input("> ")

		if insanity  == "1" or insanity  == "2":
			print "Your body survives powered by a mind of jello. Good job!"
		else:
			print "The insanity rots your eyes into a pool of much. Good job!"
	
	
	
elif door =="3":
	print "You meet Harry Potter"
	print " 1. Cast Avada Cadavra / kill him."
	print "2. Run away in fear"
	
	potter = raw_input("> ")
	
	if potter == "1":
		print "Harry Potter dodges your spell, disarms you, and then kill you"
		print " Game Over"
		
	elif potter == "2":
		print "Harry Potter cast's a snowball on you and you fall, then he kills you. Twice."
		print "Game over. Twice"
	else:
		print "Invalid choice, you're now dead."
		print "Game Over."
	
	
else:
    print "You stumble around and fall on a knife and die.  Good job!"