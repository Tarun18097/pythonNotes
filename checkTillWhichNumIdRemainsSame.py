i = 0
j = 0
while (id(i) == id(j)):
    print(i, j , id(i), id(j))
    i += 1
    j += 1
print(f"i is: {i} with id {id(i)} and j is: {j} with id {id(j)}")

# -5 to 256 integers are cached that means they are preallocated so whenever we create something with a value which lies b/w this range python doesn't create new objects rather uses this preallocated objects which are initialized when the python interpreter starts.
