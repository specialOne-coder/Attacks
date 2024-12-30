# README: Blockchain Attack Simulations

## Description
This project contains two Python scripts that simulate potential attacks on blockchain systems using the Proof-of-Stake (PoS) consensus mechanism. These simulations highlight the vulnerabilities of PoS blockchains when specific conditions are exploited by attackers.

---

## 1. **Collision Attack**
### **File: `collision.py`**
### **Description**
This script simulates a hash collision attack, where an attacker exploits weaknesses in a hashing algorithm to find two different inputs that produce the same hash. Such collisions could undermine the integrity of a blockchain by enabling falsification of blocks or transactions.

### **Key Points:**
- Demonstrates the concept of hash collisions using a simplified hashing function (truncated MD5 for illustration).
- Illustrates how such a collision could be exploited in a blockchain context.

### **How It Works:**
- A blockchain is simulated with basic blocks containing data and hashes.
- The script finds a collision by generating random inputs and comparing their hashes until a match is found.

---

## 2. **Economic Dominance Attack**
### **File: `pos_dominance.py`**
### **Description**
This script simulates an economic dominance attack, where a validator with a disproportionate stake in the network exerts excessive influence over block validation. This scenario illustrates how centralization of wealth can compromise the fairness and decentralization of a blockchain.

### **Key Points:**
- A blockchain is simulated with validators having varying stakes (Alice, Bob, and an Attacker).
- Blocks are added using a weighted random selection based on each validator's stake.
- The attacker dominates the block validation process due to their larger stake.

### **How It Works:**
- Blocks are added to the blockchain by selecting validators proportionally to their stakes.
- The script analyzes the percentage of blocks validated by each participant to demonstrate the attacker's dominance.

---

## Prerequisites
- **Python 3.x**
- No external libraries required.

### **Execution**
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Run the desired script:
   ```bash
   python collision.py
   ```
   or
   ```bash
   python pos_dominance.py
   ```

---

## Results
### **Collision Attack:**
You will observe two different inputs producing the same hash value, demonstrating the vulnerability of poorly designed hash functions.

### **Economic Dominance Attack:**
The analysis will show the disproportionate number of blocks validated by the attacker, highlighting how stake centralization undermines decentralization and fairness.

---

## Limitations
- These simulations are simplified and do not reflect the complexity of real-world blockchain implementations.
- Certain optimizations or security mechanisms (e.g., slashing or checkpoints) are not included.

---

## Potential Improvements
1. Add protection mechanisms like slashing or checkpoints to counter these attacks.
2. Simulate attacks in distributed environments or production-level blockchain implementations.
3. Explore vulnerabilities in hybrid consensus mechanisms like PoS/PoW.

---

## Author
This project is designed to illustrate theoretical vulnerabilities in Pow/PoS blockchain systems for educational purposes.
