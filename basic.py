print("Hello world") # print function prints the string that is inside "" or ''

x = 5 # 5 is assigned to x, no need to explicitly define data type as python is dynamically typed
print(x)
print("id of x ", id(x))
x = 20
print("id of x after changing its value ", id(x)) # change in memory address that means a new object is created this is because int type in python is immutable that means its value can't be changed after intialization.   int, float, str, google 

# why memory addresses are so close even when different objects are created ? check it 

# mutable object which can be changed  example: dict, list, etc
obj1 = [1,2,3]
print('id of obj1: ', id(obj1))
obj1.append(4)
print('id of obj1 after appending ', id(obj1))

if 'kuchbhi':  # same concept of truthy values like in js
    print('BINDASSSS CHLUNGA') 

str = 'aailajaadu'
print(str)
str =   str.replace('aaila','hey')
print(str)

str = str * 3 # prints string three times
# str = str - 3  this throws error
str = str + 'kya haal hai' # concate the strings with + operator
print(str)

print ("jaadu" in str ) # in and not in helps us if given sustring matches the other string this is case sensitive

# slice operator []
print(str[0:5]) # 5 is not included 0 is.

# use of escape character 
print("tarun \"kukreti\"")

# r"" this is a raw string literal suppose you want to save some file path as a string so using backlash inside "" will be treated as escape sequence in python to avoid that we use this
file_path = r"c:users/hp/downloads"
print(file_path)

# string formatting
name = "tarun"
age = 20
print("My name is %s and I am %d years old" %(name,age))
print("my name is {} and i am {} years old".format(name,age))

# using f strings
print(f"My name is {name} and i am {age} years old")

len_of_file_path = len(file_path)
print(len_of_file_path)











