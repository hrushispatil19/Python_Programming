#10 Exception Handling

try:
    x=-5
    print(x)
    if (x<0):
        raise Exception("No Zero Value should allowed")
   
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
else:
    print("Nothing went wrong")
    
"""
Output:
-5
Something else went wrong
"""
