try:
    son1 = int(input("1-sonni kiriting: "))
    son2 = int(input("2-sonni kiriting: "))

    natija = son1 // son2
    print(natija)

except ZeroDivisionError:
    print("Siz 0 qiymatini kirita olmaysiz")

except ValueError:
    print("Faqat son kiritish mumkin!")

else:
    print("Dasturda xatolik mavjud!")

finally:
    print("Dastur yakunlandi!")