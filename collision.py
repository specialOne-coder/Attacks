import hashlib
import random
import string

# Block structure
class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.hash = self.compute_hash()

    def compute_hash(self):
        data_to_hash = f"{self.index}{self.previous_hash}{self.data}"
        return hashlib.md5(data_to_hash.encode()).hexdigest()[:6]  # Truncated MD5 for demonstration purposes

# Blockchain structure
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

    def print_chain(self):
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}\n")

# Simulating the Blockchain
blockchain = Blockchain()
blockchain.add_block("Block 1 Data")
blockchain.add_block("Block 2 Data")
blockchain.add_block("Block 3 Data")

print("\n--- Blockchain ---\n")
blockchain.print_chain()

# Collision Attack Simulation within Blockchain
print("\n--- Simulating Collision Attack ---\n")

def find_collision_in_blockchain(blockchain):
    for block in blockchain.chain:
        print(f"Testing collisions for Block {block.index}...")
        original_hash = block.hash
        found = False
        while not found:
            # Generate random data and compute hash
            random_data = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            test_hash = hashlib.md5(f"{block.index}{block.previous_hash}{random_data}".encode()).hexdigest()[:6]

            if test_hash == original_hash and random_data != block.data:
                print(f"Collision found for Block {block.index}!\n")
                print(f"Original Data: {block.data}\nRandom Data: {random_data}\nHash: {original_hash}\n")
                found = True

# Execute the collision attack simulation
find_collision_in_blockchain(blockchain)
