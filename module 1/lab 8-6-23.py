from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives.asymmetric import rsa, dsa
from cryptography.hazmat.primitives import hashes

def generateRSAKeyPair():
    privateKey = rsa.generate_private_key(public_exponent=65537,key_size=2048)
    publicKey = privateKey.public_key()
    return privateKey,publicKey

def  RSAEncrypt(publicKey, plainText):
    cipherText = publicKey.encrypt(plainText,PKCS1v15())
    return cipherText

def RSADecrypt(privateKey, cipherText):
    plainText= privateKey.decrypt(cipherText,PKCS1v15())
    return plainText

def generateDSAKeyPair():
    privateKey = dsa.generate_private_key(key_size=1024)
    publicKey = privateKey.public_key()
    return privateKey,publicKey

def DSASign(privateKey, message):
    signature= privateKey.sign(message,hashes.SHA256())
    return signature

def  DSAVerify(publicKey, message,signature):
    try:
        publicKey.verify(signature,message,hashes.SHA256())
        return True
    except:
        return False

def main():
    (RSAprivateKey,RSApublicKey) =  generateRSAKeyPair()             # 1 RSA Generate Public and Private KEy
    message = b"Message for RSA algorithm"                           # 2 
    cipherText = RSAEncrypt(RSApublicKey,message)                    # 3  RSA encrypt TExt
    decryptedText = RSADecrypt(RSAprivateKey,cipherText)             # 4  RSA decrypt text
    print(" ______________________________________________________________________________________")
    print("|")
    print("|   RSA Public Key  : %s"% RSApublicKey)
    print("|   RSA Private Key : %s"% RSAprivateKey)
    print("|   Plain Text      : %s"% message.decode())             # 5 print 
    print("|   Ciphertext      : %s"% cipherText)
    print("|   Decrypted Text  : %s"% decryptedText)
    print("|")
    (DSAPrivateKey,DSAPublicKey) =  generateDSAKeyPair()            # 6 Generate DSA public and private key
    message = b"Message for DSA algorithm"                          # 7
    signature = DSASign(DSAPrivateKey,message)                      # 8
    verified = DSAVerify(DSAPublicKey,message,signature)            # 9
    print("|    DSA DETAILS :")
    print("|    DSA Public Key  : %s"% DSAPublicKey)
    print("|    DSA Private Key : %s"% DSAPrivateKey)
    print("|    Message         : %s"% message.decode())            # 10
    print("|    Signaturer      : %s"% signature)
    print("|    Verifaction     : %s"% verified)
    print("|______________________________________________________________________________________")

main()