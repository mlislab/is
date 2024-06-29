from sympy import mod_inverse
p = 823
q = 953
e = 313
n = p * q
Pn = (p - 1) * (q - 1)
d = mod_inverse(e, Pn)
print("Decryption Key : ",d)
M = 19070
S = (M ** d) % n
#print("Signature:", S)
M1 = (S ** e) % n
print("Message:", M1)
if M == M1:
    print("As M = M1, Accept the message sent.")
else:
    print("As M not equal to M1, Do not accept the message sent.")