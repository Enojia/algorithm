#!/bash/bin/Python2

alpha = "abcdefghijklmnopqrstuvwxyz"
Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encryptor(key, message):
    crypt_arr = []

    for char in message:
        if char in alpha:
            crypt_arr.append(alpha[(alpha.index(char) + key) % 26])

        elif char in Alpha:
            crypt_arr.append(alpha[(Alpha.index(char) + key) % 26])
        
        else:
            crypt_arr.append(char)

    return "".join(crypt_arr)

crypt_message =  encryptor(2, "Caesar Cipher")
print crypt_message
