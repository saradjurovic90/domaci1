# Kvadriranje neparnih elemenata

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
    
    def square_odd_elements(self):
        # Nova lista za rezultat
        result_list = LinkedList()
        
        current = self.head
        while current:
            # Ako je element neparan, dodaj njegov kvadrat u novu listu
            if current.value % 2 != 0:
                new_node = Node(current.value ** 2)
                result_list.append(new_node)
            current = current.next
        
        return result_list

# Testiranje funkcije
l1 = LinkedList()
for value in [5, 4, 3, 8, 2]:
    l1.append(Node(value))

print("Originalna lista:")
l1.print_list()

l2 = l1.square_odd_elements()
print("Lista kvadriranih neparnih elemenata:")
l2.print_list()
