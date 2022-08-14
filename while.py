word = input("Tilni kiriting (UZ/EN): ")

while True:
    if word.isalpha():
        if word.lower() == 'uz':
            print("Assalomu aleykum")
        elif word.lower() == 'en':
            print("Hello")
        break
    elif word.isdigit():
        print("Son kiritish mumkin emas")
        word = input("Tilni kiriting (UZ/EN): ")
    else:
        word = input("Tilni kiriting (UZ/EN): ")