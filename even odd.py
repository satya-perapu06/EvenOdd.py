num=int(input())
ec=0
oc=0
while num!=0:
    r=num%10
    num=num//10
    if num%2==0:
        ec+=1
    else:
        oc+=1    
print(ec)
print(oc)
if ec%2==0 and oc%2==0:
    print("even")
elif ec%2==0 and oc%2!=0:
    print("even odd")
elif ec%2!=0 and oc%2!=0:
    print("odd")
else:
    print("mixed")


    


