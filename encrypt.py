from Crypto.Cipher import DES

key = b'abcdefgh'


def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text


des = DES.new(key, DES.MODE_ECB)
text = b'Python rocks!'
padded_text = pad(text)

encrypted_text = des.encrypt(padded_text)
print(encrypted_text)

print (des.decrypt(encrypted_text))
