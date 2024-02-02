from collections import deque

class Queue:
    def __init__(self, maxSize):
        self.queue = deque(maxlen=maxSize)
        self.max_size = maxSize

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return  len(self.queue) == self.max_size

    def push(self, elem):
        if self.is_full():
            return 'error'
        self.queue.append(elem)
        return self.queue

    def pop(self):
        if self.is_empty():
            return 'error'
        self.queue.popleft()
        return self.queue
