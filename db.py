from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DB():

    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///bot.db', echo=True)
        self.connect = self.engine.connect()

    def add_user(self, first_name, last_name, vk_id, chat_id):
        self.connect.execute(f"INSERT INTO users(first_name, last_name, vk_id, chat_id) VALUES('{first_name}','{last_name}', '{vk_id}', '{chat_id}');")
    
    def get_users(self, chat_id):
        users = self.connect.execute(f"SELECT * FROM users WHERE users.chat_id={chat_id};")
        return list(users)

    def add_chat(self, chat_id):
        self.connect.execute(f"INSERT INTO chat(chat_id) VALUES('{chat_id}');")

    def add_call_bot(self, chat_id):
        self.connect.execute(f"INSERT INTO call_bot(last_call_pid, last_call_pretty, chat_id) VALUES('2000-11-11','2000-11-11','{chat_id}');")