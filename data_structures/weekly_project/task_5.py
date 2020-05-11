import hashlib
import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None

    def add_block(self, new_block):
        # if block chain is empty
        if self.head is None:
            self.head = new_block
            return

        block = self.head
        while block.next:
            block = block.next
        block.next = new_block


block_chain = BlockChain()
block_1 = Block(timestamp=datetime.datetime.utcnow(),
                data="a1",
                previous_hash=None)
block_2 = Block(timestamp=datetime.datetime.utcnow(),
                data="a2",
                previous_hash=block_1.hash)
block_3 = Block(timestamp=datetime.datetime.utcnow(),
                data="a3",
                previous_hash=block_2.hash)
block_4 = Block(timestamp=datetime.datetime.utcnow(),
                data="a4",
                previous_hash=block_3.hash)

block_chain.add_block(block_1)
block_chain.add_block(block_2)
block_chain.add_block(block_3)
block_chain.add_block(block_4)
