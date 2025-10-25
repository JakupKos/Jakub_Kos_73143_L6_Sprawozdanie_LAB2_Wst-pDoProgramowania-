#===============================
#zad. 2
x = float(input("Podaj pierwszą liczbę:"))
y = float(input("Podaj drugą liczbę:"))
z = float(input("Podaj trzecią liczbę:"))

if x < y and x < z:
    print(x)
    if y < z:
        print(y)
        print(z)
    else:
        print(z)
        print(y)
elif y < z and y < x:
    print(y)
    if z < x:
        print(z)
        print(x)
    else:
        print(x)
        print(z)
elif z < y and z < x:
    print(z)
    if y < x:
        print(y)
        print(x)
    else:
        print(x)
        print(y)