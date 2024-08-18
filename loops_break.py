# Break used to terminate  the loop when encounter?

# i = 1
# while( i <= 5):
#     print(i)
#     i += 1
# Simple loop
# j = 1
# while( j <= 5):
#      print(j) 
#      if j== 3:
#         break
#      j +=1
# print("loop is ended")

# q5:find the number of x in tuple:

# n = int(input("Enter the number to find: "))
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# i = 0

# while i < len(nums):
#     if nums[i] == n:
#         print("Found at index", i)
#         break  # Exit loop once the number is found
#     i += 1
# else:
#  print("Number doesn't exit")

#  continue: Terminate execution in the current iteration.
# and continue the execution of the loop.

# i = 0
# while( i <= 5):
#      if i == 3:
#        i += 1
#        continue
#      print(i) #skip iteration
#      i += 1
# practice Question
# Q1:print the number from one to 10.
# and skip even number we need only odd number.

# i = 0
# while(i <= 10):
#     if(i %2 == 0): #reminder =0.
#         i +=1
#         continue
#     print(i) 
#     i += 1

    # Q2:print the number from one to 10.
# and skip odd number we need only even number.

i = 0
while(i <= 10):
    if(i %2 != 0): #reminder =0.
        i +=1
        continue
    print(i) 
    i += 1
        

   