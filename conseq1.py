list1 = [1,2,3,4,5,6,6,6,7,8,9]


pointer1 = 0
pointer2 = 1
while pointer2 == len(list1):
	if list1[pointer1] == list1[pointer2]:
		print(list1[pointer2])
	pointer2 += 1
	pointer1 += 1


