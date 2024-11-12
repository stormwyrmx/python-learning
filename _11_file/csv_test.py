import csv

"""
csv: comma separated values
"""

def write_csv():
    with open('girl.csv', 'w', encoding='utf-8') as f:
        list1=['胡思琪','秋山澪','樱岛麻衣']
        f.write(','.join(list1))

def read_csv():
    with open('girl.csv', 'r', encoding='utf-8')as f:
        s = f.read()
        print(s)
        split = s.split(',')
        print(split)

def write_csv_2d():
    with open('girl_2d.csv', 'w', encoding='utf-8')as f:
        list1=[
            ['name','age','size'],
            ['秋山澪',"17","85"],
            ['樱岛麻衣',"16","80"]
        ]
        for item in list1:
            f.write(','.join(item)+'\n')

def read_csv_2d():
    with open('girl_2d.csv', 'r', encoding='utf-8')as f:
        data=[]
        list1 = f.readlines()
        for line in list1:
            split = line.strip().split(',')
            # split = line[0:-2].split(',')
            data.append(split)
        print(data)
        # for line in f:
        #     print(line.strip().split(','))

if __name__ == '__main__':
    # write_csv()
    # read_csv()
    write_csv_2d()
    read_csv_2d()