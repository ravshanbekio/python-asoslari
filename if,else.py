lang = input("Tilni tanlang (UZ/ENG): ")

if "uz" in lang.lower():
    print("Assalomu aleykum!")
elif "eng" in lang.lower():
    print("Hello!")
else:
    print("Boshqa tilni tanladingiz!")