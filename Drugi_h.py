# Uklanjanje svakog drugog elementa

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def append(self, new_element):
        if not self.head:
            self.head = new_element
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_element
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> " if current.next else "")
            current = current.next
        print()
    
    def remove_every_second(self):
        if not self.head or not self.head.next:
            return
        
        current = self.head
        count = 1
        
        while current and current.next:
            current.next = current.next.next
            current = current.next
            
# Testiranje funkcije
l1 = LinkedList()
for value in [5, 4, 3, 8, 2]:
    l1.append(Node(value))

print("Originalna lista:")
l1.print_list()

l1.remove_every_second()
print("Lista nakon uklanjanja svakog drugog elementa:")
l1.print_list()
