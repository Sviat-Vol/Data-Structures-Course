""" Stack Implementation using Queues """

from collections import deque

class Stack:
    """
    Stack class made on queue
    """
    def __init__(self):
        self.queue = deque()
    def push(self, x):
        """
        Add element to top
        """
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
    def pop(self):
        """
        Return top object
        """
        return self.queue.popleft()
    def top(self):
        """
        Get top element
        """
        return self.queue[0]
    def empty(self):
        """
        Check whether stack is empty
        """
        return len(self.queue) == 0
