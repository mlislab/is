def encrypt(plaintext,key):
    key_length=len(key)
    key_as_int=[ord(i) for i in key]
    plaintext_int=[ord(i) for i in plaintext]
    ciphertext=''
    for i in range(len(plaintext_int)):
        value=(plaintext_int[i]+key_as_int[i % key_length])%26
        ciphertext+=chr(value+65)
    return ciphertext
def decrypt(ciphertext,key):
    key_length=len(key)
    key_as_int=[ord(i) for i in key]
    ciphertext_int=[ord(i) for i in ciphertext]
    plaintext=''
    for i in range(len(ciphertext_int)):
        value=(ciphertext_int[i]-key_as_int[i % key_length])%26
        plaintext+=chr(value+65)
    return plaintext
if __name__=="__main__":
    Message=input("Enter the message: ")
    key=input("Enter the key: ")
    encrypt_text=encrypt(Message,key)
    print("Encypted message: ",encrypt_text)
    print("Decrypted message: ",decrypt(encrypt_text,key))