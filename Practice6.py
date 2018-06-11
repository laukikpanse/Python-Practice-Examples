'''Write a Python program to accept a filename 
from the user and print the extension of that.'''


file_name = "Mrrobot.python"
my_list = list(file_name.split('.'))
print("The extension of your file is: "+my_list[-1])

