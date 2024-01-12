import uuid


def valid_id(id_check):
    """return True if id_check is an uuid valid"""
    try:
        uuid_ok = uuid.UUID(id_check)
    except ValueError:
        return False

    return id_check == str(uuid_ok)
