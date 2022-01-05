import datetime
import hashlib
import json

# Blockchain class has all the Blockchain's pillars, as the Genesis Block and the main blockchain functions
class Blockchain:
    
    # __init__() function inizializes the Blockchain Class
    def __init__(self):                                        # self is the instance of the class (it's used like "this" in C++)
        self.chain = []                                        # inizializing the chain (as list)
        self.create_block(proof = 1, previous_hash = '0')      # inizializing the Genesis Block of the Blockchain