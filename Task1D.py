n,r,x,y=input("Enter No of days,initial rating,x and y: ").split()
c=[int(c) for c in input("Enter if contest takes place: ").split()]
s=[int(s) for s in input("Enter if he eats SCN: ").split()]
rfinal=int(r)
for i in range (0,int(n)):
    if (c[i]==1):
        if s[i]==1:
            rfinal=rfinal+int(x)
        elif s[i]==0:
            rfinal=rfinal-int(y)
if rfinal>int(r):
    print ("Promoted")
elif rfinal<int(r):
    print ("Demoted")
else:
    print ("No change")



