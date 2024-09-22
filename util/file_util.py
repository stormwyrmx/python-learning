from pathlib import Path

def print_file_info(file_name:str)->None:
    try:
        path = Path(file_name)
        contents = path.read_text()
    except Exception as e:
        print(e)
    else:
        print(contents)

def append_to_file(file_name:str,data:str):
    path = Path(file_name)
    path.open('a').write(data)

if __name__ == '__main__':
    append_to_file("D:/fuck.txt","xiaoqiqi")
