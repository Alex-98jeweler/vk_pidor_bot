from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

Base = declarative_base()

class Chats(Base):
    __tablename__ = "chat"

    id = Column('id', primary_key=True)
    chat_id = Column('chat_id', Integer)


class Users(Base):
    __tablename__ = 'users'

    id = Column("id", primary_key=True)
    first_name = Column('first_name', String(50))
    last_name = Column('last_name', String(50))
    vk_id = Column('vk_id', Integer)
    chat_id = Column('chat_id', Integer, ForeignKey('chat.id'), nullable=False)

class CallBot(Base):

    __tablename__ = 'call_bot'

    id = Column('id', Integer)
    last_call_pid = Column()