import binascii
from Crypto.Cipher import AES
from helpers import generateIV, chunkMessage, XOR, getCtrs, Fk

blockSize = 16 # bytes

def encrypt(message, key, IV = None):
    if (message is None) or (len(message) == 0):
        raise ValueError('message cannot be null or empty')
    if IV is None:
        IV = generateIV(blockSize)
    blocks = chunkMessage(message, blockSize)
    ctrs = getCtrs(IV, len(blocks))

    cipherText = bytes(IV)

    # TODO: parallelize
    for block, ctr in zip(blocks, ctrs):
        cipherText += XOR(block, Fk(ctr, key, True))
    
    # pretty string
    return binascii.hexlify(bytearray(cipherText)).decode('utf-8') 

def decrypt(cipherText, key):
    if (cipherText is None) or (len(cipherText) == 0):
        raise ValueError('cipherText cannot be null or empty')

    #undo the pretty string
    cipherText = binascii.unhexlify(cipherText)

    IV, *blocks = chunkMessage(cipherText, blockSize)
    ctrs = getCtrs(IV, len(blocks))
    
    plainText = bytes()

    # TODO: parallelize
    for block, ctr in zip(blocks, ctrs):
        # encrypt set to True because it's going forward through the cipher.
        plainText += XOR(block, Fk(ctr, key, True))

    # Make output pretty.
    return plainText.decode('utf-8')

key = 'abcdefghijklmnopqrstuvwxyz123456'
m = bytes('Attack at dawn! Attack at dawn! Attack at dawn! Attack at dawn! Attack at dawn! ', 'utf8')
cipherText = encrypt(m, key)
print(cipherText)
plainText = decrypt(cipherText, key)
print(plainText)
