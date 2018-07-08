import uuid

def named_uuid(name):
    return '{}-{}'.format(name,
                          str(uuid.uuid4()))
