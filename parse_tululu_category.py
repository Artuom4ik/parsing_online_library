import os
import json
import logging

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from main import parse_book_page, download_book


if __name__ == '__main__':
    logging.basicConfig(
        filename='app.log',
        filemode='w',
        level=logging.INFO,
        encoding='utf-8'
    )
    folder = './'
    json_filename = 'book_description.json'
    file_path = os.path.join(folder, json_filename)
    for page in range(1, 5):
        url = f"https://tululu.org/l55/{page}"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        books = {
            "books": [],
        }
        for book in soup.select('div table tr'):
            if book.select('div.bookimage a'):
                book_id = book.select('div.bookimage a')[0]['href']
                book_num = book_id.split('/')[1].split('b')[1]
                book_url = urljoin('https://tululu.org/', book_id)
                response = requests.get(book_url)
                response.raise_for_status()
                book_description = parse_book_page(response.text)
                books["books"].append(book_description)
                download_book(book_num)
        with open(file_path, 'w', encoding='utf8') as json_file:
            json.dump(books, json_file, indent=4, ensure_ascii=False)