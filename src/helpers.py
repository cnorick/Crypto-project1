import random

'''
pads message to be a multiple of blocksize.
message is a byte array.
'''
def pad(message, blockSize):
    if (message is None) or (len(message) == 0):
        raise ValueError('message cannot be null or empty')
    if type(message) is not bytes:
        raise ValueError('message must be bytes')
    message = bytearray(message)
    paddingNeeded = blockSize - (len(message) % blockSize)

    paddedMessage = message[:]
    for i in range(paddingNeeded):
        paddedMessage.append(paddingNeeded)

    return bytes(paddedMessage)

'''
Unpads a message padded by calling pad().
message must be a byte array.
'''
def unpad(message):
    if type(message) is not bytes:
        raise ValueError('message must be a bytes')
    message = bytearray(message)
    numPadding = message[-1]
    return bytes(message[:-numPadding])

'''
Generates n pseudorandom bytes.
'''
def generateIV(n):
    if n < 1:
        raise ValueError('n must be greater than 0')
    return bytes(random.getrandbits(8) for _ in range(n))

'''
Divides message into chunks of size n. The last message may be shorter than n.
'''
def chunkMessage(message, n):
    return [message[i:i+n] for i in range(0, len(message), n)]

'''
bitwise XORs m1 and m2.
'''
def XOR(m1, m2):
    return bytes(a ^ b for a, b in zip(m1, m2))

'''
Test that unpad correctly reverses pad.
'''
def paddingTest():
    m = bytes('abcde', 'utf8')
    for i in range(1, 11):
        assert m == (unpad(pad(m, i)))