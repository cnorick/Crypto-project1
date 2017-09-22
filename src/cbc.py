import binascii
from Crypto.Cipher import AES
from helpers import pad

def encrypt(message, key):
    if (message is None) or (len(message) == 0):
        raise ValueError('message cannot be null or empty')
    paddedMessage = pad(message, 16)
    cipher = AES.AESCipher(key[:32], AES.MODE_ECB)
    ciphertext = cipher.encrypt(paddedMessage)
    return binascii.hexlify(bytearray(ciphertext)).decode('utf-8') 

def decrypt(cipherText, key):
    return

m = bytes('abcd', 'utf8')
cipherText = encrypt(m, 'abcdefghijklmnopqrstuvwxyz123456')
print(cipherText)