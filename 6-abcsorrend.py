import locale

szo1 = input("Add meg az első szavad: ")
szo2 = input("Add meg a második szavad: ")
locale.setlocale(locale.LC_ALL, "HU_hu.UTF8")

k = locale.strcoll(szo1, szo2)

if(k<0):
    print(szo1+" "+szo2)
else:
    print(szo2+" "+szo1)