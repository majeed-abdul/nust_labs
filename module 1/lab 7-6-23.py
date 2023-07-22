import hashlib

def hashCal(s1,s2):
    return hashlib.sha256((s1+s2).encode()).hexdigest()

def merkleRoot(s,div):
    arr=[]
    file = s
    with open(file,'rb') as f: 
        File_size = len(f.read()) 
        f.seek(0)
        chunk_size = int(File_size/div-1)
        for i in range(div):    
            file_hash = hashlib.sha256()
            data=f.read(chunk_size)
            file_hash.update(data)
            arr.append(file_hash.hexdigest())

    while len(arr)>1:
        for i in range(int(len(arr)/2)):
            arr[i]=hashCal(arr[i*2],arr[i*2+1])
        for i in range(len(arr)-1,int(len(arr)/2-1),-1):
            arr.pop()
    return arr[0]


mr=merkleRoot("assets/Lab 6-6-2023.pdf",1024)       

print(" ______________________________________________________________________________________")
print("|")
print("|   "+mr)
print("|______________________________________________________________________________________")
print()