import math
import mmh3
from bitarray import bitarray


# Bloom filter class
class BloomFilter:
    def __init__(self, expected_items=1000000, fp_rate=0.01):
        self._arr_size = int(
            -((expected_items * math.log(fp_rate)) / (math.log(2) ** 2))
        )
        self._hash_count = int((self._arr_size / expected_items) * math.log(2))
        self.bit_array = bitarray(self._arr_size)
        self.bit_array.setall(0)

    def add(self, url):
        for i in range(self._hash_count):
            digest = mmh3.hash(url, seed=i)
            index = digest % self._arr_size
            self.bit_array[index] = 1

    def lookup(self, url):
        for i in range(self._hash_count):
            digest = mmh3.hash(url, seed=i)
            index = digest % self._arr_size

            if self.bit_array[index] == 0:
                return False

        return True
