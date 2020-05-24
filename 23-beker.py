
lista = []

while True :
    a = int(input("Adj meg egy számot!"))
    if a==0 :
        break

    lista.append(a)
    
print(lista)
lista.reverse()
print(lista)