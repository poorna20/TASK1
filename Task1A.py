
l=int(input("Enter length of string: "))
x=(input("Enter string: "))
while (l<=105):
    y=int(x,2)
    left=y-1
    right=y+1
    while ((len(format(left,"b"))==l)):
        while ((len(format(right,"b"))==l)):
            if (((left+right)/2)==y):
                print ("Output: ",(format(left,"b")),(format(right,"b")))
                break
            else:
                print ("-1")
            right=right+1
            break
        left=left-1
        break
    else:
        print ("-1")
    break

    

else:
    print ("-1")
