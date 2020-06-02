T=int(input())
lis=[]
ch=''
vowel=['a','e','i','o','u']
cons=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
for i in range(T):
    N=int(input())
    S=input()[:N]
    lis.append(S)
for word in lis:
    ch=word  
    sl=len(ch)-1
    count=0
    i=0
    while i<sl:
        if ch[i] in cons and ch[i+1] in vowel:
            count+=1
        i+=1
    print(count)        
