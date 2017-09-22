import binascii
from Crypto.Cipher import AES
from helpers import pad, generateIV, chunkMessage, XOR

blockSize = 16 # bytes

'''
Encrypts message using key with cbc mode.
'''
def encrypt(message, key, IV = None):
    if (message is None) or (len(message) == 0):
        raise ValueError('message cannot be null or empty')
    if IV is None:
        IV = generateIV(blockSize)
    
    cipherText = bytes(IV)

    paddedMessage = pad(message, blockSize)
    blocks = chunkMessage(paddedMessage, blockSize)
    for block in blocks:
        # update the IV to be the newly encrypted ciphertext.
        IV = encryptBlock(block, key, IV)
        print(binascii.hexlify(bytearray(IV)).decode('utf-8'))
        cipherText += IV
    
    # Make the value a pretty string
    return binascii.hexlify(bytearray(cipherText)).decode('utf-8') 

'''
Encrypts a single block using cbc mode.
XORs the message with the IV and passes it through AES.
'''
def encryptBlock(block, key, IV):
    xoredMessage = XOR(block, IV)
    cipher = AES.AESCipher(key[:32], AES.MODE_ECB)
    ciphertext = cipher.encrypt(xoredMessage)
    return bytes(ciphertext)

def decrypt(cipherText, key):
    return

m = bytes('abcd', 'utf8')
cipherText = encrypt(m, 'abcdefghijklmnopqrstuvwxyz123456')
print(cipherText)