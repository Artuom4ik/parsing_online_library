import os

import requests
from pathvalidate import sanitize_filename
from bs4 import BeautifulSoup


def check_for_redirect(response):
    if response.history:
        raise requests.HTTPError


def download_txt(url, filename, num_book, folder='books/'):
    filename = f'{num_book}.{sanitize_filename(filename)}.txt'
    return os.path.join(folder, filename)


def get_title_author_book(num_book):
    url = f'https://tululu.org/b{num_book}/'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    return soup.find('body').find('table').find('div', id='content').find('h1').text.split('::')


if __name__ == '__main__':
    os.makedirs('books', exist_ok=True)
    for num_book in range(1, 11):
        url = f"https://tululu.org/txt.php?id={num_book}"
        response = requests.get(url)
        response.raise_for_status()
        try:
            check_for_redirect(response)
            filename, author = get_title_author_book(num_book)
            filename = filename.strip()
            directory = download_txt(url, filename, num_book)
            with open(directory, 'wb') as file:
                file.write(response.content)
        except requests.HTTPError:
            continue