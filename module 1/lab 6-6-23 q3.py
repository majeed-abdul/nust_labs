import hashlib

file = "assets/Lab 6-6-2023.pdf"
   
arr1=[]
arr2=[]
arr3=[]

with open(file,'rb') as f: 
    File_size = len(f.read()) 
    f.seek(0) # Move back to beginning of the file
    chunk_size = int(File_size/7)
    for i in range(8):    
        file_hash = hashlib.sha256()
        data=f.read(chunk_size)
        file_hash.update(data)
        arr1.append(file_hash.hexdigest())

for i in range(0,7,2):
    arr2.append(hashlib.sha256((arr1[0+i]+arr1[1+i]).encode()).hexdigest())

for i in range(0,3,2):
    arr3.append(hashlib.sha256((arr2[0+i]+arr2[1+i]).encode()).hexdigest())

final=hashlib.sha256((arr3[0]+arr3[1]).encode()).hexdigest()

print(" ______________________________________________________________________________________")
print("|")
for i in arr1:
    print("|   "+i)
print("|")
for i in arr2:
    print("|   "+i)
print("|")
for i in arr3:
    print("|   "+i)
print("|")
print("|   "+final)
print("|______________________________________________________________________________________")
print()

# |   d59f2df0460af94eb0f5f234634c3dbb731e1222a3aec6d0d187c4a775a65dfc
# |   8723462180d6cdc1e381453fd54f6a3411966e27ea938919624846bd9ffc54dc
# |   30e3eb6d35d14bdfd35d22e98d4e4412467c046d799c3a583500b386c664813c
# |   a867641991a2644bc849f82675f6e053298a40282dcf8c1fe27c1ba997ab0ac2
# |   40bf3e3d44794e7439f3f12c45a51c166d8eeec934cb354c83f73077e6df44fe
# |   a47f3f2d757220400314630f84aae058add76669b2709e450138a32dbb6168a8
# |   0f71be5c945ed627f88765f2bfbe534a84b7143d20e9b6244ecb07e76ed34ca3
# |   e2ca2771fc7c542bcdeeb6065a6e872ff2f2d263a19005b55f63311c0a8f1fa9