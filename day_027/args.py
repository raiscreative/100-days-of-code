def add(*args): # tuple
    print(args[0])

    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 7, 11, 13, 8))


def calculate(n, **kwargs): # dictionary
    for key, value in kwargs.items():
        print(key, value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add = 3, multiply = 5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get('make') # kw['make]
        self.model = kw.get('model') # kw['model]
        self.colour = kw.get('colour')

my_car = Car(make='Nissan', model= 'GT-8')
print(my_car.model)