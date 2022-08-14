mevalar = ("olma","anor","banan")

# print(len(mevalar))
# meva_nomi = input("Meva nomini kiriting: ")

# if meva_nomi in mevalar:
#     print(meva_nomi,"ro'yxatda mavjud")
# else:
#     print(meva_nomi,"ro'yxatda mavjud emas")

mevalar_listi = list(mevalar)

mevalar_listi.append("tarvuz")

mevalar_tuple = tuple(mevalar_listi)
print(mevalar_tuple)