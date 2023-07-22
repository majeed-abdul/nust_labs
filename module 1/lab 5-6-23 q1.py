import hashlib

file = "../Lab5-6-2023.pdf" # Location of the file (can be set a different way)

file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
with open(file, 'rb') as f: # Open the file to read it's bytes
    fb = f.read() # Read from the file. Take in the amount declared above 
    file_hash.update(fb) # Update the hash
    fb = f.read() # Read the next block from the file

print(" ______________________________________________________________________________________")
print("|")
print("|  SHA-256   program : "+file_hash.hexdigest())
print("|  SHA-256   online  : c27783392976304d9ec296c6cf318f4145e780d02b78c679347e93408553a59c")
print("|______________________________________________________________________________________")
print()