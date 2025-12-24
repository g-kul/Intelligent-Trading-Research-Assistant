# Class Priority queue class


class PriorityQueue:
    def __init__(self):
        self._heap = []

    def push(self, priority, item):
        _element = (priority, item)
        self._heap.append(_element)
        self._heapify_up((len(self._heap) - 1))

    def pop(self):
        if self._is_empty():
            raise ValueError("The list is empty no values available!!!")

        if len(self._heap) == 1:
            return self._heap.pop()

        _head_element = self._heap[0]
        self._heap[0] = self._heap[-1]
        self._heap.pop()
        self._heapify_down(0)
        priority, item = _head_element

        return item

    def peek(self):
        if not self._is_empty():
            _head_element = self._heap[0]
            return _head_element

    def _is_empty(self):
        return len(self._heap) == 0

    def _heapify_up(self, index):
        while index > 0:
            _parent_index = (index - 1) // 2

            if self._heap[index] < self._heap[_parent_index]:
                self._heap[index], self._heap[_parent_index] = (
                    self._heap[_parent_index],
                    self._heap[index],
                )
                index = _parent_index
            else:
                break

    def _heapify_down(self, index):
        while True:
            left_child_index = (2 * index) + 1
            right_child_index = (2 * index) + 2
            smallest = index

            if (
                left_child_index < len(self._heap)
                and self._heap[left_child_index] < self._heap[smallest]
            ):
                smallest = left_child_index
            if (
                right_child_index < len(self._heap)
                and self._heap[right_child_index] < self._heap[smallest]
            ):
                smallest = right_child_index
            if smallest is not index:
                self._heap[index], self._heap[smallest] = (
                    self._heap[smallest],
                    self._heap[index],
                )
                index = smallest
            else:
                break
