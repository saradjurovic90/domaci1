# Provjera palindroma

def is_palindrome(s):
    # Bazni slučajevi
    if len(s) <= 1:
        return True
    
    # Provjera prvog i posljednjeg karaktera
    if s[0] != s[-1]:
        return False
    
    # Rekurzivni poziv za ostatak stringa
    return is_palindrome(s[1:-1])

# Testiranje funkcije
print(is_palindrome("radar"))  
print(is_palindrome("zdravo"))  
