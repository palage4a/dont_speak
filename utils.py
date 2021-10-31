# generate id
def hash(string):
    return sha1(bytes(string, 'utf-8')).hexdigest()
