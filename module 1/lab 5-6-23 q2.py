import hashlib

file = "assets/Lab5-6-2023.pdf"
file_hash = hashlib.sha256()
with open(file, 'rb') as f: 
    fb = f.read()
    file_hash.update(fb) 
    fb = f.read()

print(" ____________________________________________________________________________________________")
print("|")
print("|  SHA-256   before change : c27783392976304d9ec296c6cf318f4145e780d02b78c679347e93408553a59c")
print("|  SHA-256   after  change : "+file_hash.hexdigest())
print("|____________________________________________________________________________________________")
print()