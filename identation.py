if True:
    print("i am inside")

print("am outside")

name_in_system = "tarun"
user_name = input("Enter you name: ")
age_in_system = 21
user_age = int(input("Enter your age: "))

if(name_in_system == user_name and age_in_system == user_age):
    print("you are in")
elif(name_in_system == user_name or age_in_system == user_age):
    print("do manual authentication")
else:
    print("call the cops")



num = int(input("Enter a number: "))
i  = 1
while(i <= 10):
    if(i == 0):
        continue
    product = num * i
    if(product == 10):
        break
    print(f"{num} * {i} = {product}") # after break nothing on that block will run. 
    i += 1


choclates = ['kitkat', 'dairymilk', '5star']
for choclate in choclates:
    print(choclate)