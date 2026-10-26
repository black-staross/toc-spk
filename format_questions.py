import json
import re

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    q = item["question"]
    q_ko = item["questionTranslation"]

    # Format English question with natural line breaks:
    # 1. Choices in parenthesis (e.g., (Fast delivery / Cheap price / Customer reviews))
    if " (" in q and q.endswith(")"):
        parts = q.rsplit(" (", 1)
        base_q = parts[0]
        choices = "(" + parts[1]
        q_formatted = base_q + "\n" + choices
    elif "? Why" in q:
        q_formatted = q.replace("? Why", "?\nWhy")
    elif ", and " in q:
        q_formatted = q.replace(", and ", ",\nand ")
    elif " or at home? Why" in q:
        q_formatted = q.replace("? Why", "?\nWhy")
    else:
        q_formatted = q

    # Format Korean question translation naturally with matching line breaks
    if " (" in q_ko and q_ko.endswith(")"):
        parts_ko = q_ko.rsplit(" (", 1)
        base_ko = parts_ko[0]
        choices_ko = "(" + parts_ko[1]
        q_ko_formatted = base_ko + "\n" + choices_ko
    elif "? 왜" in q_ko:
        q_ko_formatted = q_ko.replace("? 왜", "?\n왜")
    elif "이고, " in q_ko:
        q_ko_formatted = q_ko.replace("이고, ", "이고,\n")
    elif "하고, " in q_ko:
        q_ko_formatted = q_ko.replace("하고, ", "하고,\n")
    elif "보고, " in q_ko:
        q_ko_formatted = q_ko.replace("보고, ", "보고,\n")
    elif "가고, " in q_ko:
        q_ko_formatted = q_ko.replace("가고, ", "가고,\n")
    elif "무엇이고, " in q_ko:
        q_ko_formatted = q_ko.replace("무엇이고, ", "무엇이고,\n")
    elif "있나요, " in q_ko:
        q_ko_formatted = q_ko.replace("있나요, ", "있나요,\n")
    else:
        q_ko_formatted = q_ko

    item["question"] = q_formatted
    item["questionTranslation"] = q_ko_formatted

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json questions successfully updated with clear line breaks!")
