class Queue:

  def __init__(self):
    self.queue = []

  def enqueue(self, data):
    self.queue.append(data)
  
  def dequeue(self):
    return self.queue.pop(0) if self.queue else None
  
  def front(self):
    return self.queue[0]
  
  def isEmpty(self):
    return len(self.queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.front())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.isEmpty())
