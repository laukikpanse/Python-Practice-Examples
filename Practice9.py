#Write a Python program to get a new string 
#from a given string where "Is" has been 
#added to the front. If the given string 
#already begins with "Is" then return the string unchanged.

my_string = input("Please enter a string: ")

if (my_string[0] == "I" and my_string[1] == "s"):
	print(my_string)

else:
	print("Is"+my_string)