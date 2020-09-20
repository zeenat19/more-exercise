
def function(password):
    length=len(password)
    for i in password:
        if length>=6 or length<=12 and "$" in password and 2 in password and "z" in password:
            return(password,"strong password")
        else:
            print(password,"week password")
password=input("enter your password:")
function(password)