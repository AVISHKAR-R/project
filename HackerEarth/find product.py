N=int(input())
res=1
li=list(map(int,input().split()))
print(li)  
for i in range(len(li)):
    res=(res*li[i])%(1000000007)
print(res)    





    