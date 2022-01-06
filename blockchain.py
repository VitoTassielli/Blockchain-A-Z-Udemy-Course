import datetime
import hashlib
import json
from flask import Flask

# Part 1
# Blockchain class has all the Blockchain's pillars, as the Genesis Block and the main blockchain functions
class Blockchain:
    
    # __init__() function inizializes the Blockchain Class
    def __init__(self):                                        # self is the instance of the class (it's used like "this" in C++)
        self.chain = []                                        # inizializing the chain (as list)
        self.create_block(proof = 1, previous_hash = '0')      # inizializing the Genesis Block of the Blockchain


    # create_block() function returns a block passed the proof (found by the miner) and the previous_hash (to link the new block at the blockchain)
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}

        self.chain.append(block)
        return block   


    # get_previous_block() function returns previous block of the blockchain
    def get_previous_block(self):
        return self.chain[-1]


    # proof_of_work() function returns the proof (if found it) of the mined block
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        # In this blockchain it's not used the hash of the whole block, but it's set a different challenge called hash_operation.
        # The operation cannot be symmetrical and for this reason it's been excluded the sum operation.

        # Increment new_proof with the while loop at one time it will be equal to an old proof and that will set a deadlock while looking for new different proofs':
        # the sequential blocks will alternate the two found proofs.

        # Example: block1 has proof=10 and we are looking for block2's proof.
        # We found new_proof=5 and the sum operation new_proof+previous_proof=15 and its hash has the 4 leading zero, so new_proof=5 is correct.

        # Now we have to look for block3's proof, so previous_proof=5. At the time when new_proof=10 the operation sum new_proof+previous_proof=15,
        # exactly LIKE BEFORE and its hash has the 4 leading zero.
        # So we found block1_proof=10, block2_proof=5 e block3_proof=10. It's evident that looking for block4's proof we'll found new_proof=5 e so on.
        
        # We'll have a deadlock between the two found proofs. With subtraction operation we don't have this problem
        # (we set the square operation to make the challenge a bit more difficult)

        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()  #hexdigest() makes the correct hash format
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1

        return new_proof


    # hash() takes input a block and returns its SHA256 hash
    def hash(self, block):

        # We have to convert the block's dictionary to a string, in order to make its hash
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    
    # is_chain_valid() checks that the blockchain has a valid chain. A chain is not valid if:
    # - if a block has a wrong previous_block value in its dictionary
    # OR
    # - if a block has a fake proof which doesn't the request of inizial 4 leading zero
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            # First check
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False

            # Second check
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()  
            if hash_operation[:4] != '0000':
                return False

            # Incrementing
            previous_block = block
            block_index += 1
        return True



#Part2 - Mining out Blockchain
# Creating a Web App
app = Flask(__name__)

# Creating a Blockchain
blockchain = Blockchain()