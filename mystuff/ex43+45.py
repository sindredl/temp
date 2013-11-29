from sys import exit
from random import randint
import ex45player
#imports the player class that is beeing called in bottom with print statement
#imports the exit function used to exit when dead or game is over.

class Room(object):
	
		def enter(self):
			print "room under construction."
			exit(1)
			
#Class that runs the game and takes use of the  Room class to enter rooms			
class Engine(object):
	
	def __init__(self, room_map):
		self.room_map = room_map
		
	def play(self):
		current_room = self.room_map.opening_room()
		
		while True:
			print "\n----"
			next_room_name = current_room.enter()
			current_room = self.room_map.next_room(next_room_name)
		
#calls exit function if dead class is called.	
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
	
		#Checks if the inupt has relevant info and returns the mapped name of the class.
		if  "home" in next or "behind" in next:
			return 'home'
		elif  "cafeteria" in next or "left" in next:
			return 'cafeteria'
		else:
			return 'dead'
		
class home(Room):
	
	def enter(self):
		print "You've now come home, and you can rest in peace and watch TV."
		print "So if you wan't to go out tonight, you should have at least 1000 NOK"
		print "How much money do you currently have?"
	
		next = raw_input(":~~~")
		
		if next.isdigit():
			cash = int(next)
		#Checks if the user input is a digit/integer value with the isdigit function, if it is, the value is assigned to variable cash.	
		else:
			print "What number is that?!"
			return 'home'
		#if the user input is a digit/integer it checks again if it is under 1000.
		if cash < 1000:
			print "Sorry dude, you'll have to spare it for food..."
			exit(0)
		#if inuput is not under 1000
		else:
			print "You're rich! lets go buy beer."
			return 'dead'
		
class cafeteria(Room):
	
	def enter(self):
		print "You've come to the cafeteria."
		print "You can go in and out of the cafeteria again or you can go home."
		print "What do you wan't do do?"
	
		next = raw_input(":~~~")
	
		if "cafeteria" in next:
			return 'cafeteria'
			
		elif "home" in next:
			return 'home'
			
		else:
			return 'dead'

		
#Maps the room classes to a name in a dictionary that is used to enter the room/class.		
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
		

#sets a_map variable to the first room school, then the map from is handed to the engine class(class school)
#nameinput is user input handed to the player class in ex45player
a_map = RoomMap('school')
a_game = Engine(a_map)
nameinput = raw_input("Navnet ditt mr?")
player = ex45player.Player(nameinput)
print "Hello %s !" % player.name
a_game.play()


