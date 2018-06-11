#find pair of numbers whose sum end up with a given sum

numbers = [2,4,1,5,7,9,4,6,0,2]

sum_required = 10

new_list = numbers

print(new_list)

for num in numbers:
	if abs(num - sum_required) in new_list:
		print("The pairs are: {0} and {1}".format(num,abs(num-sum_required)))
