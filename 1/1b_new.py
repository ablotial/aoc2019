import pytest

def getfuel( mass ):
    """crappy recursive function to calculate amonut of fuel needed"""
    #print mass
    if( mass // 3 <= 2 ):
        return 0
    else:
        temp = (mass // 3) - 2
        return temp + getfuel( (mass // 3) - 2 )


def test_mass14():
    returnvalue = getfuel(14)
    assert returnvalue == 2

def test_mass1969():
    returnvalue = getfuel(1969)
    assert returnvalue == 966 

def test_mass100756():
    returnvalue = getfuel(100756)
    assert returnvalue == 50346
