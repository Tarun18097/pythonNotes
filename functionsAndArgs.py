'''
 syntax for function
 def functionName(args, args):


'''
# wrte a func that gives sum, avg, min, max of args
def doSomeOperations(*args):
    # print(type(args))
    my_sum = sum(args)
    my_avg = my_sum/len(args)
    my_min = min(args)
    my_max = max(args)

    print("sum is ",my_sum)
    print("my avg is ",my_avg)
    print("min is : " ,my_min)
    print("max is : " ,my_max)


num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

doSomeOperations(num1,num2,num3)

