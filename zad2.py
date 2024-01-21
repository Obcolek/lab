import random

def password():
    char = list(map(chr, range(33, 127)))
    you_password = ''.join(random.choice(char) for _ in range(8))
    return you_password
    
done_password = password()
print("Bezpieczne hasło:", done_password)
