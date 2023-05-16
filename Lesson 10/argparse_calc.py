import argparse

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y


# if __name__ == '__main__' indicates the entry point to the program when run directly by the Python interpreter.
# The code inside the if statement is not executed when the file's code is imported as a module.
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=float)
    parser.add_argument("y", type=float)
    
    # Optional argument with (bool with default False if not provided)
    parser.add_argument("-s", "--subtract", action="store_true") # Flip logic using "store_false"; will default to true 
    
    args = parser.parse_args()
    
    # Manual typecasting, if type not specified when adding args to parser
    # x, y = int(args.x), int(args.y)

    if args.subtract:
        print(subtraction(args.x, args.y)) 
    else:
        print(addition(args.x, args.y))
    
    quit()
    