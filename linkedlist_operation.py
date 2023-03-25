class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
    #insert at begininning
    def insertAtBeginning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    #insert after
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must in linkedlist")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    #insert at end
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    #Deleting a node
    def deleteNode(self,position):

        if self.head is None:
            return
        
        temp = self.head
        if position ==0:
            self.head = temp.next
            temp = None
            return
        # Find the key to be deleted 
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        # If the key is not present 
         
        if temp is None:
            return 
        
        if temp.next is None:
            return
        
        next = temp.next.next
        temp.next = None
        temp.next = next


    def search(self, key):

        current = self.head

        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False
    
    #Sort the linked list
    def sortLinkedList(self, head):
        current = head
        index = Node(None)

        if head is None:
            return
        else:
            while current is not None:
                # index points to the node next to current 
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data

                    index = index.next
                current = current.next

    #Print the Linked list
    def printList(self):
        temp = self.head
        while(temp):
            print(str(temp.data) +" ", end="")
            temp = temp.next


if __name__ == '__main__':

    lst = LinkedList()
    lst.insertAtEnd(1)
    lst.insertAtBeginning(2)
    lst.insertAtBeginning(3)
    lst.insertAtEnd(4)
    lst.insertAfter(lst.head.next,5)

    print("Linked List:")
    lst.printList()

    print("\nAfter deleting an element: ")
    lst.deleteNode(3)
    lst.printList()

    print()
    item_to_find = 3
    if lst.search(item_to_find):
        print(str(item_to_find), "is found")
    else:
        print(str(item_to_find), "is not found")
    
    lst.sortLinkedList(lst.head)
    print("Sorted List: ")
    lst.printList()