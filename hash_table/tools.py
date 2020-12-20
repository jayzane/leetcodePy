import hashlib


def get_hash(key, m):
    if key is None:
        return 0
    return int(hashlib.md5(str(key).encode()).hexdigest(), 16) % (m - 1)
