# ===============================
# zad. 7
Hasło = "pk47!jy0893"
x = len(Hasło)

z = (
    Hasło[0:1] == "!" or
    Hasło[1:2] == "!" or
    Hasło[2:3] == "!" or
    Hasło[3:4] == "!" or
    Hasło[4:5] == "!" or
    Hasło[5:6] == "!" or
    Hasło[6:7] == "!" or
    Hasło[7:8] == "!" or
    Hasło[8:9] == "!" or
    Hasło[9:10] == "!" or
    Hasło[10:11] == "!"
)

if x == 11 and z:
    print("Hasło jest poprawne")
else:
    print("Hasło jest niepoprawne")