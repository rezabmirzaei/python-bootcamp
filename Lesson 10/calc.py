import sys

def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y
                
if __name__ == '__main__':
    method, x, y, *etc = tuple(sys.argv[1:])
    if method not in ["addition","subtraction"]:
        print("Must have addition or subtraction as first argument")
        quit()
    else:        
        print(locals()[method](int(x), int(y)))
