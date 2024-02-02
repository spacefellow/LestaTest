class Queue:
    def __init__(self, maxSize):
        self.queue = []
        self.max_size = maxSize

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def push(self, element):
        if self.is_full():
            return 'error'
        self.queue.append(element)
        return self.queue

    def pop(self):
        if self.is_empty():
            return 'error'
        self.queue.pop(0)
        return self.queue
