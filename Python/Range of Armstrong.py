nums=int(input('Enter the range:'))
for num in range(1,nums+1):
    copy=num
    mod=val=1
    result=power=0
    while num!=0:
        num=num/10
        power+=1
        num=int(num)
    num=copy
    while num!=0:
        mod=num%10
        num/=10
        for i in range(power):   
            val=val*mod
        result+=val
        num=int(num)
        val=1
    if copy==result:print(result,end=" ")  
