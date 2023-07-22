from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

def generateECDSAKeyPair():
    privateKey = ec.generate_private_key(ec.SECP256K1())
    publicKey = privateKey.public_key()
    return privateKey,publicKey

def ECDSASign(privateKey, message):
    signature = privateKey.sign(message,ec.ECDSA(hashes.SHA256()))
    return signature

def ECDSAVerify(publicKey, message, signature):
    try:
        publicKey.verify(signature, message, ec.ECDSA(hashes.SHA256()))
        return True
    except:
        return False

def main():
    (ECDSAPrivateKey,ECDSAPublicKey)=generateECDSAKeyPair()     
    message=b"Message for ECDSA algorithm"                      
    signature=ECDSASign(ECDSAPrivateKey,message)                
    verified=ECDSAVerify(ECDSAPublicKey,message,signature)      
    print(" ______________________________________________________________________________________")
    print("|")
    print("|                              ECDSA ")
    print("|   ECDSA Public Key  : %s"% ECDSAPublicKey)
    print("|   ECDSA Private Key : %s"% ECDSAPrivateKey)
    print("|   Message           : %s"% message.decode())
    print("|   Signature         : %s"% signature)
    print("|   Verifaction       : %s"% verified)
    print("|______________________________________________________________________________________")
    
main()