# myfile = open("info.teo", "w", encoding="utf8")
# hoten = input("Họ tên của bạn: ")
# myfile.write(f"Họ tên: {hoten}\n")
# tuoi = int(input("Bao nhiêu tuổi: "))
# myfile.write(f"{tuoi} tuổi")
# myfile.close

with open("info.txt", "w", encoding="utf8") as myfile:
    hoten = input("Họ tên của bạn: ")
    myfile.write(f"Họ tên: {hoten}\n")
    tuoi = int(input("Bao nhiêu tuổi: "))
    myfile.write(f"Tuổi: {tuoi}")