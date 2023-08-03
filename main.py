import os
import argparse
import logging
import time

import requests
from pathvalidate import sanitize_filename
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def download_book(book_id):
    first_reconnect = True
    while True:
        try:
            url = f'https://tululu.org/b{book_id}/'
            response = requests.get(url)
            response.raise_for_status()
            check_for_redirect(response)
            book_description = parse_book_page(response.text)
            name_book = book_description["title"]
            img_url = book_description['img_url']
            name_img = img_url.split('/')[-1]
            download_txt(name_book, book_id)
            download_img(img_url, name_img)
            logging.info(f'Книга по номером {book_id}, скачалась успешно')
            return response.status_code
        except requests.exceptions.HTTPError:
            logging.error(f'Ошибка скачивания книги под номером {book_id}')
            break
        except requests.exceptions.ConnectionError:
            if first_reconnect:
                logging.error('Разрыв соединения.')
                logging.info('Идет переподключение, займет 5 секунд.')
                time.sleep(5)
                first_reconnect = False
            else:
                logging.error('Соединение снова разорвано.')
                logging.info('Идет переподключение, займет 15 секунд.')
                time.sleep(15)


def get_range():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('start_id', nargs='?', type=int, default=1)
    parser.add_argument('end_id', nargs='?', type=int, default=10)
    args = parser.parse_args()
    return args.start_id, args.end_id


def check_for_redirect(response):
    if response.history:
        raise requests.exceptions.HTTPError


def download_txt(filename, num_book, folder='books/'):
    os.makedirs(folder, exist_ok=True)
    params = {
        'id': num_book
    }
    url_book = "https://tululu.org/txt.php"
    response = requests.get(url_book, params=params)
    response.raise_for_status()
    check_for_redirect(response)
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


def parse_book_page(page):
    soup = BeautifulSoup(page, 'lxml')
    relative_url = soup.find('div', class_='bookimage').find('img')['src']
    img_url = urljoin('https://tululu.org/', relative_url)
    title, author = get_title_author_book(page)
    genre_tags = soup.find('span', class_='d_book').find_all('a')
    comments_tags = soup.find_all('div', class_='texts')
    genres = [genre.text
              for genre in genre_tags]
    comments = [comment.find('span').text
                for comment in comments_tags]

    return {
        'title': title.strip(),
        'author': author.strip(),
        'img_url': img_url,
        'genres': genres,
        'comments': comments
    }


def get_title_author_book(page):
    soup = BeautifulSoup(page, 'lxml')
    return 


if __name__ == '__main__':
    start_id, end_id = get_range()
    logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO, encoding='utf-8')
    for num_book in range(start_id, end_id + 1):
        download_book(num_book)
