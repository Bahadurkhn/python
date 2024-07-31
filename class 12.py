# String Method?
# Center():
# A center method aligns the string to the center as per the user gives the parameter.
a = "welcome to pakistan,welcome to Karachi"
print(len(a))
print(len(a.center(40)))
# output:
# len of string is 19,total len=40
print(a.count("welcome"))
# the count method the return number of values in a strings

# endswith():
str1 ="welcome to ends methods"
print(str1.endswith("methods"))

# this checks if the string endswith given value.
# if yes then return true else fasle
str1 ="welcome to ends methods"
print(str1.endswith("to",4,10))
# we can also even check the value in between of the string like:
str2 ="He's is a good boy.he is very innocent.he is a very good prorgammer"
print(str2.find("very"))
# findmethod():
# It search for a first occurence value of a sring and give the index of the value where
# it's present.else it's return -1
str3 ="He's is a good boy.he is very innocent."
# print(str3.index("the"))
# index is use for exception if value not found give error.
str3 ="HeIsAGoodBoy"
print(str3.isalnum())
# isalnum only return true if the entire string only consist of A-Z,a-z or 0-9
str4 ="128765346776125616575"
print(str4.isalnum())
# isalpha
str5 ="Welcome00"
print(str5.isalpha())

str6 ="Welcome"
print(str6.isalpha())
# isalpha only return true if the entire string only consist of A-Z,a-z
# else false
str6 ="Welcome"
print(str6.swapcase())
# swapcase:
# it return uppercase to lower or lower case to upper

str7 ="He's is a good boy.he is very innocent."
print(str7.title())
# output:
# He'S Is A Good Boy.He Is Very Innocent. it make it tittle