# ТЕХНИЧЕСКОЕ ЗАДАНИЕ на разработку чат-бота Telegram и VK для компании «Наша обувь»

## Требуется разработать программный код(приложение) на языке программирования PHP(не меньше версии 8) или Python (не ниже 3.8) для автоматизации процесса выдачи индивидуальных купонов на скидку с уникальным штрих-кодом из 1С.
Разрабатываемое приложение состоит из: чат-бота для мессенджера телеграм, чат-бота для социальной сети
Вконтакте, чат-бот для социальной сети инстаграм, и функции для запроса штрих-кода из 1С и генерации
купона. Приложение располагается на бесплатном хостинге beget.ru. Адрес хостинга предоставляет исполнитель.
Хостинг регистрируется на заказчика.
## Минимальные требования к хостингу:
1 ГБ NVME, 1 база данных, 1 FTP-аккаунт, нагрузка до 15 CP.
## Общие требования к приложению:
1. В базе данных должна быть информация о сгенерированных купонах. Кому отправлен купон, дата и время генерации, какой канал отправки. ТИп базы – MySQL.
2. Поля базы данных:
- Дата создания – тип дата. Дата отправки купона.
- Имя пользователя – тип строка, записывается ник пользователя, которому отправлен купон.
- Соц сеть – список. Значения: ВК, ИНСТА, TG. Указывается соц сеть, которой выдан купон.
## Требования к чат-боту телеграм:
1. Должен принимать сообщения от клиента
2. После запуска чат-бота клиентом, бот проверяет клиента на выдачу купона(выдавался ли ранее купон по базе данных) и подписку на канал (адрес канала предоставляет заказчик)
3. Если подписки не обнаружено бот присылает сообщение с предложением для подписки
4. После подписки бот присылает сгенерированный купон
5. Токен и доступ к боту предоставляет заказчик
- Алгоритм работы. Клиент добавляется к "чат–боту". Чат-бот присылает приветственное сообщение. Текст предоставляет заказчик. И отображается кнопка «Хочу купон». При клике на кнопку, бот проверяет клиента по двум условиям. Подписка на канал, выдавался ли ранее. Если оба условия выполнены (подписка есть, нет в списке выданных) бот присылает сгенерированный купон и текстовое сообщение(текст предоставляет
заказчик) в чат.
## Требования к чат-боту ВК:
1. Должен принимать сообщения от клиента
2. После запуска чат-бота клиентом, бот проверяет клиента на выдачу купона(выдавался ли ранее
купон) и подписку на группу (адрес группы предоставляет заказчик)
3. Если подписки не обнаружено бот присылает сообщение с предложением для подписки
4. После подписки бот присылает сгенерированный купон
5. Токен и доступ к боту предоставляет заказчик
- Алгоритм работы. Клиент добавляется к "чат–боту". Чат-бот присылает приветственное сообщение. Текст
предоставляет заказчик. И отображается кнопка «Хочу купон». При клике на кнопку, бот проверяет клиента
по двум условиям. Подписка на канал, выдавался ли ранее. Если оба условия выполнены (подписка есть, нет
в списке выданных) бот присылает сгенерированный купон и текстовое сообщение(текст предоставляет
заказчик) в чат.
## Требования к чат-боту Инстаграм:
1. Должен принимать сообщения от клиента
2. После запуска чат-бота клиентом, бот проверяет клиента на выдачу купона(выдавался ли ранее
купон) и подписку на группу (адрес группы предоставляет заказчик)
3. Если подписки не обнаружено бот присылает сообщение с предложением для подписки
4. После подписки бот присылает сгенерированный купон
5. Токен и доступ к боту предоставляет заказчик.
6. Подключение к соц. сети через VPN. VPN оплачивает заказчик.
- Алгоритм работы. Клиент пишет в директ «хочу купон». Чат-бот проверяет клиента по двум условиям.
Подписка на канал, выдавался ли ранее. Если оба условия выполнены (подписка есть, нет в списке выданных) бот присылает сгенерированный купон и текстовое сообщение(текст предоставляет заказчик) в
директ клиенту.
## Требования к функции по генерации купона:
1. Функция запрашивает у 1С по веб-адресу (ссылке) картинку штрих-кода. Ссылка предоставляется
заказчиком.
2. Функция должна забирать у 1С png картинку штрих-кода по стандартному протоколу.
3. Функция должна генерировать изображение по представленному макету. Должна быть
возможность замены макета. Макет предоставляется заказчиком. Параметры макета: формат – jpg или png.
Размер: не менее 980х1024. Примеры изображений: 
<image src="./media/instagramm.jpg" alt="Instagramm" caption="Для Instagramm">
<image src="./media/telegramm.jpg" alt="Telegramm" caption="Для Telegramm">
<image src="./media/vk.jpg" alt="VK" caption="Для VK">
4. Функция должна передавать сгенерированное изображение чат-боту.
## Требования к 1С:
1. 1С должна быть доступна в сети интернет, для обращения к ней для запроса штрих-кода. Адрес
предоставляет заказчик.
2. 1С предоставляет штрих код в формате png.
Срок разработки не более 2 недель. Разработка ведется на ресурсах исполнителя. После утверждения,
переносится на хостинг заказчика.