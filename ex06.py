import random
import string

def generate_password(tamanho=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(tamanho))
    return password

passowrd_size = 10
password = generate_password(passowrd_size)
print("Senha:", password)