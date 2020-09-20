def function():
    i=1
    while i<100:
        if i%3==0:
            print("nav")
        elif i%5==0:
            print("gurukul")
        else:
            print("navgurukul")
        i=i+1
num=int(input("enter any num:"))
function()