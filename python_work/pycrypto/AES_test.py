#AES_test.py
from Crypto.Cipher import AES


#“This is a key123”为 key，长度有着严格的要求，必须为 16、24 或 32 位，否则将会看到下面的错误。
#“This is an IV456”为 VI，长度要求更加严格，只能为 16 位。否则，你将会看到下面的错误。

#加密
obj = AES.new('This is a key123',AES.MODE_CBC,'This is an IV456')
message = "The answer is no"
ciphertext = obj.encrypt(message)
print(ciphertext)

#解秘
obj2 = AES.new('This is a key123',AES.MODE_CBC,'This is an IV456')
s = obj2.decrypt(ciphertext)
print(s)
