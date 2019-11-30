

'''
translator
Giraffe language
vowels -> g
---------------------
dog -> dgg
cat -> cgt
'''

# function
def translate(phrase):
    translation = ""
    for letter in phrase:
        # if letter == any letter in "AEIOUaeiou"
        if letter.lower() in "aeiou":
            if letter.islower():
                translation += "g"
            else:
                translation += "G"
        else:
            translation += letter

    return translation

print(translate("Qian"))
print(translate(input("Enter a phase: ")))