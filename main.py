import requests

url = 'http://data.fixer.io/api/'
key = 'access_key=70402a075db79ce14ef44d254f828ec9'


def data(date, url=url, acc=key):
    req_his = requests.get(f'{url}' + f'{date}?' + f'{acc}')

    with open('historical.json', 'w') as f:
        f.write(req_his.text)


data('2000-11-10')