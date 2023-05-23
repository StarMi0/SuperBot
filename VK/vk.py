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
                            vk.messages.send(
                                user_id=event.object['message']['from_id'],
                                message="Для продления работы бота, оформите подписку",
                                random_id=random.randint(0, 100)
                            )
                        else:
                            # Send message about existing active coupon
                            vk.messages.send(
                                user_id=event.object['message']['from_id'],
                                message="Для продления работы бота, оформите подписку",
                                random_id=random.randint(0, 100)
                            )
                    else:
                        # Send message about subscription
                        vk.messages.send(
                            user_id=event.object['message']['from_id'],
                            message=f'Для продления работы бота, оформите подписку',
                            random_id=random.randint(0, 100)
                        )
                else:
                    # pass # Этот фрагмент кода и до except можно убрать до появления у них необходимо
                    text = f"Для продления работы бота, оформите подписку"

                    vk.messages.send(
                        user_id=event.object['message']['from_id'],
                        message=text,
                        random_id=random.randint(0, 100)
                    )
    except requests.exceptions.ReadTimeout:
        print("\n Переподключение к серверам ВК \n")
        time.sleep(3)