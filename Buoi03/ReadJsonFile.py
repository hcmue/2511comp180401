# Đọc file student_data.json
import json
with open("student_data.json", "r", encoding="utf8") as mf:
    data = json.load(mf)
    # print(data)
    for item in data:
        item["gpa"] = item["gk"]*0.4+item["ck"]*0.6    
    print(json.dumps(data, indent=2))
    GPA = sum([item["gpa"]*item["sotc"] for item in data]) \
        / sum([item["sotc"] for item in data])
    print(GPA)