# wap to estimate runtime of all the funcions you have used so far.
from listEmailWithSapIds import generate_email_list;
from functionScope import add;
from functionScope import sub;
from avgOfThreeNums import avg;
from organizeFiles import create_dir_structure;
from functionsAndArgs import doSomeOperations;
import time as t

sapid = "570018097,570018114,570011111,570011112"
sapid = sapid.strip().replace("'","").replace('"',"").split(",")

def time_took_to_run_functions(fn, *args, **kwargs):
    start_time = t.time() # start the time.
    res = fn(*args,**kwargs)     # calling function with *, it unpacks a list or tuple into positional arguments.   if a tuple looks like this tup = (3,4)  *tup will give us 3 4
    end_time = t.time() # end the time.
    execution_time = end_time - start_time
    print(f"Execution time: of {fn} {execution_time * 1000000 } microseconds")
    return res

# creating a dictionary to store all functions and its args as key value pairs
function_dict = {
    add: (3,4),
    sub: (4,3),
    generate_email_list: sapid,
    avg: (1,2,3),
    create_dir_structure: "/home/tarun/pythonClasses",
    doSomeOperations: (35,4,44),
}


# iterate over the dictionary and call each function.
for fn, args in function_dict.items():
    if isinstance(args, tuple):
        res = time_took_to_run_functions(fn, *args)
    else:
        res = time_took_to_run_functions(fn,args)
    
    print(f"Result of {fn}: {res}\n")




# modify all your previous functions to print their execution time.

# create a presentation and explain usage of passing functions as arguments to modify function using wrapper functions for those who are not able to code.



