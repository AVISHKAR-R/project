T=int(input())
anals=['a','e','i','o','u','A','E','I','O','U']
for i in range(T):
    count=0
    S=input()
    for i in range(len(S)):
        print(len(S))
        if S[i] in anals:
            count+=((len(S)-i)*(i+1))
print(count) 