a = int(input("A? "))
b = int(input("B? "))
c = int(input("C? "))

if a == b == c:
    ket = "Tidak Ada"
else:
    if a == b:
        if a > c:
            ket = "A dan B"
        else:
            ket = "C"
    else:
        if a == c:
            if a > b:
                ket = "A dan C"
            else:
                ket = "B"
        else:
            if b == c:
                if b > a:
                    ket = "B dan C"
                else:
                    ket = "A"
            else:
                if a > b:
                    if a > c:
                        ket = "A"
                    else:
                        ket = "C"
                else:
                    if b > c:
                        if b > a:
                            ket = "B"
                    else:
                        if c > b:
                            if c > a:
                                ket = "C"


print(f"Terbesar = {ket}")

