# Stepenovanje broja

def power(x, n):
    # Bazni slučaj
    if n == 0:
        return 1
    
    # Rekurzivni poziv
    return x * power(x, n - 1)

# Testiranje funkcije
print(power(3, 3))  
print(power(2, 4)) 
