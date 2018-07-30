class Queue:
    
    #creates the queue
    def __init__(self):
        self.queue=list()
        
    #add an item to the front of the queue
    def enqueue(self, item):
        #I chose not to allow duplicates for the queue
        if item not in self.queue:
          self.queue.insert(0,item)
          print(item,'has been added to your queue!')
          return True
        return False
 
    # remove an item from the front of your queue
    def dequeue(self):
        if len(self.queue)<=0:
            print("There's nothing in your Queue!")
        return self.queue.pop()
    
    # check the number of items in the Queue
    def size(self):
        return len(self.queue)
    
def main():
    brentQueue = Queue()
    brentQueue.enqueue(8) #[8]
    brentQueue.enqueue(6) #[6,8]
    brentQueue.enqueue(8) #[6,8]
    brentQueue.enqueue(4) #[4,6,8]
    brentQueue.enqueue(2) #[2,4,6,8]
    brentQueue.enqueue(10) #[10,2,4,6,8]
    
    print(brentQueue.size()) #5
    
    print(brentQueue.dequeue()) #removes an item from the front of the queue (8)
    
    print(brentQueue.size()) #4
    
main()