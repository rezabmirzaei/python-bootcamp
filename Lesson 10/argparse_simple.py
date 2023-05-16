import argparse

parser = argparse.ArgumentParser()

parser.add_argument("first_argument")
parser.add_argument("second_argument")

args = parser.parse_args()

print(f"first_argument:{args.first_argument}")
print(f"second_argument:{args.second_argument}")