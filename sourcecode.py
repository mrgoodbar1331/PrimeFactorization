# This is a funtion that lists the prime factors of any integer

def getnumber():
	"""This is in order to handle an exception and run a loop at the same time"""
	
	print "\nEnter a positive integer and then recieve the prime factors!\n"
	print "Note: Guaranteed correct up to about 200,000; can do most 7 digit numbers.\n"
	print "Past that, it's hit or miss.\n"
	number = raw_input(">")
	return number

def primefactorization():
	""" This function will return a list of the prime factors of any number. This
	function depends on a txt file that contains a list of primes. The program
	will ask the user to input the location of this file."""
	
	 
	
	# remove the hashtags above and replace the directory below with an "a"
	
	with open(a, 'r') as file:
		lines = file.readlines()
		file.close()
		
	list_of_primes = []
		
	for prime in lines:
		list_of_primes.append(int(prime.strip()))
		
	
	while True:
		number = getnumber()
		try:
			selection = int(number)
			if selection < 2:
				print "Your number is below 2! Choose again!"
			else:
				break
		except ValueError:
			print "The number you entered is not valid!"
			
	primefactors = []
	prgnumb = selection
	
	for prime in list_of_primes:
		if prime > selection / 2:
			break
		else:
			while True:
				if prgnumb % prime == 0:
					primefactors.append(prime)
					prgnumb = prgnumb / prime
				else:
					break
	
	if primefactors == []:
		print "Your number is a prime!"
	else:
		print primefactors
		print "There ya go!\n"			
				

print "\nPlease enter the location of the provided prime number text file\n"
print "Example: \"C:\\Users\\Editor\\mystuff\\primes-to-100k.txt\"\n"
a = raw_input(">")
				
while True:
	primefactorization()
	print "Press CTRL-C to exit; press ENTER to continue.\n"
	raw_input()
	
	
	
		
	
