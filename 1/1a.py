import sys

filename = sys.argv[1]
data = open(filename,"r")

total = 0
for line in data:
    line = (int(line) // 3) - 2
    print line
    total = total + line
print("the total fuel required is {}".format(total))
