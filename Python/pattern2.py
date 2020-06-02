num=int(input('Enter the number:'))
for row in range(num):
    for col in range(row+1):
        print('1',end=" ")
    # for fill in range(2,(num+1)-row):
    #     print(fill,end=" ")      
    print()

