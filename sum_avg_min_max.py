
def find_sum(*args):
    add = sum(args)
    average = add / len(args)
    max_val = max(args)
    min_val = min(args)

    print(f"from the given inputs sum is: {add}, average is: {average}, max value is: {max_val} and min value is {min_val}")


num1 = int(input("Enter num1: "))
num2 = int(input("Enter num1: "))
num3 = int(input("Enter num1: "))



find_sum(num1,num2,num3)



