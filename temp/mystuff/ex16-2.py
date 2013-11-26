
user_input = raw_input("type filename")

file = open(user_input, 'w')

print "You have now chosen the file %r" % user_input

user_input2 = raw_input("What do you want to store in the file %r?" % user_input)


print "Writing %r to file" % user_input2

file.write(user_input2)
file.close()