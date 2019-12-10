import sys
import argparse

def get_fuel( mass ):
    """crappy recursive function to calculate amonut of fuel needed"""
    print mass
    if( mass // 3 <= 2 ):
        return 0 
    else:
        temp = (mass // 3) - 2
        return temp + get_fuel( (mass // 3) - 2 )

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

filename = args.filename
data = open(filename,"r")

total = 0
for line in data:
    var = get_fuel(int(line))
    print var
    print 'next'
    total = total + var
print("the total fuel required is {}".format(total))

