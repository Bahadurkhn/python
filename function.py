def CalculateGmean(a, b):
 mean = (a*b)/(a+b)
 print(mean)

a = 8
b = 6
c = 6
d = 9
# e = 7  
def ISlower(a, b):
 if(a<b):
    print("The first number is lasser/lower")
 else:
    print("The second number is greater or equal")
ISlower(a, b)

CalculateGmean(a, b)

def ISGreater(c, d):
 if(c<d):
    print("The first number is lasser/lower")
 else:
    print("The second number is greater or equal")
ISGreater(c, d)
CalculateGmean(c, d)
# CalculateGmean(a, e )