from pojo.pets.Pet import Pet
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)

class Cat(Pet):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.type = "cat"

    # special method of class cat
    def meow(self):
        print(f"{self.name} says Meow!")
        print("""    /\__/\     Meow~ 
   /`    '\ 
 === 0  0 ===   
   \  --  /
  /        \ 
 /          \ 
|            |
 \  ||  ||  /
  \_oo__oo_/#######o
""")
        skip=input("Push 'Enter' to continue")
    def get_type(self):
        return self.type