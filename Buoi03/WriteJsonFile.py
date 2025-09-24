# Ghi file json
import json
data = [
    {
        "maMon": "comp1804", "tenmon": "Lập trình Python",
        "sotc": 3, "gk" : 8, "ck": 9
    },
    {
        "maMon": "comp1802", "tenmon": "Thiết kế Web",
        "sotc": 2, "gk" : 8, "ck": 7
    }
]
with open("student_data.json", "w", encoding="utf8") as mf:
    json.dump(data, mf, indent=4)