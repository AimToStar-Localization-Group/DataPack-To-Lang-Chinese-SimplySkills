import json

with open("definitions.json", "r") as file:
    original_data = json.load(file)

extracted_data = {}
for key, value in original_data.items():
    if "description" in value:
        extracted_data[f"text.skills.{key}.title"] = value["title"]
        extracted_data[f"text.skills.{key}.description"] = value["description"]

with open("zh_cn.json", "w", encoding="utf-8") as f:
    json.dump(extracted_data, f, indent=4, ensure_ascii=False)
