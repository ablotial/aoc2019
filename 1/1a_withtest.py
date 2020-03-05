import pytest
import sys
import argparse

def getfuel( mass ):
   return (mass // 3) - 2

def totalfuel( masses ):
    total = 0
    for mass in masses:
       total = total + getfuel( mass )
    return total

def getargs():
   parser = argparse.ArgumentParser();
   parser.add_argument("filename")
   args = parser.parse_args();
   return args

def getdata( args ):
   filename = args.filename
   data = open(filename,"r")
   l = []
   for line in data:
       l.append( int(line) )
   return l

data = getdata( getargs() )
print("the total fuel required is {}".format( totalfuel( data ) ) )


def test_mass12():
    returnvalue = getfuel(12)
    assert returnvalue == 2

def test_mass14():
    returnvalue = getfuel(14)
    assert returnvalue == 2

def test_mass1969():
    returnvalue = getfuel(1969)
    assert returnvalue == 654

def test_mass100756():
    returnvalue = getfuel(100756)
    assert returnvalue == 33583

def test_sumis34241():
    testmasses = [12,14,1969,100756]
    returnvalue = total( testmasses )
    assert returnvalue == 34241
