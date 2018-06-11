#Linear Search algorithm without using sort() function

numbers = [1,2,5,6,8,9,0,12,11,19,14]



for i in range(0,len(numbers)-1):
	if numbers[i]>numbers[i+1]:
		temp = numbers[i]
		numbers[i] = numbers[i+1]
		numbers[i+1] = temp

print(numbers)