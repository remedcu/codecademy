from block import Block

class Blockchain:
    def __init__(self):
        self.chain = list()
        self.all_transactions = list()
        self.genesis_block()
    
    def genesis_block(self):
        self.obj = Block(self.all_transactions,hash(0))
        self.chain.append(self.obj)