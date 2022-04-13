from vk_bot import VkBot
from config import KEYBOARD, TOKEN, GROUP_ID
from vk_api.bot_longpoll import VkBotEventType
from parser import get_peer_id

bot = VkBot(TOKEN, GROUP_ID)

for event in bot.lp.listen():
    print(event.message)
    if event.message:
        if ('payload' in event.message and event.message['payload'] == '{"command":"start"}') or       \
            ('action' in event.message and event.message['action']['type'] == "chat_invite_user"):
            bot.send_message(get_peer_id(event.message), "Hi", keyboard=bot.get_keyboard(KEYBOARD))
    



