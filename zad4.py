#===============================
#zad. 4
gol = int(input("Podaj liczbę strzelonych bramek:"))

pkt = gol * 10
if gol >= 5 and gol <= 10:
    bonus = 5
    pkt = pkt + bonus
    print(pkt)
elif gol > 10:
    bonus = 15
    pkt = pkt + bonus
    print(pkt)



