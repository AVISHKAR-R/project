#import cmath
nums=int(input('enter the number'))
count=0
for num in range(1,nums+1):
    check=2
    sqro=num**0.5
    sqr=int(sqro)
    while check<=sqr:
        if num%check==0:
            break
        check+=1
    if check>sqr:
         print(num,end=" ")
         count+=1        
print('\ncount=',count)         
    # else:
    #     print('It is not a prime')       
    