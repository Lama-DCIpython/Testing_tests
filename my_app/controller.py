from my_app import db


def get_client(id_):
    try:
        return db.clients[id_]
    except KeyError:
        return None
