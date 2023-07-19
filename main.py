import os

import requests
from pathvalidate import sanitize_filename


def check_for_redirect(response):
    if response.history:
        raise requests.HTTPError


def download_txt( url , filename, folder='books/' ):
    filename = sanitize_filename(filename)
    return os.path.join(folder, filename)    


if __name__ == '__main__':
    os.makedirs('books', exist_ok=True)
    for num in range(10):
        url = f"https://tululu.org/txt.php?id={num}"
        filename = f'id{num + 1}.txt'
        response = requests.get(url)
        response.raise_for_status()
        try:
            check_for_redirect(response)
            with open(f'books/{filename}', 'wb') as file:
                file.write(response.content)
        except requests.HTTPError:
            continue
