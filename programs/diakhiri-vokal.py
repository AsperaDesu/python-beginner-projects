print("Apakah Kalimat Termasuk Huruf Vokal")
print("-"*35)

kalimat = input("Isikan sebuah kalimat? ")

if len(kalimat) % 2 == 0:
    if kalimat[-1].lower() in "aiueo":
        print(f"Kalimat diakhiri dengan huruf vokal '{kalimat[-1]}'")
    else:
        print("Kalimat tidak diakhiri dengan huruf vokal")
else:
    if kalimat[len(kalimat)//2].lower() in "aiueo":
        print(f"Huruf di tengah kalimat merupakan huruf vokal '{kalimat[len(kalimat)//2]}'")
    else:
        print("Huruf di tengah kalimat bukan merupakan huruf vokal")
