from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
import hashlib
import random

def generateTxid():
    randInt=random.randint(1,1000000)
    sha256Hash=hashlib.sha256(randInt).digest()
    return str(sha256Hash)

def generateInput():
    preTxid=generateTxid()
    prevOutputIndex=random.randint(0,5)
    return preTxid,prevOutputIndex

