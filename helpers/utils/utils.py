def humanify(name: str):
    import re
    return ' '.join(re.split('_+', name)).capitalize()