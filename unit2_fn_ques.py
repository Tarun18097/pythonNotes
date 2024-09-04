
# write a function that takes one user arg as list and returns another list with cumulative sum in every iteration.

def cumulative_sum(l):
    ln = len(l)
    sum=0
    p = list()
    
    for i in range(0,ln):
        sum+=l[i] # sum = sum + len[i]
        p.append(sum)

    return p

    
l = [1,2,3,4,4]
p = cumulative_sum(l)
print(cumulative_sum(l))

# write a program to take n inputs from user and store them as a list
def make_list():
    n = int(input("enter a number"))
    numbers_list = list()
    for i in range(0,n):
        numbers_list.append(input("enter a number: "))

    return numbers_list
print(make_list())
# print(numbers_list)

    

    
