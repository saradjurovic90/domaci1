# Prebrojavanje parnih cifara

def count_even_digits(number):
    # Bazni slučaj
    if number == 0:
        return 0
    
    # Uzimanje posljednje cifre
    last_digit = number % 10
    
    # Provjera da li je cifra parna
    is_even = 1 if last_digit % 2 == 0 else 0
    
    # Rekurzivni poziv za ostatak broja
    return is_even + count_even_digits(number // 10)

# Testiranje funkcije
print(count_even_digits(123456))  
print(count_even_digits(13579))   
