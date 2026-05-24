import re

def analyze_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            code = f.read()
    except:
        return {
            "functions": 0,
            "loops": 0,
            "conditions": 0,
            "comments": 0,
            "lines": 0
        }

    return {
        "functions": len(re.findall(r"def ", code)),
        "loops": len(re.findall(r"\bfor\b|\bwhile\b", code)),
        "conditions": len(re.findall(r"\bif\b", code)),
        "comments": len(re.findall(r"#", code)),
        "lines": len(code.split("\n"))
    }