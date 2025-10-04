class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    def fly(self):
        print("FlyingFish is flying")

    def swim(self):
        print("FlyingFish is swimming")


# Create an instance of FlyingFish
fish = FlyingFish()
fish.fly()  # Output: FlyingFish is flying
fish.swim()  # Output: FlyingFish is swimming