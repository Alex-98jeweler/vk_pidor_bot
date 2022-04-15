

def get_peer_id(message: dict):
    return message['peer_id']

def get_users(message):
    try:
        profiles = message['profiles']
    except:
        pass
    return profiles