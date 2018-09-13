from blockchain import Blockchain

new_transactions = "fake_transactions"

my_blockchain = Blockchain()
my_blockchain.add_block(new_transactions)
print(my_blockchain.print_blocks())

print(my_blockchain.validate_chain())