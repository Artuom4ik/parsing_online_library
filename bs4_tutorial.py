import requests
from bs4 import BeautifulSoup


url = 'https://tululu.org/b1/'
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'lxml')
title, author = soup.find('body').find('table').find('div', id='content').find('h1').text.split('::')
author = author.strip()
print(f'Заголовок: {title}')
print(f'Автор: {author}')
