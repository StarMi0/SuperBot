import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from functions.functions import key_dict
from VK.vk import run_vk_bot


# Connect to VK API
vk_session = vk_api.VkApi(token=key_dict['VKID'])
vk = vk_session.get_api()
upload = vk_api.VkUpload(vk)
longpoll = VkBotLongPoll(vk_session, key_dict['VK_GROUP_ID'])


if __name__ == "__main__":
    run_vk_bot(longpoll, vk, upload)


