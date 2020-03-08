import pytest
import sys

sys.path.append("/home/deana/projects/aoc2019/")

import aocutils

def getfuel( mass ):
   return (mass // 3) - 2

def totalfuel( masses ):
    total = 0
    for mass in masses:
       total = total + getfuel( mass )
    return total

data = aocutils.getdata( aocutils.getargs() )
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
    returnvalue = totalfuel( testmasses )
    assert returnvalue == 34241
