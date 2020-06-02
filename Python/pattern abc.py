num=int(input('enter the number:'))
ch=65
for row in range(1,num+1):
    for space in range(1,(num+1)-row):
        print(end=' ')
    for col in range(1,row+1):  
        print(chr(ch),end=" ") 
        ch+=1
        if ch>90:
            ch=65
    print("")     