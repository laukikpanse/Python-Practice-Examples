#count the number of words in the string

my_string = "hello laukik how are you baby what hello laukik are you you you"
new_string = my_string.split()

my_dict = dict()


for char in new_string:
	if char in my_dict:
		my_dict[char] +=1   
	else:
		my_dict[char] = 1
print(my_dict)