class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            raise AttributeError

    def insert_right(self, data):
        if self.head is None:
            self.insert_empty(data)
        else:
            c_node = self.head
            while c_node.next:
                c_node = c_node.next
            
            new_node = Node(data)
            c_node.next = new_node
            new_node.previous = c_node
            print('here')

    def insert_left(self, data):
        if self.head is None:
            self.insert_empty(data)
        else:
            new_node = Node(data)
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

    def reverse_list(self):
        if self.head is None:
            raise ValueError
        else:
            placeholder_node = self.head
            q = placeholder_node.next
            placeholder_node.next = None
            placeholder_node.previous = q
            while q:
                q.next = q.previous
                q.previous = placeholder_node
                placeholder_node = q
                q = q.next
            self.head = placeholder_node
                       
    def print_forward(self):
        if self.head:
            c_node = self.head
            while c_node:
                print(c_node.data)
                c_node = c_node.next

if __name__ == '__main__':
    llist = DoubleLinkedList()
    llist.insert_right(1)
    llist.insert_right(2)
    llist.insert_right(3)
    llist.print_forward()
    llist.insert_left(0)
    llist.print_forward()
    llist.reverse_list()