class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class SinglyLL:
    def __init__(self):
        self.head = None  

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, target_value): 
        current = self.head
        index = 0
        # Traverse the list until the end is reached
        while current is not None:
            # Compare the data of the current node with the target value
            if current.data == target_value:
                return index  # if found Return the position
            
            # Move to the next node in the sequence
            current = current.next
            index += 1

        return -1  # Target value does not exist in the list

if __name__ == "__main__":
    llist = SinglyLL()

    # 2. Add elements to the linked list
    llist.append(10)
    llist.append(25)
    llist.append(30)
    llist.append(45)
    print("Linked List: 10 -> 25 -> 30 -> 45 -> None")
    # 3. Search for elements
    search_targets = [30, 99]
    for target in search_targets:
        result_index = llist.search(target)
        if result_index != -1:
            print(f"{target} FOUND at index {result_index}.")
        else:
            print(f"{target} NOT FOUND in the list.")
