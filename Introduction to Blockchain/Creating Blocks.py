import datetime

print(datetime.datetime.now()) #If an error is shown
#Use the below line (without "#") of code first to avoid that error. It is an error from Codecademy's part.
#print(datetime.now())

class Block:
    def __init__(self,transactions,previous_hash):
    	self.transactions = transactions
    	self.previous_hash = previous
    	self.nonce = 0
    	self.timestamp = datetime.datetime.now()