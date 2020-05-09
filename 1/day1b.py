def getfuel( mass ):
    """crappy recursive function to calculate amonut of fuel needed"""
    #print mass
    if( mass // 3 <= 2 ):
        return 0
    else:
        temp = (mass // 3) - 2
        return temp + getfuel( (mass // 3) - 2 )
