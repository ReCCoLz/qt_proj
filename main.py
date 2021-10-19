import requests
import os 

url = 'http://data.fixer.io/api/'
key = 'access_key=f83859c0187edb449a865f5e632951aa'


def merge_data():
    inf = []
    for i in os.listdir('C:/Users/recol/Documents/my_projects(python)/qt_proj/data'):
        with open(f'C:/Users/recol/Documents/my_projects(python)/qt_proj/data/{i}', 'r', encoding='utf-8') as f:
            inf.append(f.read() + '\n')



    with open('all_data_merge.json', 'w', encoding='utf-8') as d:
        for j in inf:
            d.write(j)


def data(date, url=url, acc=key):
    req_his = requests.get(f'{url}' + f'{date}?' + f'{acc}')
    date = str(date).split('-')

    with open(f'C://Users//recol//Documents//my_projects(python)//qt_proj//data//historical{date[0]}.{date[1]}.json', 'w') as f:
        f.write(req_his.text)

def get_data():
    for year in range(21):
        for mounth in range(1, 12+1):
            if year < 10:
                if mounth < 10:
                    data(f'200{year}-0{mounth}-10')
                else:
                    data(f'200{year}-{mounth}-10')
            else:
                if mounth < 10:
                    data(f'20{year}-0{mounth}-10')
                else:
                    data(f'20{year}-{mounth}-10')