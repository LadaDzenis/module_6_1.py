class Animal:

    def __init__(self, name):
        self.name = name
        self.alive = True #живой
        self.fed = False  # накормленный


    def eat(self, food):
        if food.edible == True:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        elif food.edible == False:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Plant:
    edible = False  # съедобность
    def __init__(self, name):
        self.name = name



class Mammal(Animal):
    pass
class Predator(Animal):
    pass
class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True


predator = Predator('Волк с Уолл-Стрит')
mammal = Mammal('Хатико')
flower = Flower('Цветик семицветик')
fruit = Fruit('Заводной апельсин')

print(predator.name)
print(flower.name)

print(predator.alive)
print(mammal.fed)
predator.eat(flower)
mammal.eat(fruit)
print(predator.alive)
print(mammal.fed)
