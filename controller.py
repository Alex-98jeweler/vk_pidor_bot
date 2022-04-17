from datetime import datetime, timedelta
from random import randint
import re
from time import sleep, time
import time
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


    def __gen_random_user(self, chat_id):
        try:
            a = self.db.get_users(chat_id)
            b = a[0]
        except IndexError:
            self.__init_chat_members_list(chat_id)
            self.db.add_call_bot(chat_id)
            print('Я исключение')
            return self.__gen_random_user(chat_id)
        num = randint(0, len(a) - 1)
        return a[num]

    
    def choice(self, command, chat_id):
        messages, column_call, name, column_count = command
        user = self.__gen_random_user(chat_id)
        if self.__check_call(column_call, chat_id):
            for i in messages:
                if messages.index(i) == len(messages) - 1:
                    self.vk.send_message(chat_id, i.format(user[3], user[1], user[2]))
                else:
                    self.vk.send_message(chat_id, i)
                    sleep(1)
            self.__add_change(chat_id, column_call)
            self.db.update_count(column_count, chat_id, user[3])
        else:
            result = self.db.select_call(column_call, chat_id)[0][0]
            result = datetime.fromisoformat(result)
            result = result + timedelta(days=1)
            result = result - datetime.now()
            result = datetime.strptime(str(result), "%H:%M:%S.%f")
            self.vk.send_message(chat_id, f"{name} можно определить через {result.hour}ч:{result.minute}м:{result.second}с")


    def __add_change(self, chat_id, column):
        self.db.update_call_bot(column, chat_id)


    def __check_call(self, column, chat_id):
        result = self.db.select_call(column, chat_id)[0][0]
        check = None
        if datetime.now() < (datetime.fromisoformat(result) + timedelta(days=1)):
            check = False
        else:
            check = True
        return check

    def get_top(self, chat_id, command):
        top, sort_index = command
        users = self.db.get_users(chat_id)
        users.sort(key= lambda x: x[sort_index], reverse=True)
        message = ''
        num = 1
        for i in users:
            word = "раз"
            if i[sort_index] == 2 or i[sort_index] == 3 or i[sort_index] == 4:
                word = 'раза'
            message += f"\n{num}. {i[1]} {i[2]}  -  {i[sort_index]} {word}"
            num += 1
        top = top + message
        self.vk.send_message(chat_id, top)

    def run(self, payload, chat_id):
        if payload in COMMAND_CHOICE:
            self.choice(COMMAND_CHOICE[payload], chat_id)
        elif payload in COMMAND_TOP:
            self.get_top(chat_id, COMMAND_TOP[payload])
        
               