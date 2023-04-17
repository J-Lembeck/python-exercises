text = input("Digite uma frase: ")

text = text.replace(" ", "").lower()

if text == text[::-1]:
    print("O texto é um palíndromo.")
else:
    print("O texto não é um palíndromo.")