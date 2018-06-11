#Laukik Narendra Panse

age = 27 #declaring an integer

#concatinating string and Integer using str()
print("My age is: "+str(age))

#Replacement fields using .format
#useful when lot of data
print("My age is: {0}".format(age))


#use Triple quotes to write single code on multiple lines
print('''The days in a week are: 
	{0}, 
	{1}, 
	{2}, 
	{3}, 
	{4}, 
	{5}, 
	{6}'''
	.format("Monday",
		"Tuesday","Wednesday",
		"Thursday","Friday","Saturday","Sunday"))

#Old method of string formating
print("My age is: %d" %age)

print("My age is %d %s %s" %(age," 1 month", "10 days"))

#using string formating in For Loop

for i in range(0,20):
	print("The current number is {0}".format(i))


