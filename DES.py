#pycryptodome
from Crypto.Cipher import DES
key = input("Enter a key:")

if len(key) != 8:
    # raise ValueError("The key should be of length 8")
    print("The length of the key should be 8")
    exit()

plaintext = input("Enter plain text:")

if len(plaintext) % 8 != 0 :
    print("The length of plaintext should be a multiple of 8")
    exit()

cipher = DES.new(key.encode(),DES.MODE_ECB)

encrypted = cipher.encrypt(plaintext.encode())
print("encrypted text",encrypted.hex())

decrypted = cipher.decrypt(encrypted)
print("decryped text",decrypted.decode())