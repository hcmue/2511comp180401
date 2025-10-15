from jinja2 import Environment, FileSystemLoader
# Khai báo thư mục chứa template

env = Environment(loader=FileSystemLoader("")) # Thư mục chứa template
# Load template
template = env.get_template("template.txt")

# Data sample
ho_ten = "Khoa CNTT"
phone = "0909123456"
danh_sach = [
    { "ten": "7up", "soluong": 7 },
    { "ten": "Bánh mì", "soluong": 17 },
]

result = template.render(ho_ten=ho_ten, phone=phone, danh_sach=danh_sach)
print(result)
# Save file html