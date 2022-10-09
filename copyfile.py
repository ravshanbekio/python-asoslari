import os

with open("test.txt",'w') as file:
    file.write("Test")
src = "test.txt"
dest = "D:\\test.txt"


if os.path.exists(dest):
    print("Fayl allaqachon shu yerda edi")
else:
    os.replace(src,dest)
    print(src+" Fayl moved")
