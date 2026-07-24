class Node:
    def __init__(self,data):
        self.data = data
        self.next = None #Address of the next node

class SinglyLL:
    def __init__(self):
        self.head = None
    def swap(self,n1,n2):
        prevNode1 = None
        prevNode2 = None
        node1 = self.head
        node2 = self.head

        #Checks if list is empty
        if(self.head == None):
            return
        #if n1 and n2 are equal the list will create the same
        if (n1==n2):
            return
        #Search for node 1
        while (node1 != None and node1.data != n1):
            prevNode1 = node1
            node1 = node1.next

        #Search for node 2
        while (node2 != None and node2.data != n2):
            prevNode2 = node2
            node2 = node2.next
        
        if (node1!= None and node2 != None):

            #if previous node to node1 is not none then it will point to node 2
            if (prevNode1 != None):
                prevNode1.next = prevNode2
            else:
                self.head = node2
        
        #If previous node to node2 is not none then it will point to node 1
            if (prevNode2 != None):
                prevNode2.next = prevNode1
            else:
                self.head = node1
            #Swaps the next nodes of node1 and node2
            temp = node1.next
            node1.next = node2.next
            node2.next = temp
        else:
            print("Swapping is not possible")

    def display(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp :
                print(temp.data,'- -',end = " ")
                temp = temp.next

l = SinglyLL()
n =Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
l.display()
print(end = '\n')
l.display()
print(end = '\n')
l.Swap(10,30)
l.display()


            
            


        
        