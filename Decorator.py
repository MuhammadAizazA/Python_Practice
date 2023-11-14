def decorator_function(recived_func):
    def wrapper_function(*args,**kwarg):
        print("----------------------------------------------")
        returning_func=recived_func(*args,**kwarg)
        print("----------------------------------------------")
        return returning_func
    
    return wrapper_function

@decorator_function
def say_whee(num1,num2):
    print(num1+num2)
    
say_whee(1,4)
