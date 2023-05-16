import argparse

# 'parser' manages the attributes; allows us to define attributes and reads/assignes/converts etc as defined
parser = argparse.ArgumentParser()

# Add expected arguments
# Positional
parser.add_argument("echo", help="The string you want printed (echoed)") # prints help when used with -h (--help)
parser.add_argument("numb", type=int) # Set type explicitly, will fail if not correct type provided via CLA
# Optional
parser.add_argument("-opr", "--optional_required") # Optional argument, fails if passed in without trailing arg, default to None if not passed in
parser.add_argument("-opd", "--optional_default", action="store_true") # Optional argument, defaults to False if not provided

# Get arguments passed in as CLAs
args = parser.parse_args()

# Handle unknown args
# args, unknown = parser.parse_known_args()

# Reference arguments using names provided when added
print(f"""echo:{args.echo}
numb:{args.numb}
--optional-required:{args.optional_required}
--optional_default:{args.optional_default}""")