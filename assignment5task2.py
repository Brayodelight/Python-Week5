class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")


class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")


# Vehicle Subclasses
class Car(Vehicle):
    def move(self):
        return f"🚗 {self.name} is driving on the road"
    
    def honk(self):
        return f"🚗 {self.name} goes Beep Beep!"


class Boat(Vehicle):
    def move(self):
        return f"⛵ {self.name} is sailing on water"
    
    def anchor(self):
        return f"⛵ {self.name} dropped anchor"


class Airplane(Vehicle):
    def move(self):
        return f"✈️ {self.name} is flying through the air"
    
    def takeoff(self):
        return f"✈️ {self.name} is taking off!"


# Animal Subclasses
class Dog(Animal):
    def move(self):
        return f"🐕 {self.name} is running on four legs"
    
    def bark(self):
        return f"🐕 {self.name} says Woof!"


class Fish(Animal):
    def move(self):
        return f"🐟 {self.name} is swimming in water"
    
    def bubble(self):
        return f"🐟 {self.name} blows bubbles"


class Bird(Animal):
    def move(self):
        return f"🐦 {self.name} is flying through the sky"
    
    def chirp(self):
        return f"🐦 {self.name} sings Tweet tweet!"


# Demonstration
def showcase_movement(entities):
    print("\n=== Movement Showcase ===")
    for entity in entities:
        print(entity.move())
        # Demonstrate unique methods if they exist
        if isinstance(entity, Car):
            print(entity.honk())
        elif isinstance(entity, Bird):
            print(entity.chirp())
        print()  # Blank line for spacing


if __name__ == "__main__":
    # Create instances of our classes
    vehicles = [
        Car("Toyota Corolla"),
        Boat("Sea Ray"),
        Airplane("Boeing 747")
    ]
    
    animals = [
        Dog("Buddy"),
        Fish("Nemo"),
        Bird("Tweety")
    ]
    
    # Show movement capabilities
    showcase_movement(vehicles)
    showcase_movement(animals)
    
    # Mix vehicles and animals together
    mixed_entities = [
        Car("Tesla Model S"),
        Bird("Angry Bird"),
        Boat("Yacht"),
        Fish("Dory")
    ]
    
    print("\n=== Mixed Movement ===")
    for entity in mixed_entities:
        action = entity.move()
        print(action)
        # Special actions based on type
        if "flying" in action.lower():
            print("↑↑↑ Look up in the sky! ↑↑↑")
        elif "swimming" in action.lower():
            print("~~~ Splish splash ~~~")