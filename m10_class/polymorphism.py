class Dog:
    def run(self):
        print('Dog: run()')
    def walk(self):
        print('Dog: walk()')

class Cat:
    def run(self):
        print('Cat: run()')
    def walk(self):
        print('Cat: walk()')

class Tiger:
    def run(self):
        print('Tiger: run()')
    def walk(self):
        print('Tiger: walk()')

def test(animal):
    animal.run()
    animal.walk()

def main():
    dog = Dog()
    dog.run()
    cat = Cat()
    cat.run()
    tiger = Tiger()
    tiger.run()
    print()

    test(dog)
    test(cat)
    test(tiger)

main()
