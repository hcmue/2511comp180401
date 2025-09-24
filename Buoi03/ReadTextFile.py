try:
    with open("info.sxt", "r", encoding="utf8") as myfile:
        for line in myfile:
            print(line[:-1])
except Exception as ex:
    print("Lỗi", ex)