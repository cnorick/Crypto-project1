import binascii
from Crypto.Cipher import AES

'''
pads message to be a multiple of blocksize.
message is a byte array.
'''
def pad(message, blockSize):
    if (message is None) or (len(message) == 0):
        raise ValueError('input text cannot be null or empty set')

    paddingNeeded = blockSize - (len(message) % blockSize)

    paddedMessage = message[:]
    for(i in range(paddingNeeded)):
        paddedMessage.append(bytes(paddingNeeded))

    return paddedMessage

def unpad(message):
    return