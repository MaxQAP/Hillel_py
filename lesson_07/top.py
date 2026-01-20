class animal:
    def __init__(self, name: str, age: int, is_alive: bool = True):
        self.name = name
        self.age = age
    def sound(self):
        print('I am animal')

class dog(animal):
    pass

animal = animal = dog(name='animal', age=1, is_alive=True)
dog: animal = dog( name='dog', age=2, is_alive=True)

dog.sound()