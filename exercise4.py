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






choice = ''
message = ''
choice = ''

while choice != 0:
    choice = input("\nEnter 1 to encrypt and 2 to decrypt")

    if choice == '1':
        message = input("\nEnter Message: ")
        for i in range(0, len(message)):
            result = result + chr(ord(message[i] - 2)

        print(result + '\n\n')
        result = ''

    elif choice == '2'
        message = input("\nEnter Message: ")
        for i in range(0,len(message)):
            result = result + chr(ord(message[i]) + 2)

        print(result + '\n\n')
        result = ''
