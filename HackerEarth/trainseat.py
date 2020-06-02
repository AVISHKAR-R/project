
T=int(input())
N=[]
for i in range(T):
    seat=int(input())
    N.append(seat)
for i in range(len(N)):    
    if N[i]%12==1:print(N[i]+11,'WS')
    elif N[i]%12==2:print(N[i]+9,'MS')
    elif N[i]%12==3:print(N[i]+7,'AS')
    elif N[i]%12==4:print(N[i]+5,'AS')
    elif N[i]%12==5:print(N[i]+3,'MS')
    elif N[i]%12==6:print(N[i]+1,'WS')
    elif N[i]%12==7:print(N[i]-1,'WS')
    elif N[i]%12==8:print(N[i]-3,'MS')
    elif N[i]%12==9:print(N[i]-5,'AS')
    elif N[i]%12==10:print(N[i]-7,'AS')
    elif N[i]%12==11:print(N[i]-9,'MS')
    else:print(N[i]-11,'WS')