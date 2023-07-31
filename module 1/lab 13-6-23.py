from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
import hashlib
import random

def generateTxid():
    randInt=random.randint(1,1000000)
    sha256Hash=hashlib.sha256(str(randInt).encode()).hexdigest()
    return str(randInt)

def generateInput():
    preTxid=generateTxid()
    prevOutputIndex=str(random.randint(0,5))
    return preTxid,prevOutputIndex

def generateOutput():
    recipientAddress = 'recipient_address_' + str(random.randint(1,100))
    randomInt=random.randint(1,1000)/1000
    amount = str(round(randomInt,8))
    return recipientAddress,amount

def  generateTransactionFee():
    randomInt=random.randint(1,10)/10000
    transectionFee=str(round(randomInt,8))
    return transectionFee

def generateRandomTransaction():
    txid = generateTxid()
    inputPrevTxid, inputPrevOutputIndex = generateInput()
    outputRecipientAddress, outputAmount = generateOutput()
    transactionFee = generateTransactionFee()
    return txid, inputPrevTxid, inputPrevOutputIndex,outputRecipientAddress,outputAmount,transactionFee

def concatenateString(txid, inputPrevTxid,inputPrevOutputIndex, outputRecipientAddress,outputAmount, transactionFee):
    transactionData = txid+inputPrevTxid+str(inputPrevOutputIndex)+outputRecipientAddress+outputAmount+transactionFee
    return transactionData

def generateECDSAKeyPair():
    ECDSAPrivateKey = ec.generate_private_key(ec.SECP256K1())
    ECDSAPublicKey = ECDSAPrivateKey.public_key
    return ECDSAPrivateKey, ECDSAPublicKey

def ECDSASign(privateKey, message):
    signature = privateKey.sign(message,ec.ECDSA(hashes.SHA256()))
    return signature

def ECDSAVerify(publicKey, message,signature):
    try:
        publicKey.verify(signature, message,ec.ECDSA(hashes.SHA256()))
        return True
    except:
        return False
    
def main():
    txid, inputPrevTxid, inputPrevOutputIndex,outputRecipientAddress, outputAmount,transactionFee = generateRandomTransaction()
    transactionDataAsMessage =concatenateString(txid, inputPrevTxid,inputPrevOutputIndex, outputRecipientAddress,outputAmount, transactionFee).encode()
    transactionDataAsMessageSHA256Hashed = hashlib.sha256(transactionDataAsMessage).digest()
    ECDSAPrivateKey, ECDSAPublicKey = generateECDSAKeyPair()
    signature = ECDSASign(ECDSAPrivateKey,transactionDataAsMessageSHA256Hashed)
    verified = ECDSAVerify(ECDSAPublicKey,transactionDataAsMessageSHA256Hashed,signature)
    print(" ______________________________________________________________________________________")
    print("|")
    print("|   ECDSA Public Key   : %s"% ECDSAPublicKey.__format__)
    print("|   ECDSA Private Key  : %s"% ECDSAPrivateKey)
    print("|   TransectionDataHash: %s"% transactionDataAsMessageSHA256Hashed)    
    print("|   Signature          : %s"% signature)
    print("|   Verification       : %s"% str(verified))
    print("|______________________________________________________________________________________")
    print()

main()