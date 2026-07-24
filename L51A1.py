class node:
    def __init__(self,data):
        self.data = data
        self.prev = None # address of the previous node 
        self.next = None #Address of the next node

class DoublyLL:
    def __init__(self):
        self.head = None
    
    def insert_beg(self,data):
        nb = node(data)
        nb.next = self.head
        self.head = nb

    def insert_end(self,data):
        ne = node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne
        ne.prev = temp

    def display(self):
        if self.head == None:
            print("List is empty ")
        else:
            temp = self.head 
            while temp :
                print(temp.data,"--->",end = " ")
                temp = temp.next

#Drivers code
l = DoublyLL()
n = node(10)
l.head = n
n1 = node(20)
n.next = n1
n2 = node(30)
n1.prev = n
n1.next = n2
l.display()
print(end = "\n")
l.insert_beg(100)
l.display()
print(end = '\n')
l.insert_end(100)
l.display()
