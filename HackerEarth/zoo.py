word=input()[:20]
zcount=word.count("z",0,5)
ocount=word.count("o")
odd=zcount*2
if odd==ocount:
    print("Yes")
else:
    print("NO")    