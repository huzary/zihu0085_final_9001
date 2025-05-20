import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)
### Parent class of cat and dog
### Include the name, color, hunger happiness and energy of pet
class Pet:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.hunger = 50
        self.happiness = 50
        self.energy = 50

    ### Define the name
    def set_name(self,name):
        self.name=name

    ### Set color of pet
    def set_color(self,color):
        self.color=color

    ### Set hunger
    def set_hunger(self,hunger):
        self.hunger=hunger

    ### Set happiness
    def set_happiness(self,happiness):
        self.happiness=happiness

    ### Set energy
    def set_energy(self,energy):
        self.energy=energy

    ### Get the name
    def get_name(self):
        return self.name
    
    ### Get color
    def get_color(self):
        return self.color
    
    ### Get hunger
    def get_hunger(self):
        return self.hunger
    
    ### Get happiness
    def get_happiness(self):
        return self.happiness
        
    ### Get energy
    def get_energy(self):
        return self.energy

    