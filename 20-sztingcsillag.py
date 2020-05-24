def eljaras(a):
    for i in range(1, a+1):
        if i%3!=0:
            print("+", end= " ")
        else:
            print("-", end=" ")

a = int(input("Adj meg egy számot"))
eljaras(10)