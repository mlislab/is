import hashlib
msg = "bvrit"
res = hashlib.sha512(msg.encode())
print("Hexadecimal equivalent : ",res.hexdigest())