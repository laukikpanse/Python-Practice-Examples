#finding the minimum number in the list without using the min() function


numbers = [22,34,67,88,99,23,45,12,10,2,0]

min_num = numbers[0]

for i in range(0,len(numbers)):
	if numbers[i]<min_num:
		min_num = numbers[i]

print("The minimum number in the list is: {0}".format(min_num))