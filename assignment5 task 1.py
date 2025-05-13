class Superhero:
    """Base class representing a superhero"""
    
    def __init__(self, name, secret_identity, powers, base_of_operations):
        """Initialize superhero attributes"""
        self.name = name
        self.secret_identity = secret_identity  # Encapsulated attribute
        self._powers = powers                  # Protected attribute
        self.base_of_operations = base_of_operations
        self._health = 100                     # Private attribute
    
    def use_power(self):
        """Use the superhero's powers"""
        return f"{self.name} uses {self._powers[0]}!"
    
    def take_damage(self, damage):
        """Reduce health points"""
        self._health -= damage
        if self._health <= 0:
            return f"{self.name} has been defeated!"
        return f"{self.name} has {self._health} health remaining"
    
    def heal(self, amount):
        """Restore health points"""
        self._health = min(100, self._health + amount)
        return f"{self.name} healed to {self._health} health"
    
    def get_secret_identity(self):
        """Getter for encapsulated attribute"""
        return "Classified" if self.secret_identity else "Unknown"
    
    def __str__(self):
        """String representation of the superhero"""
        return (f"Superhero: {self.name}\n"
                f"Powers: {', '.join(self._powers)}\n"
                f"Base: {self.base_of_operations}")


class Avenger(Superhero):
    """Subclass representing Avengers with additional capabilities"""
    
    def __init__(self, name, secret_identity, powers, base_of_operations, avenger_level):
        """Initialize Avenger-specific attributes"""
        super().__init__(name, secret_identity, powers, base_of_operations)
        self.avenger_level = avenger_level
        self._tech = []  # Additional private attribute
    
    def add_tech(self, technology):
        """Add technology to the Avenger's arsenal"""
        self._tech.append(technology)
        return f"{self.name} added {technology} to their tech"
    
    def use_power(self):  # Method overriding (polymorphism)
        """Avengers have special power usage"""
        return f"Avenger {self.name} unleashes {self._powers[0]} with level {self.avenger_level} intensity!"
    
    def assemble(self):
        """Avenger-specific method"""
        return f"{self.name} answers the Avengers' call!"
    
    def __str__(self):  # Method overriding
        """Enhanced string representation"""
        base_info = super().__str__()
        return (f"{base_info}\n"
                f"Avenger Level: {self.avenger_level}\n"
                f"Tech: {', '.join(self._tech) if self._tech else 'None'}")


# Demonstration
if __name__ == "__main__":
    # Create a regular superhero
    spidey = Superhero(
        name="Spider-Man",
        secret_identity="Peter Parker",
        powers=["Web-slinging", "Spider-sense", "Wall-crawling"],
        base_of_operations="Queens, NY"
    )
    
    # Create an Avenger (inherits from Superhero)
    iron_man = Avenger(
        name="Iron Man",
        secret_identity="Tony Stark",
        powers=["Powered armor", "Genius intellect", "Weapons systems"],
        base_of_operations="Stark Tower",
        avenger_level=10
    )
    iron_man.add_tech("Repulsor Beams")
    iron_man.add_tech("J.A.R.V.I.S. AI")
    
    # Demonstrate functionality
    print("--- Regular Superhero ---")
    print(spidey)
    print(spidey.use_power())
    print(spidey.take_damage(30))
    print(spidey.heal(15))
    print(f"Secret Identity: {spidey.get_secret_identity()}\n")
    
    print("--- Avenger ---")
    print(iron_man)
    print(iron_man.use_power())  # Polymorphism in action
    print(iron_man.assemble())  # Avenger-specific method
    print(iron_man.take_damage(20))
    print(f"Tech: {iron_man._tech}")  