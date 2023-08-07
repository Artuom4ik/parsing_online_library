import os
import json
import logging
import argparse

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from tululu import parse_book_page, download_book


def get_range():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--start_page', nargs='?', type=int, default=1)
    parser.add_argument('--end_page', nargs='?', type=int, default=702)
    parser.add_argument('--dest_folder', nargs='?', type=str, default='./')
    parser.add_argument('--skip_imgs', action='store_true')
    parser.add_argument('--skip_txt', action='store_true')
    parser.add_argument(
        '--json_path',
        nargs='?',
        type=str,
        default='book_description.json'
    )
    args = parser.parse_args()
    return (
        args.start_page,
        args.end_page,
        args.dest_folder,
        args.skip_imgs,
        args.skip_txt,
        args.json_path
    )


def download_all_books(page, skip_txt, skip_imgs, json_path, dest_folder):
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
            download_book(book_num, skip_txt, skip_imgs, dest_folder)
    with open(json_path, 'w', encoding='utf8') as json_file:
        json.dump(books, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    logging.basicConfig(
        filename='app.log',
        filemode='w',
        level=logging.INFO,
        encoding='utf-8'
    )
    start_page, end_page, dest_folder, skip_imgs, skip_txt, json_path = get_range()
    os.makedirs(dest_folder, exist_ok=True)
    json_path = os.path.join(dest_folder, json_path)
    for page in range(start_page, end_page):
        download_all_books(page, skip_txt, skip_imgs, json_path, dest_folder)