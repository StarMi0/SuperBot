import requests, sqlite3
import io
from PIL import Image

conn = sqlite3.connect('code.db')
cursor = conn.cursor()


def check_code(user_id: str, social: str) -> bool:
    cursor.execute("SELECT * FROM USERS WHERE social = ? AND user_id = ?", (social, user_id))
    results = cursor.fetchall()
    return bool(results)


def add_to_db(user_id: str, social: str, img_url: str):
    cursor.execute("INSERT INTO USERS (social, user_id, url) VALUES (?, ?, ?)",
                   (social, user_id, img_url))
    conn.commit()


def image_save(image: Image, user_id: str, social: str) -> str:
    """
    Сохраняет изображение под id пользователя и наименованием социальной сети где он получил купон.
    :param image:
    :param user_id:
    :param social:
    :return: path like object
    """
    with open(f"{user_id}_{social}.jpg", "wb") as f:
        f.write(image)


def url_parce(test: bool, social: str) -> str:
    """
    Собирает путь к штрихкоду в зависимости от параметров запроса
    :param test: True or False
    :param social: vk, in, tg
    :return: string url type
    """
    url_to_db = 'http://31.186.145.106:55080/'
    discount = '/hs/chatbot/getdiscountcode/'
    if test:
        url = url_to_db + 'test' + discount + social
    else:
        url = url_to_db + 'retail' + discount + social
    return url


def get_discount_code(social: str, user_id: str, force=False):
    """
    Забирает штрихкод из базы данных, сохраняет его как изображение, вставляет его в шаблон, возвращает готовое
    изображение с подарочным штрихкодом.
    :param social: vk, in, tg
    :param user_id:
    :return:
    """
    if not check_code(user_id, social) or force is True:
        login = key_dict['BD_login']
        password = key_dict['BD_pass']
        img_path = 'media'
        url = url_parce(True, social)
        r = requests.get(url, auth=(login, password))
        image = Image.open(f'{img_path}/{social}.jpg')
        if r.status_code == 200:
            image_bytes = r.content
            insert_code = Image.open(io.BytesIO(image_bytes))
            new_img = insert_image(image, insert_code, x=505, y=130)
            new_img.save(f"{img_path}/code/{social}_{user_id}.jpg")
            add_to_db(user_id, social, f"{social}_{user_id}.jpg")
            return f"{img_path}/code/{social}_{user_id}.jpg"
        else:
            return None
    else:
        return False


def get_square_edges(img):
    width, height = img.size

    left_edge = 0
    right_edge = 0
    top_edge = 0
    bottom_edge = 0

    for x in range(width):
        for y in range(height):
            px = img.getpixel((x, y))
            if px == (255, 255, 255):
                if x < left_edge or left_edge == 0:
                    left_edge = x
                if x > right_edge:
                    right_edge = x
                if y < top_edge or top_edge == 0:
                    top_edge = y
                if y > bottom_edge:
                    bottom_edge = y

    return (left_edge, top_edge, right_edge, bottom_edge)


def insert_image(img, insert_img, x, y):
    insert_img = insert_img.resize((370, 221), Image.Resampling.NEAREST)
    insert_width, insert_height = insert_img.size

    x_offset = int(x - (insert_width / 2))
    y_offset = int(y - (insert_height / 2))
    img.paste(insert_img, (x_offset, y_offset))

    return img


def txt_dict(filename):
    d = dict()
    with open(filename) as f:
        for line in f:
            (key, val) = line.split()
            d[key] = val
    return d


key_dict = txt_dict('keys.txt')

if __name__ == "__main__":
    pass
