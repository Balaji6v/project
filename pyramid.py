num = 1
# i is range in 1 to 21 beg,end
for i in range(1, 21):
#j is rows is added in one by one
    for j in range(i): #is
#if greater than 20 is break the loop
        if num > 20:
            break
# print in same line and row to added +1
        print(num, end=" ")
        num += 1
    print()
# Newline after each row
    if num > 20:
        break
