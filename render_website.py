import json
import collections
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

def get_books_description():
    with open("parse/book_description.json", "r", encoding='utf-8') as my_file:
        books_description_json = my_file.read()

    books_description = json.loads(books_description_json)
    return books_description


def render_website():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template/template.html')

    rendered_page = template.render(
        books_description = get_books_description()
    )

    with open('template/index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    render_website()