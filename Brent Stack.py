# Name: Brent Porter
# GitHub ID: eporter2maryville
# Assignment: 4.1 Create a Stack


class Stack:
    
    #creates the stack
    def __init__(self):
        self.stack=list()
        
    #add an item to the stack
    def push(self, item):
        #I chose to allow duplicates
        self.stack.append(item)
        print(item, " has been added to the stack")
 
    # remove an item from the stack
    def pop(self):
        if len(self.stack)<=0:
            print("There's nothing in your stack!")
        return self.stack.pop()
    
    # checking what the top item is without removing it
    def peek(self):
        if len(self.stack)<=0:
            print("There's nothing in your stack!")
        return self.stack[-1]
    
    # check the number of items in the stack
    def size(self):
        return len(self.stack)
    
def main():
    brentStack = Stack()
    brentStack.push('Manna Manna')
    brentStack.push('Do')
    brentStack.push('Doo')
    brentStack.push('Da')
    brentStack.push('DoDo')
    
    print('\n',brentStack.size())
    
    print('\n',brentStack.peek())
    
    brentStack.pop()
    
    print('\n',brentStack.peek())
    
    print('\n',brentStack.size())
    
main()