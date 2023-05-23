

class Dog:
    """One of the objects to be returned"""

    def speak(self):
        return "Woof!"
    
    def __str__(self):
        return "Dog"
    
class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """Returns a dog object"""
        return Dog

    def get_food(self):
        """Returns a dog food object"""
        return "Dog Food!"
    
class PetStore:
    """PetStore houses our abstract factory"""

    def __init__(self, pet_factory=None):
        """pet_factory is our abstract factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects returned"""
        pet = self._pet_factory.get_pet()()
        pet_food = self._pet_factory.get_food()

        print(f"Our pet is {pet}!")
        print(f"Our pet says hello by {pet.speak()}")
        print(f"Its food is {pet_food}!")


#Create a concrete factory
factory = DogFactory()

#Create a pet store housing our Abstract Factory
shop = PetStore(factory)

#Invoke the utility method to show the details of our pet
shop.show_pet()