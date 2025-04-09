#fibanacijev broj
def fibonacci(n):
    if n <= 0:
        return "Input mora biti prirodan broj veći od 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test funkcije
print(fibonacci(10))  
