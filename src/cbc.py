import binascii
from Crypto.Cipher import AES
from helpers import pad, generateIV, chunkMessage, XOR

blockSize = 16 # bytes

'''
Encrypts message using key with cbc mode.
Appends IV to beginning of ciphertext. If IV isn't provided, one is generated.
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

'''
Decrypts message via cbc with key given the ciphertext generated from encrypt.
cipherText is prepended with the IV created from encrypt.
'''
def decrypt(cipherText, key):
    if (cipherText is None) or (len(cipherText) == 0):
        raise ValueError('cipherText cannot be null or empty')
    cipherText = binascii.unhexlify(cipherText)
    IV, *blocks = chunkMessage(cipherText, blockSize)
    
    plainText = bytes()
    for block in blocks:
        plainText += decryptBlock(block, key, IV)
        IV = block # IV becomes current ciphertext

    # Make output pretty.
    return plainText.decode('utf-8')

'''
Decrypt block via cbc.
'''
def decryptBlock(block, key, IV):
    cipher = AES.AESCipher(key[:32], AES.MODE_ECB)
    return XOR(cipher.decrypt(block), IV)

key = 'abcdefghijklmnopqrstuvwxyz123456' 
m = bytes('Attack at dawn! Attack at dawn! Attack at dawn! Attack at dawn! Attack at dawn! ', 'utf8')
cipherText = encrypt(m, key)
print(cipherText)
plainText = decrypt(cipherText, key)
print(plainText)