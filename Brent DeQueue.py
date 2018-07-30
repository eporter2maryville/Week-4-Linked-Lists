# Name: Brent Porter
# GitHub ID: eporter2maryville
# Assignment: 4.3 Create a Dequeue


class Dequeue:
    
    #creates the queue
    def __init__(self):
        self.dequeue=list()
        
    #add an item to the front of the dequeue
    def addRear(self, item):
        #I chose not to allow duplicates for the queue
        if item not in self.dequeue:
          self.dequeue.insert(0,item)
          print(item,'has been added to the rear of your queue!')
          return True
        return False
    
    #add an item to the rear of the dequeue
    def addFront(self,item):
        #no dupes
        if item not in self.dequeue:
            self.dequeue.append(item)
            print(item,'has been added to the front of your queue!')
            return True
        return False
 
    # remove an item from the front of your dequeue
    def removeFront(self):
        if len(self.dequeue)<=0:
            print("There's nothing in your Queue!")
        return self.dequeue.pop()
    
    # remove an item from the rear of your dequeue
    def removeRear(self):
        if len(self.dequeue)<=0:
            print("There's nothing in your Queue!")
        return self.dequeue.pop(0)
    
    # check the number of items in the Queue
    def size(self):
        return len(self.dequeue)
    
def main():
    brentDequeue = Dequeue()
    brentDequeue.addRear(8) #[8]
    brentDequeue.addRear(6) #[6,8]
    brentDequeue.addRear(8) #[6,8]
    brentDequeue.addRear(4) #[4,6,8]
    brentDequeue.addRear(2) #[2,4,6,8]
    brentDequeue.addRear(10) #[10,2,4,6,8]
    
    print(brentDequeue.size()) #5
    
    print(brentDequeue.removeFront()) #removes an item from the front of the queue (8)
    
    print(brentDequeue.removeRear()) #removes an item from the rear of the queue (10)
    
    print(brentDequeue.size()) #3
    
    brentDequeue.addFront(15) # [2,4,6,15]
    
    print(brentDequeue.size()) #4
main()