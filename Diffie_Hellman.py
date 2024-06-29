p = 23
g = 5
xa = 4
ra = int(pow(g, xa, p))
xb = 6
rb = int(pow(g, xb, p))
print("Public Key A:", ra)
print("Public Key B:", rb)
ka = int(pow(rb, xa, p))
kb = int(pow(ra, xb, p))
print("Secret Key A:", ka)
print("Secret Key B:", kb)