from itertools import permutations
my_string = 1991
new_string = str(my_string)
l = list(permutations(new_string))

count = 1
for char in l:
	print(count)
	print(char)
	count+= 1