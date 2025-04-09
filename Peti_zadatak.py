# Dvostruka olancana lista za zadatak sa filmovima

class FilmNode:
    def __init__(self, naziv, zanr, godina, ocjena):
        self.film = {'naziv': naziv, 'zanr': zanr, 'godina': godina, 'ocjena': ocjena}
        self.next = None
        self.prev = None

class DoublyLinkedListFilms:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
    
    def print(self):
        current = self.head
        while current:
            print(f"Naziv: {current.film['naziv']}, Žanr: {current.film['zanr']}, Godina: {current.film['godina']}, Ocjena: {current.film['ocjena']}")
            current = current.next
    
    def append(self, novi_element):
        if not self.head:
            self.head = novi_element
            self.tail = novi_element
        else:
            self.tail.next = novi_element
            novi_element.prev = self.tail
            self.tail = novi_element
    
    def prosjek_by_year(self, year):
        current = self.head
        count = 0
        suma = 0
        
        while current:
            if current.film['godina'] == year:
                count += 1
                suma += current.film['ocjena']
            current = current.next
        
        return suma / count if count != 0 else None
    
    def film_by_year(self, year):
        current = self.head
        while current:
            if current.film['godina'] >= year:
                print(current.film)
            current = current.next
    
    def film_by_zanr(self, zanr):
        current = self.head
        count = 0
        while current:
            if current.film['zanr'] == zanr:
                count += 1
            current = current.next
        return count

# Testiranje funkcije
f1 = FilmNode("Inception", "Sci-Fi", 2010, 8.8)
f2 = FilmNode("The Godfather", "Crime", 1972, 9.2)
f3 = FilmNode("The Dark Knight", "Action", 2008, 9.0)
f4 = FilmNode("Forrest Gump", "Drama", 1994, 8.8)
f5 = FilmNode("Interstellar", "Sci-Fi", 2014, 8.6)

film_lista = DoublyLinkedListFilms()
for film in [f1, f2, f3, f4, f5]:
    film_lista.append(film)

print("Svi filmovi:")
film_lista.print()

print("\nProsječna ocjena filmova iz 2010:")
print(film_lista.prosjek_by_year(2010))

print("\nFilmovi iz 2008 i noviji:")
film_lista.film_by_year(2008)

print("\nBroj Sci-Fi filmova:")
print(film_lista.film_by_zanr("Sci-Fi"))
