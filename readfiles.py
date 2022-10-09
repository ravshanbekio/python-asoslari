# Fayllarni o'qish

f = open("demofile.txt", "r")
print(f.read())
f.close()

# Faqatgina bitta qatordagi ma'lumotlarni o'qish
f = open("demofile.txt", "r")
print(f.readline())
f.close()

# Barcha qatordagi ma'lumotlarni list ichiga olib o'qish
f = open("demofile.txt", "r")
print(f.readlines())
f.close()



# Yangi fayl yaratib, unga ma'lumot yozish
f = open("demofile.txt", "w")
print(f.write(""))
f.close()


# Avvaldan mavjud faylga yangi ma'lumot qo'shish
f = open("demofile.txt", "a")
print(f.write(""))
f.close

