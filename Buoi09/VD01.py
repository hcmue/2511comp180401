import matplotlib.pyplot as plt

diem = list(range(0, 11))
so_luong = [1, 1, 0, 0, 0, 0, 0, 34, 45, 12, 5]

plt.plot(diem, so_luong)
plt.xlabel("Điểm")
plt.ylabel("Số lượng SV")
plt.title("THỐNG KÊ ĐIỂM")

plt.show()