# INSTALLATION
Для установки достаточно скачать репозиторий через команду:
```shell
git clone https://github.com/User/SuperBot
```
После установки необходимо создать в родительском каталоге 3 файла:
- [run.sh](./run.sh)
- [keys.txt](./keys.txt)
- [code.db](./code.db)
1. Файл [run.sh](./run.sh) служит для автоматизации запуска и имеет следующий вид:
```shell
#!/bin/bash

pkill python

git pull origin master

source env/bin/activate

pip install -r req.txt

python3.8 main.py &

python3.8 create_bot_vk.py &
```
2. Файл [keys.txt](./keys.txt) хранит ключи и ссылки к проекту, о нем сказано в разделе [Other](#Other:)
3. Файл [code.db](./code.db) это база данных в виде SQlite3, которая содержит единственную таблицу следующего формата:

| id  | social | user_id | url |
|-----|------|-------|---|
| row id | vk \ tg | ID of user accaunt | Path to file of coupon |

# UPDATING
Обновление происходит автоматически при перезагрузке, это прописано в файле [run.sh](./run.sh), при запуске которого происходит обновление кода из репозитория и обновление всех установленных библиотек, а так же перезапуск приложения.
# Docker
На данный момент не используется.
# Keys
___
# Other:
1. [Техническое задание](./TZ.md)
2. В корне должен располагаться файл keys.txt в котором указываются ключи от ботов, не загружается из репозитория, хранится локально, имеет ограниченный доступ. Ключи расположены в следующем порядке:
- Телеграмм
- ВК
Имеет следующую структуру (последовательность может быть любая, но все заголовки должны присутствовать, варинтов с ошибками считыванния не предусмотрено):
```text
TGID Telegram_bot_token
BD_login Data_base_login
BD_pass Data_base_password
tg_chanel Telegramm_chanall_ID
url_tg URL_to_telegramm_channel
VKID VK_bot_token
```