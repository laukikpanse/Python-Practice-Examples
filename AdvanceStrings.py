#Laukik Narendra Panse

#declaring a variable with string
flag_name = "Indian flag"

#printing string normally
print(flag_name)

#String Slicing

#printing from 0th to 4th character
print(flag_name[:5]) #Output: India

#printing something in a range
print(flag_name[3:8]) #Output: ian f

#printing in reverse
print(flag_name[::-1])

#printing with a gap of 1
print(flag_name[0:12:2])

numbers = "1,2,3,4,5,6,7,8,9,0"
print(numbers)

#skipping every next character to avoid commas
print(numbers[0::2])

#no need to use + to concatinate direct strings
print("Hello ""how are you ""?") #useless

#multiplying strings
print("Hello "*5)

#checking if string is substring
day = "Today is Wednesday"
print("Friday" in day) #Output = False
print("Wednesday" in day)#Output = True

