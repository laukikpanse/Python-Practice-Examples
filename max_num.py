#finding max number from the list without using max() function


numbers = [2,4,5,6,89,93,24,79,0,99,196]

max_num = 0

for i in range(0,len(numbers)):
	if numbers[i] > max_num:
		max_num = numbers[i]
print(max_num)