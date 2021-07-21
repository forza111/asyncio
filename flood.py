
class Dog:
    def __str__(self):
        print('class describe dog')

    def __init__(self,breed):
        self.breed = breed
        print(f"Create Dog {self.breed}")

    def __del__(self):
        print(f"Dog {self.breed} is deleted")


AkitaInu = Dog("AkitaInu")

print(AkitaInu)