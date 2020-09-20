def function():
    value=student*spent
    print(value)
    if value<=50000:
        return("budget is under control")
    else:
        print("budget is out of control")
student=int(input("enter any num:"))
spent=int(input("enter any num:"))
function()

