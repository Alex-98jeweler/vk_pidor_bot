from time import strftime, strptime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class DB():

    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///bot.db')
        self.connect = self.engine.connect()

    def add_user(self, first_name, last_name, vk_id, chat_id):
        self.connect.execute(f"INSERT INTO users(first_name, last_name, vk_id, count_pid, count_pretty, chat_id) VALUES('{first_name}','{last_name}', '{vk_id}', 0, 0, '{chat_id}');")
    
    def get_users(self, chat_id):
        users = self.connect.execute(f"SELECT * FROM users WHERE users.chat_id={chat_id};")
        return list(users)

    def add_chat(self, chat_id):
        self.connect.execute(f"INSERT INTO chat(chat_id) VALUES('{chat_id}');")

    def add_call_bot(self, chat_id):
        self.connect.execute(f"INSERT INTO call_bot(last_call_pid, last_call_pretty, chat_id) VALUES('2000-11-11','2000-11-11','{chat_id}');")

    def update_call_bot(self, column: str, chat_id):
        self.connect.execute(f"UPDATE call_bot SET {column}='{datetime.now()}' WHERE call_bot.chat_id={chat_id};")
        
    def select_call(self, column, chat_id):
        result = self.connect.execute(f'SELECT call_bot.{column} FROM call_bot WHERE call_bot.chat_id={chat_id};')
        return list(result)

    def update_count(self, column, chat_id, vk_id):
        self.connect.execute(f"UPDATE users SET {column}={column}+1 WHERE users.chat_id={chat_id} AND users.vk_id={vk_id};")