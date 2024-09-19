# wap that takes two values from user and returns divison of first from second.
def do_divison():
    num1 = input("Enter num1: ")
    num2 = input("Enter num2: ")
    # converting these number into float.
    num1 = float(num1)
    num2 = float(num2)
    return num1 / num2

divison_of_two_numbers = do_divison()
print(divison_of_two_numbers)