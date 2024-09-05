
# write a function that takes one user arg as list and returns another list with cumulative sum in every iteration. 

def cumulative_sum(l):
    if((isinstance(l,list))):  # return true if l is a list
        size_of_list = len(l)
        sum=0
        sum_list = list()
        for i in range(size_of_list):
            sum += l[i]   # sum = sum + l[i]
            sum_list.append(sum)
    else:
        print("Entered parameter is not a list ")
        return -1

    return sum_list
   
l = [1,2,3,4,4]
print(f"Given list: {l}")
print(f"cumulaive sum after every step: {cumulative_sum(l)}")




    # write a program to take n inputs from user and store them as a list

def make_list():
    size_of_list = int(input("How many numbers you want to enter in the list: "))
    number_list = []
    for i in range(size_of_list):
        number_list.append(input(f"Enter number {i+1}: "))

    return number_list

user_entered_list = make_list()
print(f"This is your list: {user_entered_list}")

    # write a program that will not stop taking input till entered stop and store all the input as list.

def generate_list():
    num_list = list()
    print("This function is to generate a list where you don't know how many inputs you have to give, so after giving all the inputs enter 'stop' to stop giving the inputs.")
    i = 1
    while(True):
        user_input = input(f"Enter number {i}: ")
        if(user_input == "stop"):
            break
        num_list.append(int(user_input))
        i += 1
    return num_list


generated_list = generate_list()

print(f"This is your generated list: {generated_list}")


    

    