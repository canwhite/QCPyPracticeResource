#SHA256_test.py
from Crypto.Hash import SHA256

hash = SHA256.new()
hash.update(b'message')
#h = hash.digest()
h = hash.hexdigest()
print(h)
