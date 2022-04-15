from calendar import c
from datetime import datetime, timedelta
from random import randint
from time import sleep
from config import *
from db import DB
from parser import get_users
from vk_bot import VkBot




class Controller:

    def __init__(self):
        self.vk = VkBot(TOKEN, GROUP_ID)
        self.db = DB()


    def __init_chat_members_list(self, chat_id):
        users = self.vk.get_chat_members(chat_id)
        users = get_users(users)
        for i in users:
            self.db.add_user(i['first_name'], i['last_name'], i['id'], chat_id)


    def set_mode(self, command):
        return COMMAND[command] 


    def __gen_random_user(self, chat_id):
        try:
            a = self.db.get_users(chat_id)
            b = a[0]
        except IndexError:
            self.__init_chat_members_list(chat_id)
            print('Я исключение')
            return self.__gen_random_user(chat_id)
        num = randint(0, len(a) - 1)
        return a[num]

    
    def choice(self, command, chat_id):
        messages, mode, name = command
        print(messages[0])
        user = self.__gen_random_user(chat_id)
        self.__add_change(chat_id, mode)
        if self.__check_call(mode, chat_id):
            for i in messages:
                if messages.index(i) == len(messages) - 1:
                    self.vk.send_message(chat_id, i.format(user[3], user[1], user[2]))
                else:
                    self.vk.send_message(chat_id, i)
                    sleep(1)
        else:
            self.vk.send_message(chat_id, f"{name} можно определить через сутки")

    def __add_change(self, chat_id, column):
        self.db.update_call_bot(column, chat_id)

    def __check_call(self, column, chat_id):
        result = self.db.select_call(column, chat_id)[0][0]
        if datetime.fromisoformat(result) > datetime.now() + timedelta(days=1):
            return True
        else:
            return False
                  