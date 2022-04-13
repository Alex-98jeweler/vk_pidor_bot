from vk_api import VkApi
from random import randint
from vk_api.bot_longpoll import VkBotLongPoll
import json

class VkBot():

    def __init__(self, token, group_id) -> None:
        self.__api = VkApi(token=token)
        self.group_id = group_id
        self.lp = VkBotLongPoll(self.__api, group_id)

    def send_message(self, to, body, keyboard=None):
        self.__api.method('messages.send', values={"peer_id": to, 
                                                    'message': body, 
                                                    "random_id": randint(9999999, 9999999999999),
                                                    'keyboard': keyboard
                                                    })

    def get_chat_members(self, chat_id):
        try:
            a = self.__api.method("messages.getConversationMembers", values={
                                                                            "peer_id": chat_id
                                                                            })
            return a
        except:
            self.send_message(chat_id, "Для этого необходимо меня назначить администратором сообщества")

    def get_keyboard(self, keyboard: dict):
        keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
        keyboard = str(keyboard.decode('utf-8'))
        return keyboard

