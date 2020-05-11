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
        hash_str = self.data.encode('utf-8')
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

block = block_chain.head

# print all blocks
while block.next:
    print(block.timestamp)
    print(block.data)
    print(block.previous_hash)
    print(block.hash)
    print("\n")
    block = block.next

print(block.timestamp)
print(block.data)
print(block.previous_hash)
print(block.hash)


"""
Answer:
2020-05-11 14:23:18.381751
a1
None
f55ff16f66f43360266b95db6f8fec01d76031054306ae4a4b380598f6cfd114


2020-05-11 14:23:18.381941
a2
f55ff16f66f43360266b95db6f8fec01d76031054306ae4a4b380598f6cfd114
2c3a4249d77070058649dbd822dcaf7957586fce428cfb2ca88b94741eda8b07


2020-05-11 14:23:18.381947
a3
2c3a4249d77070058649dbd822dcaf7957586fce428cfb2ca88b94741eda8b07
f46dd28a5499d8efef0b8fb8ee1ec1c5a5e407c9381741d576ba8deb4f59ec3f


2020-05-11 14:23:18.381950
a4
f46dd28a5499d8efef0b8fb8ee1ec1c5a5e407c9381741d576ba8deb4f59ec3f
4539e4b4889079c2a00afeae0bfc1439840ef2379a1fb81c8ba27361ad476d6b

"""