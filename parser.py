
from config import COMMAND


def get_peer_id(message: dict):
    return message['peer_id']

def get_users(message):
    profiles = message['profiles']
    return profiles