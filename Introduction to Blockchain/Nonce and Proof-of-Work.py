new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

from hashlib import sha256

difficulty = 2
nonce = 0
proof = ""
while(proof[:2] != difficulty*"0"):
    proof = sha256((str(nonce)+str(new_transactions)).encode()).hexdigest()
    #print(proof)
    final_proof = proof
    nonce+=1

print(final_proof)