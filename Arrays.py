from array import *


#Declaring an array
my_array = array('i',[10,20,30,40,50])

#Printing all the characters in an array
print("Printing all elements in array: \n")

for nums in my_array:
	print(nums)

#Accessing a particular element in an array

print("The value at index 0: {0}".format(my_array[0])) #Values inside square brackets are Indexes
print("The value at index 1: {0}".format(my_array[1]))
print("The value at index 4: {0}".format(my_array[4]))


#inserting an element in the array
print("Array after inserting an elemnt in array")
my_array.insert(2,5)
for nums in my_array:
	print(nums)
#Note: Insetion does'nt replace but adds value

#Deleting an element from the array

my_array.remove(30)
print("Array after Deleting an elemnt in array")

for nums in my_array:
	print(nums)

#Printing the index of an element

print("The index of element 5 is: {0}".format(my_array.index(5)))

