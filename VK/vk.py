import random
import time

import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from functions.functions import get_discount_code, key_dict

GROUP_ID = key_dict['VK_GROUP_ID']  # Replace with your group ID


def run_vk_bot(longpoll, vk, upload):
    try:
        for event in longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW and \
                    event.object['message']['from_id'] and \
                    event.object['message']['text']:

                if event.object['message']['text'].lower() == 'купон':
                    # Check if user is subscribed to the group

                    is_subscribed = vk.groups.isMember(
                        group_id=GROUP_ID,
                        user_id=event.object['message']['from_id'],
                    )

                    if is_subscribed:
                        # Get discount code link
                        link = get_discount_code('vk', event.object['message']['from_id'])
                        if link:
                            # Open image and send it to the user

                            image = open(link, 'rb')
                            upload_image = upload.photo_messages(photos=image,
                                                                 peer_id=event.object['message']['from_id'])[0]
                            pic = f"photo{upload_image['owner_id']}_{upload_image['id']}"
                            vk.messages.send(
                                user_id=event.object['message']['from_id'],
                                attachment=pic,
                                random_id=random.randint(0, 100)
                            )
                        else:
                            # Send message about existing active coupon
                            vk.messages.send(
                                user_id=event.object['message']['from_id'],
                                message="У Вас уже есть активный купон.",
                                random_id=random.randint(0, 100)
                            )
                    else:
                        # Send message about subscription
                        vk.messages.send(
                            user_id=event.object['message']['from_id'],
                            message=f'Подпишитесь на наш канал: {key_dict["url_vk"]}\n,'
                                    f'чтобы получить купон и повторите попытку.',
                            random_id=random.randint(0, 100)
                        )
                else:
                    # pass # Этот фрагмент кода и до except можно убрать до появления у них необходимо
                    text = f"Не понял, что вы хотели сказать: {event.object['message']['text']}\n" \
                           f"Если вы хотите получить купон, вы должны подписаться на группу {key_dict['url_vk']}\n" \
                           f"И написать мне сообщение 'КУПОН'☺"

                    vk.messages.send(
                        user_id=event.object['message']['from_id'],
                        message=text,
                        random_id=random.randint(0, 100)
                    )
    except requests.exceptions.ReadTimeout:
        print("\n Переподключение к серверам ВК \n")
        time.sleep(3)