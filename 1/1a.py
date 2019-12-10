import sys
import argparse

parser = argparse.ArgumentParser();
parser.add_argument("filename")
args = parser.parse_args();

filename = args.filename
data = open(filename,"r")

total = 0
for line in data:
    line = (int(line) // 3) - 2
    print line
    total = total + line
print("the total fuel required is {}".format(total))
