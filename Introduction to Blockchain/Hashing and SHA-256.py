from hashlib import sha256

text = "I am excited to learn about blockchain" #Add a "!" at the end of 'blockchain' for the last Instruction in Codecademy

obj = sha256(text.encode())
hash_result = obj

print(hash_result.hexdigest())