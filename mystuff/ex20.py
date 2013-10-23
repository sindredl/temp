# -*- coding: utf-8 -*-
#Importerer argv fra sys modulen.
from sys import argv

#Gir 2 variabler til argv'en.
script, input_file = argv

#Funksjon med ett parameter som kan lese og printe ut fila.
def print_all(f):
	print f.read()
	
#Funksjon med en rewind funksjon som går tilbake til første linje i filen.
def rewind(f):
	f.seek(0)

#funksjon med to parametere, teller antall linjer og skriver de ut.	
def print_a_line(line_count, f):
	print line_count, f.readline()
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)