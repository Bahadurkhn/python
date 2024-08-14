# Loops are used to repeat instruction.
# types: while loop,for loops:

# while loop:
# q1:Print number from 1 to 100
# a = 1
# while(a<=100):
#     print(a)
#     a +=1

# q2:Print number from 100 to 1

# a = 100
# while(a>=1):
#     print(a)
#     a -=1

# q3:print the multiple  table  of a number n

# n = int(input("Enter the number of multiplication table: "))
# i = 1
# while(i<=10):
#   print(i*n)
#   i +=1

# q3:print the element of the following list:
# list =[1,4,9,16,25,36,49,64,81,100]
# nums =[1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx <= len(nums):
#     print(nums[idx])
#     idx +=1

# # q4:
# colors =["red","green","yellow","blue"]
# idx1 = 0
# while idx1 <= len(colors):
#     print(colors[idx1])
#     idx1 += 1

# q5:find the number of x in tuple:
n = int(input("Enter the number to find: "))
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

i = 0
found = False  # Flag to track if the number was found

while i < len(nums):
    if nums[i] == n:
        print("Found at index", i)
        found = True
        break  # Exit loop once the number is found
    i += 1

if not found:
    print("Number not found in the tuple.")







