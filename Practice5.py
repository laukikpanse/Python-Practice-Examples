'''Write a Python program which accepts a sequence of 
comma-separated numbers from user 
and generate a list and a tuple with those numbers'''

numbers = input("Please Enter comma-separated numbers: ")

my_list = list(numbers.split(','))
my_tuple = tuple(numbers.split(','))

print(my_list)
print(my_tuple)