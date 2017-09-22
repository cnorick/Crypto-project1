import random
from Crypto.Cipher import AES

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
Fk is a pseudorandom function keyed on <key>. It takes message as input
and outputs its encrypted ciphertext if <encrypt> is true. Otherwise it
pushes the ciphertext back through the pseudorandom function and outputs the plaintext.
'''
def Fk(input, key, encrypt = True):
    cipher = AES.AESCipher(key[:32], AES.MODE_ECB)
    if encrypt:
        return bytes(cipher.encrypt(input))
    else:
        return bytes(cipher.decrypt(input))

'''
Creates n CTRs starting at IV and incrementing by one each time.
'''
def getCtrs(IV, n):
    if type(IV) is not bytes:
        raise ValueError('IV must be bytes')
    IVasInt = int.from_bytes(IV, 'big')
    return [i.to_bytes(len(IV), 'big') for i in range(IVasInt, IVasInt + n)]


'''
Test that unpad correctly reverses pad.
'''
def paddingTest():
    m = bytes('abcde', 'utf8')
    for i in range(1, 11):
        assert m == (unpad(pad(m, i)))