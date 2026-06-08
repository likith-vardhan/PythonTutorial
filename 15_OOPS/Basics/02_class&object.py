class Dog:
    # __init__ is the constructor — runs automatically when object is created
    def __init__(self, name, breed, age):
        # Instance attributes — unique to each object
        self.name = name      # 'self' refers to THIS specific object
        self.breed = breed
        self.age = age

    # Instance method — a behavior the dog can perform
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

    def info(self):
        print(f"Name: {self.name}, Breed: {self.breed}, Age: {self.age}")


# Creating objects
dog1 = Dog("Buddy", "Labrador", 3)
dog2 = Dog("Max", "German Shepherd", 5)

# Using methods
dog1.bark()    # Buddy says: Woof! Woof!
dog2.bark()    # Max says: Woof! Woof!

dog1.info()    # Name: Buddy, Breed: Labrador, Age: 3
dog2.info()    # Name: Max, Breed: German Shepherd, Age: 5

# Accessing attributes directly
print(dog1.name)   # Buddy
print(dog2.age)    # 5

