import os

import requests


os.makedirs('books', exist_ok=True)
for num in range(10):
    filename = f'id{num}.txt'
    url = f"https://tululu.org/txt.php?id={num}"
    response = requests.get(url)
    response.raise_for_status()
    with open(f'books/{filename}', 'wb') as file:
        file.write(response.content)