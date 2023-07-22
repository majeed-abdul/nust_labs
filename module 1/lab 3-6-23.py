import hashlib
import bcrypt

str="MAJEED"  
# -------------  RIPEMD-160
h = hashlib.new('ripemd160')
h.update(str.encode('utf-8'))
rm=h.hexdigest()

# -------------- BCRYPT
bcryptt=bcrypt.hashpw(str.encode('utf-8'), bcrypt.gensalt())  

print()
print()
print(" ________________________________________________________")
print("|")
print("|                    "+str)
print("|")
print("| MD5      : "+hashlib.md5(str.encode('utf-8')).hexdigest())
print("| SHA-1    : "+hashlib.sha1(str.encode('utf-8')).hexdigest())
print("| SHA-256  : "+hashlib.sha256(str.encode('utf-8')).hexdigest())
print("| SHA-512  : "+hashlib.sha512(str.encode('utf-8')).hexdigest())
print("| SHA3-256 : "+hashlib.sha3_256(str.encode('utf-8')).hexdigest())
print("| SHA3-512 : "+hashlib.sha3_512(str.encode('utf-8')).hexdigest())
print("| BLAKE2   : "+hashlib.blake2b(str.encode('utf-8')).hexdigest()) 
print("| RIPEMD   : "+rm)
print("|")
print(bcryptt)
print("|_______________________________________________________")
print()