postal_code = 12323

my_list = list(str(postal_code))

count = 0
for i in range(0,len(my_list)-2):
	if(i > len(my_list)):
		break

	else:
		if (my_list[i] == my_list[i+2]):
			count = count+1
			break

		else:
			print("This is a valid postal code")
			break
	if (count>1):
		print("Sorry, Not a valid postal code")
