n=int(input("Enter length of the string: "))
if (n<=(10**6)) and (n in [2**i for i in range(0,20)]):
    s=(input("Enter String: "))
    count=0
    while (n!=0):
        if (n>1):
            if s[:int(n/2)]==s[int(n/2): ]:
                count=count+1
            s=s[0:int(n/2)]
            n=len(s)       
            continue
        elif (n==1):
            count=count
        print ("Degree of symmetry: ",count)
        break

    
    
