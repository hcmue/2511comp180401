import requests

# res = requests.get("https://dummyjson.com/recipes")
# print(res)
# if res.status_code == 200:
#     print("Lấy dữ liệu thành công")
#     print(res.json())

res = requests.get("https://hcmue.edu.vn")
if res.status_code == 200:
    print("Lấy dữ liệu thành công")
    print(res.text)