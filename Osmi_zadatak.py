# Brisanje knjiga sa najvisom i najmanjom cijenom

class BookNode:
    def __init__(self, sifra, naziv, sifra_autora, cijena):
        self.book = {
            'sifra': sifra,
            'naziv': naziv,
            'sifra_autora': sifra_autora,
            'cijena': cijena
        }
        self.next = None
        self.prev = None

class DoublyLinkedListBooks:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
    
    def print(self):
        current = self.head
        while current:
            print(f"Naziv: {current.book['naziv']}, Cijena: {current.book['cijena']}")
            current = current.next
    
    def append(self, novi_element):
        if not self.head:
            self.head = novi_element
            self.tail = novi_element
        else:
            self.tail.next = novi_element
            novi_element.prev = self.tail
            self.tail = novi_element
    
    def remove_highest_and_lowest(self):
        if not self.head or not self.head.next:
            return
        
        # Pronalazak najviše i najniže cijene
        current = self.head
        highest = float('-inf')
        lowest = float('inf')
        
        while current:
            if current.book['cijena'] > highest:
                highest = current.book['cijena']
            if current.book['cijena'] < lowest:
                lowest = current.book['cijena']
            current = current.next
        
        # Uklanjaju se knjige s najvišom cijenom
        current = self.head
        prev = None
        
        while current:
            next_node = current.next
            
            if current.book['cijena'] == highest or current.book['cijena'] == lowest:
                # Ako je to prvi čvor
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                # Ako je to posljednji čvor
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                # Ako je to čvor u sredini
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
            
            current = next_node

# Testiranje funkcije
b1 = BookNode(1, "Knjiga 1", 101, 15.99)
b2 = BookNode(2, "Knjiga 2", 102, 29.99)
b3 = BookNode(3, "Knjiga 3", 103, 9.99)
b4 = BookNode(4, "Knjiga 4", 104, 19.99)
b5 = BookNode(5, "Knjiga 5", 105, 24.99)

book_list = DoublyLinkedListBooks()
for book in [b1, b2, b3, b4, b5]:
    book_list.append(book)

print("Sve knjige:")
book_list.print()

book_list.remove_highest_and_lowest()
print("\nKnjige nakon uklanjanja onih s najvišom i najnižom cijenom:")
book_list.print()
