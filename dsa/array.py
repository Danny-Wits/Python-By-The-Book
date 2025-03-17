# Cirlular Queue

class Cirque:
    def __init__(self, size: int):
        self.array = [0]*size
        self.front = 0
        self.rare = -1

    def enqueue(self, element):
        if self.isFull():
            print("Queue is full")
            return
        self.rare += 1
        self.array[self.rare] = element

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        front = self.array[self.front]
        self.front += 1
        print(front)
        return front

    def isFull(self):
        return len(self.array) == self.rare+1

    def isEmpty(self):
        return self.rare < self.front

    def __str__(self):
        return str(self.array)


queue = Cirque(3)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.enqueue(10)
print(queue)
