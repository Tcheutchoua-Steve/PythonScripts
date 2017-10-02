class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
"""
def printQueue ( Queue):
    print(Queue.items)
q = Queue()
q.enqueue('hello')
printQueue(q)
q.enqueue('dog')
printQueue(q)
q.enqueue(3)
printQueue(q)
q.dequeue()
printQueue(q)
"""
