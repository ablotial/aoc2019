import argparse

parser = argparse.ArgumentParser();
parser.add_argument("filename")
args = parser.parse_args();

filename = args.filename
data = open(filename,"r")
line = data.readline()

for noun in range(100):
    for verb in range(100):
        print "noun {}, verb {}".format(noun, verb)
        values = line.split(',')
        location = 0
        values[1] = noun;
        values[2] = verb;
    
        while( int(values[location]) != 99 ):
            print values[0]
            print "current location is: {}".format(location)
            if( int(values[location]) == 1 ): #add
                values[int(values[location+3])] = int(values[int(values[location+1])]) + int(values[int(values[location+2])])
            elif( int(values[location]) == 2 ): #multiply
                values[int(values[location+3])] = int(values[int(values[location+1])]) * int(values[int(values[location+2])])
            else:
                print "Something went wrong..."
                break
        
            location = location + 4


        if( int(values[0]) == 19690720 ):
            print "I found the value for inputs {} and {}".format(noun, verb)
            break
    if( int(values[0]) == 19690720 ):
        print "I found the value for inputs {} and {}".format(noun, verb)
        break
