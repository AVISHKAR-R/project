num=int(input('Enter the number:'))
for row in range(num,0,-1):
    for space in range(0,num-row):
        print(end=" ")
    print(row,end='') 
    for col in range(1,row):
        print(end="  ")
    if row!=1:print(row,end='')
    print()    
for row in range(1,num+1):
    for space in range(0,num-row):
        print(end=" ")
    print(row,end='') 
    for col in range(1,row):
        print(end="  ")
    if row!=1:print(row,end='')
    print()    