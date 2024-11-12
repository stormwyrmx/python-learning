from pathlib import Path

path = Path("D:/OneDrive - mail.nwpu.edu.cn/笔记/华为手机备忘录/刀剑神域.txt")
lines = path.read_text('utf-8').splitlines()

for line in lines:
    print(line)

def write_file():
    path.write_text("物语系列")
