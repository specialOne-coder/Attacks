import hashlib
import random
import string

# Simple Block structure
class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.hash = self.compute_hash()

    def compute_hash(self):
        data_to_hash = f"{self.index}{self.previous_hash}{self.data}"
        return hashlib.sha256(data_to_hash.encode()).hexdigest()

# Simple Blockchain
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", "Genesis Block")
        self.chain.append(genesis_block)

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, data)
        self.chain.append(new_block)

# Simulating a simple blockchain
blockchain = Blockchain()
blockchain.add_block("Block 1 Data")
blockchain.add_block("Block 2 Data")
blockchain.add_block("Block 3 Data")

# Print the blockchain
for block in blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Data: {block.data}")
    print(f"Hash: {block.hash}\n")

# Simulating an attack: Finding a collision in the hash
# Simplified hash for illustration purposes
def simplified_hash(data):
    return hashlib.md5(data.encode()).hexdigest()[:6]  # Using MD5 and truncating to 6 characters

# Finding a collision
print("\nFinding a collision...")
found = False
hash_dict = {}

while not found:
    random_data = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    hash_value = simplified_hash(random_data)
    
    if hash_value in hash_dict:
        print(f"Collision found!\nData 1: {hash_dict[hash_value]}\nData 2: {random_data}\nHash: {hash_value}")
        found = True
    else:
        hash_dict[hash_value] = random_data
