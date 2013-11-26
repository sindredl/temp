# -*- coding: utf-8 -*-

from sys import argv

script, user_name, nickname = argv
prompt = '~>'

print
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions, %s AKA %s." % (user_name, nickname)
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer= raw_input(prompt)

print "How old might you be, %s?" % user_name
alder = raw_input(prompt)

print """
Allright, %r. So you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice. 
You are also %r old.
""" % (nickname, likes, lives, computer, alder)


# http://pot.home.xs4all.nl/infocom/zork1.html  <- Zork and Adventure tekstspill.


