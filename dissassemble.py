with open("mario.bmp", "rb") as file:
    header = list(file.read(14))
    dib_size = int(list(file.read(1))[0])
    file.seek(file.tell() - 1)
    dib_header = list(file.read())


with open("mario.txt", "w") as file:
    for byte in header:
        file.write(f"{byte:02X} ")
    file.write("\n\n")

    temp = 1
    for _ in range(dib_size):
        file.write(f"{dib_header[_]:02X} ")
        if temp > 15:
            file.write("\n")
            temp = 0
        temp += 1
    
    file.write("\n\n")
