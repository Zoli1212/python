a = int(input("Adj meg egy egész számot!"))
b = int(input("Adj meg egy második egész számot!"))
c = int(input("Add meg a harmadik egész számot!"))
if a+b==c or b+c==a or a+c==b:
    print("Igen a két szám összege megegyezik a harmadikkal")
else:
    print("Nem egyeznek meg")