num=int(input("Enter the number:"))
for row in range(1,num+1):
    for space in range(1,num-row+1):
        print(end=" ")
    for col in range(row):
             print("*",end=" ")    
    print("")    