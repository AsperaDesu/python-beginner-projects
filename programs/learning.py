print("Translation from a Vowel To the Letter 'G'")

def translate(phrase):
    translation = ""
    for letters in phrase:
        if letters.lower() in "aiueo":
            translation = translation + "g"
        else:
            translation = translation + letters
    return translation

print(translate(input("Enter a Phrase: ")))