import os

import requests


def check_for_redirect(response):
    if response.history:
        raise requests.HTTPError


if __name__ == '__main__':
    os.makedirs('books', exist_ok=True)
    for num in range(10):
        filename = f'id{num + 1}.txt'
        url = f"https://tululu.org/txt.php?id={num}"
        response = requests.get(url)
        response.raise_for_status()
        try:
            check_for_redirect(response)
            with open(f'books/{filename}', 'wb') as file:
                file.write(response.content)
        except requests.HTTPError:
            continue
