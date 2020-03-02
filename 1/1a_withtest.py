import pytest

def getfuel( mass ):
   return (mass // 3) - 2

def total( masses ):
    total = 0
    for mass in masses:
       total = total + getfuel( mass )
    return total

def test_mass12yield2():
    returnvalue = getfuel(12)
    assert returnvalue == 2

def test_mass14yield2():
    returnvalue = getfuel(14)
    assert returnvalue == 2

def test_mass1969yield654():
    returnvalue = getfuel(1969)
    assert returnvalue == 654

def test_mass100756yield33583():
    returnvalue = getfuel(100756)
    assert returnvalue == 33583

def test_sumis34241():
    testmasses = [12,14,1969,100756]
    returnvalue = total( testmasses )
    assert returnvalue == 34241
