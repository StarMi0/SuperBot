import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from functions.functions import get_discount_code

GROUP_ID = 12345  # Replace with your group ID

# Connect to VK API
vk_session = vk_api.VkApi(token="YOUR_TOKEN_HERE")
longpoll = VkBotLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.object.text.lower() == 'хочу купон':
        # Check if user is subscribed to the group
        is_subscribed = vk.groups.isMember(
            group_id=GROUP_ID,
            user_id=event.object.from_id
        )

        if is_subscribed:
            # Get discount code link
            link = get_discount_code('vk', event.object.from_id)
            if link:
                # Open image and send it to the user
                image = open(link)
                vk.messages.send(
                    user_id=event.object.from_id,
                    attachment=image,
                )
            else:
                # Send message about existing active coupon
                vk.messages.send(
                    user_id=event.object.from_id,
                    message="You already have an active coupon."
                )
        else:
            # Send message about subscription
            vk.messages.send(
                user_id=event.object.from_id,
                message="Subscribe to our channel and try again."
            )
