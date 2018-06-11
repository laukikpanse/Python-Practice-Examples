'''Write a Python program that accepts an integer (n) 
and computes the value of n+nn+nnn'''



number = (input("Please enter some number: "))

mynum = str(number)
my_sum = int((mynum+mynum*2+mynum*3))
print(sum(my_sum))


