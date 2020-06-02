num=int(input('Enter the 10 Digit number:'))
copy=num
digit=result=0
while num!=0:
    rem=num%10
    power=1
    for i in range(rem):
        power*=10
    calc=rem*power
    result+=calc
    num/=10
    num=int(num)
    digit+=1
if digit==10 and result==9876543210:
    print(result,"is Pandigital number")    
else:
    print(result,"is not Pandigital number")  

