#!/usr/bin/python2.7
import random
import os
import time

def main():
	print ("\nWelcome to the rock,paper,scissor game").upper()
	print "============================================"
	user_num=user_input()
	comp_num=comp_input()
	result(user_num,comp_num)


def user_input():
	guess=raw_input("\nEnter the choice among rock, paper, scissor: ")
	if guess == 'rock':
		number= 1
	elif guess == 'paper':
		number = 2
	elif guess == 'scissor':
		number = 3
	else: 
		print "\nwrong choice...Please enter within the option!!!\n"
		time.sleep(3)
		os.system('clear')
		main()

	print "\nYou have selected ",guess,"whose code is: ",number
	return number

def comp_input():
	number =random.randrange(1,4)
	if number == 1:
		guess= 'rock'
	elif number == 2:
		guess = 'paper'
	elif number == 3:
		guess = 'scissor'
	
	print "computer selected ",guess,"whose code is: ",number
	return number

def result(user_num,comp_num):
	difference=user_num-comp_num
	global won
	global loss
	if difference == 0:
		print "\nThere is a TIE!!!\n"
		restart(won,loss)
	elif difference % 3 == 1:
		print "\nYou won the game\n"
		won=won+1
		#print 'you won',won,'number of times \n'
		#print 'you lost',loss,'number of times'
		restart(won,loss)
	elif difference % 3 == 2:
		print "\nSorry...You loss!!!\n"
		loss=loss+1
		#print 'you lost',loss,'number of times\n'
		#print 'you won',won,'number of times \n'
		restart(won,loss)

def restart(w,l):	
	global won
	global loss
	won=w
	loss=l
	print "What do you want to do now???\n"
	print "Press 1 to see the score"
	print "Press 2 to continue the game\n"

	choice=raw_input("Enter your choice: ")
	if choice == '1':
		print '\nYou lost',loss,'number of times\n'
		print 'You won',won,'number of times \n'
		
		tell=raw_input("Do you want to continue??? ")
		if tell == 'y' or tell == 'Y':
			os.system('clear')
			main()
		else:
			print "-----------------Good Bye---------------------------"
			exit();

	if choice == '2':
		os.system('clear')
		main()
	
print "Lucky to have this opportunity to work on python nicely"
won=0
loss=0
main()
			
