class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue)<1:
            return "Queue is Empty"
        return self.queue.pop(0)

    #print the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

qu = Queue()

for i in range(0,int(input("Ente the length of your queue: "))):
    qu.enqueue(int(input("Enter the element: ")))

qu.display()
qu.dequeue()
print("After removing a element: ")
qu.display()
