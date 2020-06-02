T=int(input())
for i in range(T):
    amount=list(map(int,input().split()))
    n=int(input())
    res=0
    for par in range(n):
        green=purple=0
        status=list(map(int,input().split()))
        if status[0]==1:
            green=amount[0]
        if status[1]==1:
            purple=amount[1]
        res+=green+purple    
    print(res)    