with open("names.txt", "r", encoding="utf-8") as file:
    names = file.read().splitlines()

    frequency_name = {}

    for name in names:
        if name in frequency_name:
            frequency_name[name] += 1
        else:
            frequency_name[name] = 1

    print("Frequência dos nomes:")
    for name, frequency in frequency_name.items():
        print(f"{name}: {frequency} vezes")
