import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://xn----7sbiew6aadnema7p.xn--p1ai/alphabet.php'
def get_towns():
    need = []
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml').find('div', {'id': 'content'}).find('ul')
    for a in soup.find_all('li'):
        need.append(a.text)
    with open('rus_towns.txt', 'w', encoding='utf-8') as file:
        for i in need:
            file.write(i + '\n')

get_towns()