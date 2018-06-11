#Program to print unique words in a string:


my_string = "hello hello hello how are you you mack hello mack hello how the end"

new_string = my_string.split()

list_1 = list(new_string)
list_2 = []



for i in range(0,len(list_1)):
	if list_1[i] in list_2:
		pass
	else:
		list_2.append(list_1[i])

print(' '.join(list_2))