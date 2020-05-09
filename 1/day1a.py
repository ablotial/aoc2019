import aocutils

def getfuel( mass ):
   return (mass // 3) - 2

def totalfuel( masses ):
    total = 0
    for mass in masses:
       total = total + getfuel( mass )
    return total

def main():
    data = aocutils.getdata( aocutils.getargs() )
    print("the total fuel required is {}".format( totalfuel( data ) ) )

if __name__ == "__main__":
    main()
