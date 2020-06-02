num=int(input('Enter the number'))
for row in range(num+1):
    for col in range(num,row,-1):
        print(col,end=" ")
    print()    