import argparse

parser = argparse.ArgumentParser()

parser.add_argument("my_arg")

args = parser.parse_args()

print(f"Hello from file! {args.my_arg}")