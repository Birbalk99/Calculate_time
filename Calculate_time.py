from functools import wraps
import time
def Calculate_Time(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f'Executing.....{function.__name__}')
        T1 =time.time()
        returned_value = function(*args,**kwargs)
        T2 = time.time()
        Total_Time = T2-T1
        print(f'This function took{Total_Time} Second')
        return returned_value
    return wrapper
@Calculate_Time
def square_finder(n):
    return[i**2 for i in range(1,n+1)]

square_finder(1000)
