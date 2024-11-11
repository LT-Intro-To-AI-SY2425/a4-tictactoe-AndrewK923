# object oriented programming

# (define-struct dog [fur_color name age favorite_food])
class Dog:
    species = "canis familiaris"
    
    def __init__(self, n , a):
        self.name = n
        self.age = a
        self.fetch_count = 0 
    
    def __str__(self):
        s = f"{self.name} is {self.age} years old" 
        return s
    
    def play_fetch(self, num_fetch):
        self.fetch_count += num_fetch
logan = Dog("Logan", 8)
becker = Dog("Becker", 4)
kepa = Dog("Kepa", 4) 


