import random

# Block structure
class Block:
    def __init__(self, index, previous_hash, validator, data):
        self.index = index
        self.previous_hash = previous_hash
        self.validator = validator
        self.data = data

    def __repr__(self):
        return f"Block(index={self.index}, validator={self.validator}, data={self.data})"

# Blockchain structure
class Blockchain:
    def __init__(self):
        self.chain = []
        self.validators = {"Alice": 40, "Bob": 30, "Attacker": 100}  # Stakes in tokens
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", "System", "Genesis Block")
        self.chain.append(genesis_block)

    def select_validator(self):
        total_stake = sum(self.validators.values())
        pick = random.uniform(0, total_stake)
        cumulative = 0
        for validator, stake in self.validators.items():
            cumulative += stake
            if pick <= cumulative:
                return validator

    def add_block(self, data):
        validator = self.select_validator()
        previous_hash = self.chain[-1].index if self.chain else "0"
        new_block = Block(len(self.chain), previous_hash, validator, data)
        self.chain.append(new_block)
        return new_block

    def print_chain(self):
        for block in self.chain:
            print(block)

# Simulate the Blockchain
blockchain = Blockchain()
print("Initial Blockchain:")
blockchain.print_chain()

# Add blocks and simulate validator selection
print("\nSimulating block additions:")
for i in range(10):
    new_block = blockchain.add_block(f"Transaction {i+1}")
    print(f"Added {new_block}")

# Analyze validator dominance
print("\nValidator dominance analysis:")
validator_count = {validator: 0 for validator in blockchain.validators.keys()}
for block in blockchain.chain[1:]:  # Skip genesis block
    validator_count[block.validator] += 1

for validator, count in validator_count.items():
    print(f"{validator} validated {count} blocks ({(count / len(blockchain.chain) * 100):.2f}%)")
