#Laukik Narendra Panse

for i in range(0,20):
	print("The square of {0} is : {1}".format(i,i*i))

#If Program flow:

#finding the even numbers between 0 to 50

for i in range(0,51):
	#check using modulus the remainder
	if(i % 2 == 0 ):
		#If condition is satisfied then execute following
		print("{0} is an even number.".format(i))

#another example:
#find if a person is old enough to vote:


my_name = input("Please enter your name: ")
#Taking input strictly in Integer format
my_age = int(input("Please enter your age"))

#If condition to check if eligible to vote:
if(my_age > 18):
	#if condition is satisfied
	print("Hello {0}, you are eligible to vote.".format(my_name))

else:
	#When If condition not satisfied
	print("Oops {0}, please come back in {1} years.".format(my_name,18-my_age))


#Multiple Conditions:
#we use elif in Python for multiple condition check

age = int(input("Please enter your age"))

if (age>18 and age<=60):
	print("Have fun at work")
elif (age<18):
	print("Enjoy your holidays")
elif (age>60):
	print("Stay Healthy..!")

