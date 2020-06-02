def reverse(num):
    mod=revnum=0 
    while num!=0:
        mod=num%10
        revnum=(revnum*10)+mod
        num=num/10
        num=int(num)
    return revnum    
nums=int(input('Enter the Number:'))
for num in range(nums):
    copy=num
    revnumrev=0
    numsq=0
    numsq=num*num
    revnum=reverse(num)
    revnumsq=revnum*revnum 
    revnumrev=reverse(revnumsq)
    if revnumrev==numsq:print(copy,end="  ")
    # while revnumsq!=0:
    #     mod=revnumsq%10
    #     revnumrev=(revnumrev*10)+mod
    #     revnumsq/=10
    #     revnumsq=int(revnumsq)
   