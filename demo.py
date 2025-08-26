from abc import ABC, abstractmethod

class CanFly(ABC):
    @abstractmethod
    def fly(self):
        pass

class CanSwim(ABC):
    @abstractmethod
    def swim(self):
        pass

class Pigeon(CanFly):
    def fly(self):
        print("Je suis un PIGEON et je peux VOLER.")

class Duck(CanFly, CanSwim):
    def fly(self):
        print("Je suis un CANARD et je peux VOLER.")
    def swim(self):
        print("Je suis un CANARD et je peux NAGER.")

pigeon = Pigeon()
duck = Duck()

pigeon.fly()
duck.fly()
duck.swim()

bird : CanSwim = pigeon
