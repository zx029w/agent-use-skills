
import sys
import os
import docx
import json

def read_docx(file_path):
    try:
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            if para.text.strip():
                full_text.append(para.text)
        return '\n'.join(full_text)
    except Exception as e:
        return f"Error reading {os.path.basename(file_path)}: {e}"

def scan_reports(path):
    results = {}

    if os.path.isfile(path):
        if path.endswith('.docx'):
            results[os.path.basename(path)] = read_docx(path)
    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith('.docx') and not file.startswith('~$'):
                    full_path = os.path.join(root, file)
                    results[file] = read_docx(full_path)

    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python read_reports.py <file_or_directory_path>")
        sys.exit(1)

    target_path = sys.argv[1]
    reports = scan_reports(target_path)

    # 输出为格式化的 JSON 字符串，方便 AI 阅读
    print(json.dumps(reports, ensure_ascii=False, indent=2))
