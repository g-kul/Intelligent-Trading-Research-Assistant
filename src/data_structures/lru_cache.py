# class lru cache


class Node:
    def __init__(self, url, content):
        self._url = url
        self._content = content
        self._prev = None
        self._next = None


class LRUCache:
    def __init__(self, capacity):
        self._capacity = capacity
        self._cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head._next = self.tail
        self.tail._prev = self.head

    def _add(self, node):
        _head_next = self.head._next
        node._next = _head_next
        node._prev = self.head

        self.head._next = node
        _head_next._prev = node

    def _remove(self, node):
        _next_node = node._next
        _prev_node = node._prev

        _prev_node._next = _next_node
        _next_node._prev = _prev_node

    def get(self, url):
        if url in self._cache:
            node = self._cache[url]
            self._remove(node)
            self._add(node)
            return node._content
        return None

    def put(self, url, content):
        if url in self._cache:
            self._remove(self._cache[url])

        node = Node(url, content)
        self._add(node)
        self._cache[url] = node

        if len(self._cache) > self._capacity:
            lru_node = self.tail._prev
            self._remove(lru_node)
            del self._cache[lru_node._url]
