import argparse

parser = argparse.ArgumentParser();
parser.add_argument("filename")
args = parser.parse_args();

filename = args.filename
data = open(filename,"r")

for line in data:
    values = line.split(',')
    location = 0

    while( int(values[location]) != 99 ):
        print values
        print "current location is: {}".format(location)
        if( int(values[location]) == 1 ): #add
            print "found add, adding {} + {}".format(values[int(values[location+1])], values[int(values[location+2])])
            values[int(values[location+3])] = int(values[int(values[location+1])]) + int(values[int(values[location+2])])
        elif( int(values[location]) == 2 ): #multiply
            print "multiplying {} * {}".format(values[int(values[location+1])], values[int(values[location+2])])
            values[int(values[location+3])] = int(values[int(values[location+1])]) * int(values[int(values[location+2])])
        else:
            print "Something went wrong..."
            break
    
        location = location + 4

    print values
