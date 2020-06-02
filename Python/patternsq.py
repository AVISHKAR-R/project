num=int(input('Enter the Number:'))
org=num
for row in range(0,num):
    for space in range(row):
            print(end="  ") 
    for col in range(1,num*2):
        print(num,end=" ")
    num-=1 
    print()
jump=0 
num=org          
for row in range(1,num+1):
    for space in range(row,num):
        print(end="  ")
    for col in range(jump+1):
        print(row,end=" ")
    jump+=2
    print()
