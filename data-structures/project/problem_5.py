import hashlib
from datetime import datetime
import unittest

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.next = None
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(timestamp, data, previous_hash)

    def calc_hash(self, timestamp, data, previous_hash):
        sha = hashlib.sha256()
        string = str(timestamp) + str(data) + str(previous_hash)
        hash_str = string.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:

    def __init__(self, data):
        self._add_first_block(data)

    def add_block(self, data):
        if not self.head:
            self._add_first_block(data)
            return
        timestamp = self._get_utc_time()
        last_block = self.tail
        self.tail.next = Block(timestamp, data, last_block.hash)
        self.tail = self.tail.next
    def _get_utc_time(self):
        return datetime.utcnow()

    def _add_first_block(self, data):
        timestamp = self._get_utc_time()
        new_block = Block(timestamp, data, 0)
        self.head = new_block
        self.tail = new_block
        
class problem_5_tests(unittest.TestCase):

    def test1(self):
        blockchain = Blockchain('some data')
        self.assertEquals(blockchain.tail.data, 'some data')
        blockchain.add_block('some more data')
        self.assertEquals(blockchain.tail.data, 'some more data')

    def test2(self):
        blockchain = Blockchain('some data')
        self.assertEquals(blockchain.tail.data, 'some data')

    def test3(self):
        blockchain = Blockchain('some data')
        self.assertEquals(blockchain.tail.data, 'some data')
        blockchain.add_block('some more data')
        self.assertEquals(blockchain.tail.data, 'some more data')
        blockchain.add_block('yet more data')
        self.assertEquals(blockchain.tail.data, 'yet more data')

if __name__ == '__main__':
    unittest.main()