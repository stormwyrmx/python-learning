from pathlib import Path
from data_define import *
import json



class TextFileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        record_list = []
        contents = Path(self.file_path).read_text('utf-8')
        for line in contents.splitlines():
            splitlines = line.split(',')
            record = Record(splitlines[0], splitlines[1], int(splitlines[2]), splitlines[3])
            record_list.append(record)
        return record_list


class JsonFileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        record_list = []
        contents = Path(self.file_path).read_text('utf-8')
        for line in contents.splitlines():
            data_dict = json.loads(line)  # 每一个line是一个json字符串
            record = Record(data_dict['date'], data_dict['order_id'], int(data_dict['money']), data_dict['province'])
            record_list.append(record)
        return record_list


if __name__ == '__main__':
    # file_path = Path("../data/数据分析案例/2011年1月销售数据.txt")
    # text_file_reader = TextFileReader(file_path)
    # file = text_file_reader.read_file()
    # for record in file:
    #     print(record)
    # print(file.__str__())

    file_path = Path("../data/数据分析案例/2011年2月销售数据JSON.txt")
    json_file_reader = JsonFileReader(file_path)
    json_data = json_file_reader.read_file()
    for record in json_data:
        print(record)
    print(json_data)
    print(type(json_data))
