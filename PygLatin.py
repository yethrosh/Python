print("PygLatin")

pyg = "ay"
asli = input("Enter any word: ")
if len(asli) > 0  and asli.isalpha():
    word = asli.lower()
    first = word[0]
    new_word = word[1:]
    new_word = new_word + first + pyg
    print(new_word)
else:
    print(u"آپ نے کوئي لفظ درج نہيں کيا ہے۔")
