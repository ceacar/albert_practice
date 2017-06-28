from Crypto.Cipher import AES
import base 64
import os

def decryption(encryptedString):
    PADDING = 'JOJO'
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    key = ''
    cipher = AES.new(key)
    decoded = DecodeAES(cipher, encryptedstring)
