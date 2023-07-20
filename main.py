import os

import requests
from pathvalidate import sanitize_filename
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def check_for_redirect(response):
    if response.history:
        raise requests.HTTPError


def download_txt(url, filename, num_book, folder='books/'):
    filename = f'{num_book}.{sanitize_filename(filename)}.txt'
    file_path = os.path.join(folder, filename)
    with open(file_path, 'wb') as file:
        file.write(response.content)


def download_img(img_url, filename, folder='images/'):
    os.makedirs(folder, exist_ok=True)
    response = requests.get(img_url)
    response.raise_for_status()
    file_path = os.path.join(folder, filename)
    with open(file_path, 'wb') as file:
        file.write(response.content)


def get_title_author_book(num_book):
    url = f'https://tululu.org/b{num_book}/'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    return soup.find('h1').text.split('::')


if __name__ == '__main__':
    # os.makedirs('books', exist_ok=True)
    # for num_book in range(1, 11):
    #     url = f"https://tululu.org/txt.php?id={num_book}"
    #     response = requests.get(url)
    #     response.raise_for_status()
    #     try:
    #         check_for_redirect(response)
    #     except requests.HTTPError:
    #         continue
    #     filename, author = get_title_author_book(num_book)
    #     filename = filename.strip()
    #     author = author.strip()
    #     download_txt(url, filename, num_book)

    for i in range(1, 11):
        url = f'https://tululu.org/b{i}/'
        response = requests.get(url)
        response.raise_for_status()
        try:
            check_for_redirect(response)
        except requests.HTTPError: 
            continue
        soup = BeautifulSoup(response.text, 'lxml')
        relative_url = soup.find('div', class_='bookimage').find('img')['src']
        title, author = soup.find('h1').text.split('::')
        comments = soup.find_all('div', class_='texts')
        img_url = urljoin('https://tululu.org/', relative_url)
        img_name = relative_url.split('/')[-1]
        print(f'Автор: {author}')
        print(f'Заголовок: {title}')
        for comment in comments:
            print(comment.find('span').text)
        # download_img(img_url, img_name)
        