a = int(input("Add meg az első számot"))
b = int(input("Add meg a második számot!"))
c = int(input("Add meg a harmadik számot"))

if a<b and a <c:
    print(a)
elif b<a and b<c:
    print(b)
elif c<a and c <b:
    print(c)
else:
    print(" egyenlő van a számok között ")