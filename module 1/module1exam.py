import hashlib

def calculateHash(sender,reciever,subject,body,nonce):
    string=sender+reciever+subject+body+nonce
    hash=hashlib.sha256(string.encode('utf-8')).hexdigest()
    return hash

def main():
    sender="majeedabdul.941485@gmail.com"
    reciever="umairjavaidmanj@gmail.com"
    subject="sending coins"
    body="21 bitcoins"  
    t1="ff"
    t2="cafa000"  
    print(" _____________________________________________________________________")
    print("|")
    print("|    TASK 1")
    print("|")
    for n in range(99,999):
        nonce=str(n)
        hash=calculateHash(sender,reciever,subject,body,nonce)
        first2=hash[:len(t1)]
        if first2==t1:
            print("|    found 'ff' on nonce value '%s'"%str(n))
            break    
    if first2==t1:
        print("|    "+hash)
    else:
        print("|    Nonce not found")    
    print("|_____________________________________________________________________")
    print("|")
    print("|    TASK 2")
    print("|")
    for n in range(0,99999999):
        nonce=str(n)
        hash=calculateHash(sender,reciever,subject,body,nonce)
        first4=hash[:len(t2)]
        if first4==t2:
            print("|    found '' on nonce value '%s'"%str(n))
            break
    if first4==t2:
        print("|    "+hash)
    else:
        print("|    Nonce not found")
    print("|_____________________________________________________________________")
main()