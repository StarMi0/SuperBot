import os

import requests, sqlite3
import io
from PIL import Image


if not os.path.exists('code.db'):
    new_db = open("code.db", "w")
    new_db.close()
conn = sqlite3.connect('code.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='USERS'")
if cursor.fetchone():
    print("Table exists")
else:
    cursor.execute("""CREATE TABLE USERS (
                id INTEGER PRIMARY KEY,
                social TEXT,
                user_id INTEGER,
                url TEXT
                )""")
    conn.commit()


def check_code(social: str, user_id: str) -> bool:
    pass


def add_to_db(social: str, user_id: str, img_url: str):
    pass


def image_save(image: Image, user_id: str, social: str) -> str:
    """
    Сохраняет изображение под id пользователя и наименованием социальной сети где он получил купон.
    :param image:
    :param user_id:
    :param social:
    :return: path like object
    """
    pass


def url_parce(test: bool, social: str) -> str:
    """
    Собирает путь к штрихкоду в зависимости от параметров запроса
    :param test: True or False
    :param social: vk, in, tg
    :return: string url type
    """
    pass


def get_discount_code(social: str, user_id: str):
    """
    Забирает штрихкод из базы данных, сохраняет его как изображение, вставляет его в шаблон, возвращает готовое
    изображение с подарочным штрихкодом.
    :param social: vk, in, tg
    :param user_id:
    :return:
    """
    pass


def get_square_edges(img):
    pass


def insert_image(img, insert_img, x, y):
    pass


def txt_dict(filename):
    d = dict()
    try:
        with open(filename) as f:
            for line in f:
                (key, val) = line.split()
                d[key] = val
    except:
        print("../" + filename)
        with open("../" + filename) as f:
            for line in f:
                (key, val) = line.split()
                d[key] = val
    return d


key_dict = txt_dict('keys.txt')

if __name__ == "__main__":
    pass
