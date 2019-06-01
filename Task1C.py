a=[10,16,7,8,9,43]
ans=list()

q1=int(input("0 1: "))
q2=int(input("0 2: "))
q3=int(input("0 3: "))
q4=int(input("0 4: "))

for i in range (0,6):
    if (q1%a[i]==0 and q2%a[i]==0):
        
        ans.append(a[i])
        ans.append(int(q1/a[i]))
        ans.append(int(q2/a[i]))
        ans.append(int(q3/a[i]))
        ans.append(int(q4/a[i]))


for i in range (0,6):
    if a[i] not in ans:
        ans.append(a[i])
        break
        

print("The order is: ",ans)
