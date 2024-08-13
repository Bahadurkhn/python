# While loop?

 
# count = 0
# while count < 5:
#     print(count)
#     count += 1

count = 1
while count <= 10:
    if count == 6:
        break  # Exit the loop when count is 6
    if count % 2 == 0:
        count += 1
        continue  # Skip the rest of the loop for even numbers
    print(count)
    count += 1
