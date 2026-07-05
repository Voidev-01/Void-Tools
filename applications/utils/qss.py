def open_file_qss(file_name: str):
    with open(file_name, 'r', encoding="utf-8") as f:
        return f.read()

