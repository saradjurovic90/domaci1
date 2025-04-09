# Dvostruka olancana lista: dodavanje novog elementa na pocetak

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        if head:
            head.prev = None
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> " if current.next else "")
            current = current.next
        print()
    
    def prepend(self, new_element):
        if not self.head:
            self.head = new_element
            self.tail = new_element
            new_element.prev = None
        else:
            new_element.next = self.head
            new_element.prev = None
            self.head.prev = new_element
            self.head = new_element

# Testiranje funkcije
dll = DoublyLinkedList()
for value in [2, 3, 45, 1]:
    node = Node(value)
    if not dll.head:
        dll.head = node
        dll.tail = node
    else:
        dll.tail.next = node
        node.prev = dll.tail
        dll.tail = node

print("Originalna lista:")
dll.print_list()

dll.prepend(Node(99))
print("Lista nakon dodavanja elementa na početak:")
dll.print_list()
