class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat_1 = Cat('Tom', 2)
cat_2 = Cat('Kitty', 1)
cat_3 = Cat('Miau', 3)

def find_oldest_cat(*args):
    return max(args)

print(f'The oldest cat is {find_oldest_cat(cat_1.age, cat_2.age, cat_3.age)} years old.')