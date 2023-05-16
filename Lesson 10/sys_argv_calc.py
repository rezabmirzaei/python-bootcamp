import sys

def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y


# if __name__ == '__main__' indicates the entry point to the program when run directly by the Python interpreter.
# The code inside the if statement is not executed when the file's code is imported as a module.
if __name__ == '__main__':
    
    method, x, y, *etc = tuple(sys.argv[1:])
    
    if method not in ["addition","subtraction"]:
        print("Must have addition or subtraction as first argument")
    else:        
        print(locals()[method](int(x), int(y)))

    quit()