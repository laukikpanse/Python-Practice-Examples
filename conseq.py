#find the numbers who repeat


list1 = [1,2,3,4,5,5,6,6,6,6,6,6,6,6,7,8,9,0]

dict1 = dict()
i=1
for char in list1:
	if char not in dict1:
		dict1[char] = i
	else:
		dict1[char] += 1
for char in dict1:
	if dict1[char] > 1:
		print("The additional characters are: "+str(char))
