from sys import exit
from random import randint

class Room(object):
	
		def enter(self):
			print "room under construction. subclass it and implement enter()."
			exit(1)
			
			
class Engine(object):
	
	def __init__(self, room_map):
		self.room_map = room_map
		
	def play(self):
		current_room = self.room_map.opening_room()
		
		while True:
			print "\n----"
			next_room_name = current_room.enter()
			current_room = self.room_map.next_room(next_room_name)
		
		
class dead(Room):
	
	def enter(self):
			print "You're dead, Game is over"
			exit(1)
		
class school(Room):
	
	def enter(self):
		print "You've now entered the school hall."
		print "The way home is behind you and the cafeteria is to your left"
		print "Where do you wan't to you go?"
	
		next = raw_input(":~~~")
	
	
		if  "home" in next or "behind" in next:
			home()
		elif  "cafeteria" in next or "left" in next:
			cafeteria()
		else:
			dead()
		
class home(Room):
	
	def enter(self):
		print "You've now come home, and you can rest in peace and watch TV."
		print "So if you wan't to go out tonight, you should have at least 1000 NOK"
		print "How much money do you currently have?"
	
		next = raw_input(":~~~")
		
		if next.isdigit():
			cash = int(next)
			
		else:
			print "That kind of money won't be good for any beer."
			dead()
		
		if cash < 1000:
			print "Sorry dude, you'll have to spare it for food..."
			exit(0)
		
		else:
			print "You're rich! lets go buy beer."
			dead()
		
class cafeteria(Room):
	
	def enter(self):
		print "You've come to the cafeteria."
		print "You can go in and out of the cafeteria again or you can go home."
		print "What do you wan't do do?"
	
		next = raw_input(":~~~")
	
		if "cafeteria" in next:
			cafeteria()
			
		elif "home" in next:
			home()
			
		else:
			dead()

		
		
class RoomMap(object):
	
	rooms = {
        'school': school(),
        'home': home(),
        'cafeteria': cafeteria(),
        'dead': dead()
    }
       
	def __init__(self, start_room):
		self.start_room = start_room
		
	def next_room(self, room_name):
		return RoomMap.rooms.get(room_name)
		
	def opening_room(self):
		return self.next_room(self.start_room)
		


a_map = RoomMap('school')
a_game = Engine(a_map)
a_game.play()

