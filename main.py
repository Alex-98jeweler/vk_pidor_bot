from controller import Controller
from config import KEYBOARD
from parser import get_peer_id, get_users
from models import Base

controller = Controller()

for event in controller.vk.lp.listen():
    print(event.message)
    if event.message:
        if ('action' in event.message and event.message['action']['type'] == "chat_invite_user"):
            try:
                Base.metadata.create_all(controller.db.engine)
            except:
                pass
            controller.vk.send_message(get_peer_id(event.message), "Клавиатура для запуска бота, перед запуском не забудь назначить администратором беседы", keyboard=controller.vk.get_keyboard(KEYBOARD))
            chat_id = get_peer_id(event.message)
            controller.db.add_chat(chat_id)
            controller.db.add_call_bot(chat_id)

        
controller.db.connect.close()
