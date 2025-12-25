import random


class CircularBuffer:
    def __init__(self, capacity):
        self._capacity = capacity
        self._buffer = []
        self._position = 0

    def append(self, item):
        if len(self._buffer) < self._capacity:
            self._buffer.append(item)
        else:
            self._buffer[self._position] = item
        self._position = (self._position + 1) % self._capacity

    def get_sample(self, batchsize):
        return random.sample(self._buffer, batchsize)

    def __len__(self):
        return len(self._buffer)
