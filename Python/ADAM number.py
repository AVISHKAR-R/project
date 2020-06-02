nums=int(input('Enter the Number:'))
for num in range(nums):
    copy=num
    revnum=numsq=0
    numsq=num*num
    while num!=0:
        mod=num%10
        revnum=(revnum*10)+mod
        num=num/10
        num=int(num)
    revnumsq=revnum*revnum 
    mod=0 
    revnumrev=0
    while revnumsq!=0:
        mod=revnumsq%10
        revnumrev=(revnumrev*10)+mod
        revnumsq/=10
        revnumsq=int(revnumsq)
    if revnumrev==numsq:
        print(copy,end="  ")
    #     print('It is Adam number')
    # else:
    # print("Enter the valid number")
    
