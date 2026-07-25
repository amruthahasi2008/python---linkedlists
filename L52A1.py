class node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def searching(self,data):
        t=0
        temp = self.head
        #Traversing the list through temp
        while temp:
            if temp.data == data:
                t=1
                break #break the loop when the element found
            temp = temp.next
        if t==1:
            print("Element found")
        else:
            print("Element not found")
        
    def display(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"--->",end = " ")
                temp = temp.next

#Drivers code
l = DoublyLL()
n = node(10)
l.head = n
n1 = node(20)
n.next = n1
n2 = node(30)
n2.prev = n1
n1.next = n2
l.display()
print(end = "\n")
l.searching(20)

    