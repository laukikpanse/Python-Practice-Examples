#Creating lists:

list1 = ['Physics','Chemistry','Mathematics']
list2 = [1,2,3,4,5,6,7]

#printing elements at certain index
print("Before updating element at index 0 : {0}".format(list1[0]))
print(list2[2])


#Updating list is just replacement

list1[0] = 'Geometry'

print("After updating element at index 0: {0} ".format(list1[0]))



#deleting any element from list

del list2[2]
print (list2[2])

#finding the length of a list
print("The length of List 1 is: {0}".format(len(list1)))

#printing a string multiple times
print("Hello World " * 3)