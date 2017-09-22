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
Test that unpad correctly reverses pad.
'''
def paddingTest():
    m = bytes('abcde', 'utf8')
    for i in range(1, 11):
        assert m == (unpad(pad(m, i)))
