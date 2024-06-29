def ksa(key, n):
    key_length = len(key)
    S = list(range(2**n))
    j = 0
    for i in range(2**n):
        j = (j + S[i] + key[i % key_length]) % (2**n)
        S[i], S[j] = S[j], S[i]
    return S
def prga(S, n):
    i = 0
    j = 0
    while True:
        i = (i + 1) % (2**n)
        j = (j + S[i]) % (2**n)
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % (2**n)]
        yield K
def rc4(key, plaintext, n):
    key = [int(key[i:i+n], 2) for i in range(0, len(key), n)]
    S = ksa(key, n)
    keystream = prga(S, n)
    result = []
    for i in range(0, len(plaintext), n):
        pt_bits = int(plaintext[i:i+n], 2)
        ks_bits = next(keystream)
        ct_bits = pt_bits ^ ks_bits
        result.append(format(ct_bits, f'0{n}b'))
    return ''.join(result)
def rc4_decrypt(key, ciphertext, n):
    return rc4(key, ciphertext, n)
#key = "101001000001"
key = "1001"
#plaintext = "001010010010"
plaintext = "0101"
n = 2
ciphertext = rc4(key, plaintext, n)
print(f"Ciphertext: {ciphertext}")
decrypted_text = rc4_decrypt(key, ciphertext, n)
print(f"Decrypted text: {decrypted_text}")