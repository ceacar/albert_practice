#1. understand what's public key what's private key
#2. write any string to a file
#3. use your host's public key to encrypt a file and then decrypt it and print it out



#please read this:
    #https://en.wikipedia.org/wiki/Public-key_cryptography
#in your terminal, type: pip3 install pycrypto

#read this:
    #AES encryption
    #https://en.wikipedia.org/wiki/Advanced_Encryption_Standard

#read this:
    #RSA encrytption
    #https://en.wikipedia.org/wiki/RSA_(cryptosystem)

#watch this video:
    #https://www.youtube.com/watch?v=8PzDfykGg_g

#now do the assignment


from Crypto.Cipher import AES
import base64
import os


def double_size(input_int):
    return 2*input_int

double_size_short=lambda x: 2*x


def encryption(privateInfo) :
    # anan can do this
    BLOCK_SIZE = 16
    PADDING ='JOJO'


    pad = lambda s: s + (BLOCK_SIZE - len(s) & BLOCK_SIZE) * PADDING

    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    # I WANT YOU TO USE PUBLIC KEY WHICH IS IN ~/.ssh/id_rsa.pub
    secret = os.urandom(BLOCK_SIZE)
    print 'encryption key:', secret

    cipher = AES.new(secret)

    encoded = EncodeAES(cipher, privateInfo)
    print 'Encrypted string:', encoded

#where is the decryption function?
input_string = "1234567890123456"
encryption(input_string)
#i don't believe you can run this script with only a function definition, you even didn't call this function
