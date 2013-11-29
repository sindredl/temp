

#String submission

string = "I think %s is a normal thing to do in public"

def sub1(s):
	return string % s


print sub1("running")



#Multiple strings


string2 = "I think %s and %s are perfectly normal things to do in public."
def sub2(s1, s2):
    return string2 % (s1, s2)

print sub2("running", "sleeping")




#Advanced string submission
# Dict maps name to value 


"text % (name)s text" % {"name": value}

# User Instructions
# 
# Write a function 'sub_m' that takes a 
# name and a nickname, and returns a 
# string of the following format: 
# "I'm NICKNAME. My real name is NAME, but my friends call me NICKNAME."
# 

#_______________________________________

#name = "name"
#nickname = "nickname"

string2 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."
def sub_m(name, nickname):
    return string2 % {"name": name, "nickname": nickname}
    
    
print sub_m("Mike", "Goose")

# sub_m("Mike", "Goose") 
# => "I'm Goose. My real name is Mike, but my friends call me Goose."
