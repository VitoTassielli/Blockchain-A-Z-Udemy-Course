import datetime
import hashlib
import json

# Blockchain class has all the Blockchain's pillars, as the Genesis Block and the main blockchain functions
class Blockchain:
    
    # __init__() function inizializes the Blockchain Class
    def __init__(self):                                        # self is the instance of the class (it's used like "this" in C++)
        self.chain = []                                        # inizializing the chain (as list)
        self.create_block(proof = 1, previous_hash = '0')      # inizializing the Genesis Block of the Blockchain


    # create_block() function return a block passed the proof (found by the miner) and the previous_hash (to link the new block at the blockchain)
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}

        self.chain.append(block)
        return block   


    # get_previous_block() function return previous block of the blockchain
    def get_previous_block(self):
        return self.chain[-1]