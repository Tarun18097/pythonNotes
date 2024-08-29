import sys
# basic data types in python int float complex etc
x = 10 # unlimited precision that means there is no fixed bit size for int in python it dynamically allocated more memory for representing big integers.

y = 2.2 # 15-17 digits of precision
z = 2 + 5j
print(type(x), type(y), type(z))
# boolean values 
k = True
l = False
print(k,l)

# type conversion 
# syntax <data_type> (value_to_be_converted)
# for eg. 
y = int(y)
print(type(y))


# to find the size of variable
a = 10
b = 10444444468996191981856186516515616516156458620468206802690238620682062060265962
size_of_a = sys.getsizeof(a)
size_of_b = sys.getsizeof(b)
print(f"size of a: {size_of_a} bytes")
print(f"size of b: {size_of_b} bytes") # 60 bytes. dynamically allocated memory to accomadate this large num

mem_location_of_a = id(a)
print(f"memory location of a is: {mem_location_of_a}")
