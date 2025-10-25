#===============================
#zad. 5
plik = open("notowania_gieldowe.txt", "a")
plik.write("\n ALR, 113")
plik = open("notowania_gieldowe.txt", "r")
print(plik.read())