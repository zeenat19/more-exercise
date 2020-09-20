num=int(input("enter any num:"))
store=num
i=1
sum=0
while num>0:
    a=num%store
    sum=sum+num
    a=store//num
    i=i+1
if store%num==0:
    print(num,"it is harashad num:")
else:
    print(num,"it is not harshad num:")
