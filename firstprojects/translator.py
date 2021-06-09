def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeuio":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translator(input("Enter your phrase: ")))