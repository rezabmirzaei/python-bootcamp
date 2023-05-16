import sys

print(f"## sys.argv demo")

## Access arguments passed to script using 'sys.argv'
print(f"sys.argv is of type {type(sys.argv)}") # A list
print(f"Number of arguments: {len(sys.argv)}") # Can be treated as a list, call any func/method available for lists
print(f"Arguments: {sys.argv}") # Includes script name as first argument
print(f"Arguments (-first one): {sys.argv[1:]}") # Exclude first argument