from db import DB
from vk_bot import VkBot
from config import KEYBOARD, TOKEN, GROUP_ID
from parser import get_peer_id
from models import Base

bot = VkBot(TOKEN, GROUP_ID)
db = DB('bot.db')

for event in bot.lp.listen():
    print(event.message)
    if event.message:
        if ('action' in event.message and event.message['action']['type'] == "chat_invite_user"):
            Base
            bot.send_message(get_peer_id(event.message), "Hi", keyboard=bot.get_keyboard(KEYBOARD))
    



