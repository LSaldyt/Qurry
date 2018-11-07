import uuid

def named_uuid(name):
    # Create a named label, which is very useful in jump instructs and other control-flow
    return '{}-{}'.format(name,
                          str(uuid.uuid4()))
