import hashlib

s1="we"
s2="rt"
s3="yu"
s4="ui"
s5="ui"
s6="ms"
s7="s7"
s8="ir"

h1=hashlib.sha256(s1.encode('utf-8')).hexdigest() 
h2=hashlib.sha256(s2.encode('utf-8')).hexdigest()
h3=hashlib.sha256(s3.encode('utf-8')).hexdigest()
h4=hashlib.sha256(s4.encode('utf-8')).hexdigest()
h5=hashlib.sha256(s5.encode('utf-8')).hexdigest()
h6=hashlib.sha256(s6.encode('utf-8')).hexdigest()
h7=hashlib.sha256(s7.encode('utf-8')).hexdigest()
h8=hashlib.sha256(s8.encode('utf-8')).hexdigest()

A=hashlib.sha256((h1+h2).encode('utf-8')).hexdigest()
B=hashlib.sha256((h3+h4).encode('utf-8')).hexdigest()
C=hashlib.sha256((h5+h6).encode('utf-8')).hexdigest()
D=hashlib.sha256((h7+h8).encode('utf-8')).hexdigest()

X=hashlib.sha256((A+B).encode('utf-8')).hexdigest()
Z=hashlib.sha256((C+D).encode('utf-8')).hexdigest()

final=hashlib.sha256((X+Z).encode('utf-8')).hexdigest()

print(" __________________________________________________________________________________________")
print("|")
print("|                                 Merkle Root")
print("|    SHA-256 : "+final)
print("|__________________________________________________________________________________________")
print()