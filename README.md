# INSTALLATION
# DOWNLOADING
# UPDATING
# DB
# Docker
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
3. В папке [Telegramm](./Telegramm) должны располагаться 2 файла:
- admin.txt (где указываются ID пользователей, являющимися администраторами)
- sallers.txt (где указываются ID пользователей, являющимися продавцами)