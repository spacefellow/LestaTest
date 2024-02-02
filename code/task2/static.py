class Queue:
    def __init__(self, maxSize):
        self.queue = [None] * maxSize
        self.max_size = maxSize
        self.tail = 0
        self.head = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def push(self, element):
        if self.is_full():
            return 'error'
        self.queue[self.tail] = element
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1
        return self.queue

    def pop(self):
        if self.is_empty():
            return 'error'
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return self.queue
