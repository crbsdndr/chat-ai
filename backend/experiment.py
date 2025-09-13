class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"The name is {self.name} and the color is {self.color}"
    
    @classmethod
    def abstract(cls, name, color):
        return cls(name, color)
        
car1 = Car()
car1.abstract(name="toyota", color="black")
print(car1)