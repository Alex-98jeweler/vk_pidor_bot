from db import DB
from vk_bot import VkBot
from config import KEYBOARD, TOKEN, GROUP_ID
from parser import *
from models import Base

bot = VkBot(TOKEN, GROUP_ID)
db = DB()


print(db.get_users(2000000002))
# for event in bot.lp.listen():
#     print(event.message)
#     if event.message:
#         if ('action' in event.message and event.message['action']['type'] == "chat_invite_user"):
#             try:
#                 Base.metadata.create_all(db.engine)
#             except:
#                 pass
#             bot.send_message(get_peer_id(event.message), "Hi", keyboard=bot.get_keyboard(KEYBOARD))
#             chat_id = get_peer_id(event.message)
#             db.add_chat(chat_id)
#             db.add_call_bot(chat_id)
#         if 'payload' in event.message:
#             get_command(event.message)
        
    


db.connect.close()
