# Парсер онлайн библиотеки
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

___
#### Данная программа скачивает определенное колличество книг, а также картинки, комментарии к ним с сайта [tululu.org](https://tululu.org/).
___
### Содержание:
* [Требования](https://github.com/Artuom4ik/parsing_online_library#%D0%B4%D0%BB%D1%8F-%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA%D0%B0-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%8B-%D1%82%D1%80%D0%B5%D0%B1%D1%83%D0%B5%D1%82%D1%81%D1%8F)
* [Как пользоваться скриптом](https://github.com/Artuom4ik/parsing_online_library#%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F-%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%BC)
* [Описание каждой функции](https://github.com/Artuom4ik/parsing_online_library#%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BA%D0%B0%D0%B6%D0%B4%D0%BE%D0%B9-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8)
* [Цель проекта](https://github.com/Artuom4ik/parsing_online_library#%D1%86%D0%B5%D0%BB%D1%8C-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)
___
### Для запуска программы требуется:
 * Скачать [Python](https://www.python.org/) версии 3.1 или выше.
 * Операционная система macOS, linux, windows 7 или выше.
 * Установить нужные библиотеки с помощью команды:
 ```
 pip install -r requirements.txt
 ```
___
### Как пользоваться скриптом:
* Чтобы запустить программу, требуется написать в консоль:
```
python main.py start_id end_id
```
* start_id и end_id - диапазон скачивания книг. По умолчанию дапозон стоит от 1 до 10.
* В процессе запуска программы, создастся папка для книг и картинок(название папок стоят по умолчанию, но вы можете изменить название).
___
### Описание каждой функции:
* ```parse_book_page()``` - возращает словарь с полной информацией одной книги: заголовок, автор, ссылку на картинку, жанр, комментарии.
* ```check_for_redirect()``` - проверяет было ли сделано перенапровление, если перенапровление было, то поднимется исключение ```HTTPError```.
* ```download_txt()``` - скачивает определенную книгу(по желанию аргумент ```folder``` вы можете назвать по свойму).
* ```download_img()``` - скачивает картинку определенной книги.
* ```get_title_author_book()``` - возращает заголовок и автора книги.
___
### Цель проекта:
* Код написан в образовательных целях.
