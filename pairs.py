my_list = [1,2,3,3,4,4,5,8,8,4,5,6,7,8,0,6,3,3,1,1,1,2,4]

myset = set(my_list)
required_data = 6
print(myset)

for i in myset:
	result = required_data - i
	if(result in myset):
		print("The pair is: {0} {1}".format(result,i))

