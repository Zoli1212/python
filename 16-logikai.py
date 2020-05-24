def logikai(a):
    if a%2==0 and a%3==0:
        return True
    else:
        return False

if(logikai(7)):
    print("osztható")
else:
    print("nem osztható")
