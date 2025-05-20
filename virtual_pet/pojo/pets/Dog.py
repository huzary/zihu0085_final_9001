from pojo.pets.Pet import Pet
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)

class Dog(Pet):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.type = "dog"

    # special method of class dog
    def bark(self):
        print(f"{self.name} says Woof!")
        print("""                                  ____
                           .--"~~"    ~"\___
                          Y              ]  ~~"\    WOOF! 
                          l   `v.,_    _/'      ]
                           \   |   7~~"        /'
                            \  |  / /~"------"~
                          __.} l_/-^-&lt;-.
                     .--"~      Y     I Y
                    /           l    oj-&lt;______
                   Y       _     ~---~   (   ^ Y
                   l       |~t-.__(    // \.__.^
                    \      | |    ~\      _.^
                     "-._  | |      "---"~
                         Y |-^----------..,__
       .                 | |--.,__   --.,__  ~"-.
       \\                | l l    "~--.,_  ~--.  \ 
        \\    _____      |  \ \___,      "-._    /
         \&gt;-"~     ~"-.--j   ~----/          "--"
         /        ,--.           Y
       _Y_ /     (    )     ___  |_
    ,-~   "       "--"     "   ~-&lt; ~-.
   /                    Y         \   \ 
  /          /     .    l          Y  )Y
 /     l    /-.____l    !\,      ) ! / /
Y    / /"--" /      \__/' \     / /_K-~
`\__K-"\__.-"              ^.__K-'""")
    
    def get_type(self):
        return self.type