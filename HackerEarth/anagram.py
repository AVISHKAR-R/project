# t=int(input())
# for i in range(t):
#     a=input()
#     b=input()
#     count=0
#     leng=len(a)+len(b)
#     for cha in sorted(a):
#         for chb in sorted(b):
#             if cha==chb:
#                 count+=1
#     print(leng-(2*count))           
                 
t=int(input())
for i in range(t):
    a=input()
    b=input()
    leng=len(a)+len(b)
    count=res=0
    comp=set(a).intersection(set(b))
    for check in comp:
        count=count+min(a.count(),b.count())
    res=leng-(count*2)
    print(res)  