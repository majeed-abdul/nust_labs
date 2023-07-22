import hashlib

file = "assets/message1.bin" # ---------------------------- message1 md5
file_hash1md5 = hashlib.md5() 
with open(file, 'rb') as f: 
    fb = f.read() 
    file_hash1md5.update(fb) 
    fb = f.read()

file = "assets/message2.bin" # ---------------------------- message2 md5
file_hash2md5 = hashlib.md5() 
with open(file, 'rb') as f: 
    fb = f.read() 
    file_hash2md5.update(fb) 
    fb = f.read() 

file = "assets/message1.bin" # ---------------------------- message1 sha1
file_hash1sha1 = hashlib.sha1() 
with open(file, 'rb') as f: 
    fb = f.read()  
    file_hash1sha1.update(fb) 
    fb = f.read()

file = "assets/message2.bin" # ---------------------------- message2 md5
file_hash2sha1 = hashlib.sha1() 
with open(file, 'rb') as f: 
    fb = f.read()
    file_hash2sha1.update(fb) 
    fb = f.read() 

print(" ______________________________________________________________________________________")
print("|")
print("|  MD5  message1.bin : "+file_hash1md5.hexdigest())
print("|  MD5  message2.bin : "+file_hash2md5.hexdigest())
print("|")
print("|  SHA1  message1.bin : "+file_hash1sha1.hexdigest())
print("|  SHA1  message2.bin : "+file_hash2sha1.hexdigest())
print("|______________________________________________________________________________________")
print()