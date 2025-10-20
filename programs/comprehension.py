# A
ganjil = [i for i in range(1, 20) if i % 2 == 1]

print("10 Bilangan Ganjil Pertama =", end=" ")
print(*ganjil, sep=" ")


# B
genap = [i for i in range(5, 5 * 11, 5)]

print("10 Bilangan Kelipatan 5 Pertama", end=" ")
print(*genap, sep=" ")


# C
alphabets = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
consonants = [x.upper() for x in alphabets if x not in "aiueo"]

print("10 Konsonan Pertama =", end=" ")
print(*consonants[:10], sep=" ")


# D
print("10 Ganjil dan Genap =")
mixed = ["Genap" if x % 2 == 0 else "Ganjil" for x in range(1, 11)]

print(*[f'	{i+1} -> {mixed[i]}' for i in range(10)], sep = '\n')
