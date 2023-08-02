import os

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


if __name__ == '__main__':
    url = "https://tululu.org/l55/"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    book_id = soup.find('div', id='content').find('table').find_all('tr')[1].find('a')['href']
    book_url = urljoin('https://tululu.org/', book_id)
    print(book_url)