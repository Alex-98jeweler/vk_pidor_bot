from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

Base = declarative_base()

class Chats(Base):
    __tablename__ = "chat"

    id = Column('id', Integer, primary_key=True)
    chat_id = Column('chat_id', Integer)


class Users(Base):
    __tablename__ = 'users'

    id = Column("id",Integer, primary_key=True)
    first_name = Column('first_name', String(50))
    last_name = Column('last_name', String(50))
    vk_id = Column('vk_id', Integer)
    count_pid = Column('count_pid', Integer, default=0)
    count_pretty = Column('count_pretty', Integer, default=0)
    chat_id = Column('chat_id', Integer, ForeignKey('chat.chat_id'), nullable=False)

class CallBot(Base):

    __tablename__ = 'call_bot'

    id = Column('id', Integer, primary_key=True)
    last_call_pid = Column('last_call_pid', DateTime)
    last_call_pretty = Column('last_call_pretty', DateTime)
    chat_id = Column('chat_id', Integer, ForeignKey('chat.chat_id'))
    