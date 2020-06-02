S=input()
res=""
lens=len(S)
while(lens>0):
    rev=S[lens-1]
    lens-=1
    res=res+rev   
if S==res:
    print("YES")
else:
    print("NO")   