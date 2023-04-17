def remove_duplicates(collection):
    return list(set(collection))

collection = [1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 10, 10, "João", "João", "Lembeck"]
new_collection = remove_duplicates(collection)
print(new_collection)
