# Matchcase in python

# A matchcase is compare a given varible value of different shapes.
# also refereds to as pattern. the main idea is to keep op
# comparing the varible with all the present until it fits into one.

# x = int(input("Enter the number :"))
 
# match x:
#     case 0:
#         print("x is zero")
    
#     case 4:
#         print(x,"is four")
#     case _ if x!=90:
#         print(x," is 90 ")
#     case _ if x!=80:
#         print(x,"x is 80 ")
#     case _:
#         print(x)

y=int(input("Enter your number:"))
match y:
    case 1 | 2 | 3:
            print("Number is either 1, 2, or 3")
    case 4 | 5 | 6:
            print("Number is either 4, 5, or 6")
    case _:
            print("Number is something else")

# Test cases
# Output: Number is either 1, 2, or 3
# Output: Number is either 4, 5, or 6
# Output: Number is something else

# or operator in python
