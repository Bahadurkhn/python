# Matchcase in python

# A matchcase is compare a given varible value of different shapes.
# also refereds to as pattern. the main idea is to keep op
# comparing the varible with all the present until it fits into one.

x = int(input("Enter the number :"))
 
match x:
    case 0:
        print("x is zero")
    
    case 4:
        print(x,"is four")
    case _ if x!=90:
        print(x," is 90 ")
    case _ if x!=80:
        print(x,"x is 80 ")
    case _:
        print(x)

