import csv

"""
csv: comma separated values
"""

def write_csv():
    with open('data/girl.csv', 'w', encoding='utf-8') as f:
        list1=['胡思琪','秋山澪','樱岛麻衣']
        f.write(','.join(list1))

def read_csv():
    with open('data/girl.csv', 'r', encoding='utf-8')as f:
        s = f.read()
        print(s)
        split = s.split(',')
        print(split)

def write_csv_2d():
    with open('data/girl_2d.csv', 'w', encoding='utf-8')as f:
        list1=[
            ['name','age','size'],
            ['秋山澪',"17","85"],
            ['樱岛麻衣',"16","80"]
        ]
        for item in list1:
            f.write(','.join(item)+'\n')

    with open('data/girl_2d.csv', 'w', encoding='utf-8' ,newline='')as f:
        csv_writer = csv.writer(f)
        list1=[
            ['name','age','size'],
            ['秋山澪',"17","85"],
            ['樱岛麻衣',"16","80"]
        ]
        for item in list1:
            # writerow() 会把传入的列表写成一行，元素之间用逗号分隔，并在结尾自动加上换行符（\n）。所以前面要加newline=''
            csv_writer.writerow(item)
        # csv_writer.writerows(list1)

def read_csv_2d():
    with open('data/girl_2d.csv', 'r', encoding='utf-8')as f:
        data=[]
        list1 = f.readlines()
        for line in list1:
            split = line.strip().split(',')
            # split = line[0:-2].split(',')
            data.append(split)
        print(data)
        # for line in f:
        #     print(line.strip().split(','))

    with open('data/girl_2d.csv', 'r', encoding='utf-8')as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            print(row)


if __name__ == '__main__':
    # write_csv()
    # read_csv()
    write_csv_2d()
    read_csv_2d()