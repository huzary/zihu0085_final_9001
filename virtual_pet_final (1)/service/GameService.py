from pojo.pets.Dog import Dog
from pojo.pets.Cat import Cat
from mapper.UserMapper import UserMapper
import time
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)

### Here is the service class of game, it will realize most of service method of game
class GameService:
    def __init__(self):
        self.mapper = UserMapper()
        self.valid_colors = ["black", "white", "brown", "golden", "gray"]

    ### We can choose our pet in this method, choose their name. color and type when we login a account at the first time.
    ### For the second time login or after pet choosing, we will jump to the method pet_menu 
    def choose_pet(self, username):
        user = self.mapper.get_user(username)

        if not user.pet:
            print(f"Hi {username}, choose your pet:")
            name = input("Enter your pet's name: ")

            print("Available colors: " + ", ".join(self.valid_colors))
            color = input("Pet color: ").strip().lower()
            while color not in self.valid_colors:
                print("Invalid color. Choose from: " + ", ".join(self.valid_colors))
                color = input("Pet color: ").strip().lower()

            print("""                        _
                       | \ 
                       | |
                       | |
  |\                   | |
 /, ~\                / /
X     `-.....-------./ /
 ~-. ~  ~              |
    \             /    |
     \  /_     ___\   /
     | /\ ~~~~~   \ |
     | | \        || |
     | |\ \       || )
    (_/ (_/      ((_/
""")
            print('\n')
            print("""              ____
         _mn~~    ~nmm
       _n~           ~Y
     /mn          ,,   ~m
    MMM)         (~~    ~=m__
   (MMMM)        C``        ~~"e=o_
  (MMMMMM                         O)
  MMMMMMM                         0)
  MMMMMMM        C               //
  MMMMMMM__       "~~~        __-`
   MMMMMM ~~\__     v====^^^^""
   MMMMMM    ~]     L
     MMMM    =T=====T=
      ~~~   nn|V~~~~~D
             (~     ~D
            (~        ~D
         _mn~ M         ~D
       (Mnm   M          ~D
      (MnmM   MM         D~
      (m MM   =nnn~~~~nnMMM~XX~nm_
mmmmmmm(MMXMm_    _m ~m___MM_ MM__Mnm_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
            choice = input("Type 'dog' or 'cat': ").strip().lower()
            while True:
                if choice == "dog":
                    pet = Dog(name, color)
                    break
                elif choice== "cat":
                    pet = Cat(name, color)
                    break
                else:
                    print("Unknown pet type. Please choose again!")
                    choice = input("Type 'dog' or 'cat': ").strip().lower()

            user.set_pet(pet.__dict__)
            self.mapper.update_user(user,user.get_username())
            print(f"You adopted a {choice} named {name} with {color} color!")
            print("Loading your pet...")
            pet = self.create_pet_from_data(user.get_pet())
            self.pet_menu(pet, user)
        else:
            print("Loading your pet...")
            pet = self.create_pet_from_data(user.get_pet())
            self.pet_menu(pet, user)

    # We can feed our pets, the hunger value will minus 10, if hunger value already be 0, we can't feed anymore.
    def feed(self,pet):
        hunger=pet.get_hunger()
        if hunger>0:
            pet.set_hunger(hunger-10)    
            print(f"{pet.get_name()} is eating food!")
            print("""    _--"-.
 .-"      "-.
|""--..      '-.
|      ""--..   '-.
|.-. .-".    ""--..".
|'./  -_'  .-.      |
|      .-. '.-'   .-'
'--..  '.'    .-  -.
     ""--..   '_'   :
           ""--..   |
                 ""-'    """)
            jump=input("Push 'Enter' to continue")
        else: 
            print(f"{pet.get_name()} doesn't hungry now!.")

    # We can play with our pet, happiness will add 10, hunger will add 10 and energy will minus 10
    # We can choose this methode only when happiness<100 and energy>0 and hunger<100
    def play(self,pet):
        happiness=pet.get_happiness()
        energy=pet.get_energy()
        hunger=pet.get_hunger()
        if happiness<100 and energy>0 and hunger<100:
            pet.set_happiness(happiness+10)
            pet.set_energy(energy-10)
            pet.set_hunger(hunger+10)
            print(f"{pet.get_name()} is playing now and feeling very happy!")
            if pet.get_type()=='cat':
                print("""        _,'|             _.-''``-...___..--';)
       /_ \'.      __..-' ,      ,--...--'''
      &lt;\    .`--'''       `     /'
       `-';'               ;   ; ;
 __...--''     ___...--_..'  .;.'
(,__....----'''       (,..--''
""")
            else:
                print("""        ,''',_
        ( }  _)
 /=*,  ,'~  =~
!    ,/     )
`\,:'       '
 (       &lt; (
 !   )''' ",\ 
 ) ,/      "_)
&lt; &lt;       /   \ 
 ",)     |     )""")
            jump=input("Push 'Enter' to continue")
        elif happiness==100:
            print(f'The happiness of {pet.get_name()} is already reached the highest value!')
        elif energy==0:
            print(f'{pet.get_name()} wants to sleep now!')
        elif hunger==100:
            print(f'{pet.get_name()} is hungry now! Please feed it.')
       
    ### This method can let pet rest, enery plus 40, happiness minus 20 and hunger minus 20.
    ### Hunger and happiness will never less than 0
    def rest(self,pet):
        happiness=pet.get_happiness()
        energy=pet.get_energy()
        hunger=pet.get_hunger()
        if energy<100:
            pet.set_energy(min(100, energy+40))
            pet.set_happiness(max(0, happiness - 20))
            pet.set_hunger(max(0,hunger-20))
            print(f"{pet.get_name()} is resting now.")
            if pet.get_type()=='cat':
                print("""               /\____/\    __
             .'  ''''  `,-'  `--.__
        __,- :   -  -  ;  " ::     `-. -.__
     ,-sssss `._  `' _,'"     ,'~~~::`.sssss-.
    |ssssss ,' ,_`--'_    __,' ::  `  `.ssssss|
   |sssssss `-._____~ `,,'_______,---_;; ssssss|
    |ssssssssss     `--'~{__   ____   ,'ssssss|
     `-ssssssssssssssssss ~~~~~~~~~~~~ ssss.-'
          `---.sssssssssssssssssssss.---'""")
            else:
                print("""(                   )            \ \ 
 \                 /              \ \ 
  \ _ _ _ _ _ _ _ /             ___) )
           (__)_     ____      /     \ 
              (_)o  /   | \--._)     /
    _______       __|uu | |   \   \_ \ 
   /       \     /      | | __ \  /_) \ 
  /_________\   (_)_____|_|(____)(_____)
""")
            jump=input("Push 'Enter' to continue")
        else:
            print(f"{pet.get_name()} doesn't want to sleep now! Please play with it!")

    ### Let pet wander, energy minus 10 and hunger add 10
    ### You can choose it only when energy>0 and hunger<100
    def wandering(self,pet):
        energy=pet.get_energy()
        hunger=pet.get_hunger()
        if energy>0 and hunger<100:
            pet.set_energy(energy-10)
            pet.set_hunger(hunger+10)
            print(f"{pet.get_name()} is wandering now.")
            if pet.get_type()=='cat':
                print("""        /\_/\         _
       /``   \       / )
       |n n   |__   ( (
      =(Y =.'`   `\  \ \ 
       {`"`        \  ) )     
       {       /    |/ /
        \\   ,(     / /
        ) ) /-'\  ,_.'
       (,(,/ ((,,/
""")
            else:
                print("""           /~~~~~~~~\                            _
    ##\__/ @)      ~~~~~~~~\                     \ \ ) )
    |              /~~\~~~~~                ((    | \   
     \    /           |                          /   |
      (~~~   /         \____________/~~~~~~~~~~~~   /
       ~~~~|~                                     /
           :                                      |
            \                                     |
            |                               /      \ 
             \  \_         :         \     /~~~\    |
             /   :~~~~~|   :~~~~~~~~~~|   :     :   :
            /    :    /    :         /    :    /    :
        (~~~     )(~~~     )     (~~~     )(~~~     )
         ~~~~~~~~  ~~~~~~~~       ~~~~~~~~  ~~~~~~~~
          STOMP     STOMP          STOMP     STOMP
""")
            jump=input("Push 'Enter' to continue")
        elif energy==0:
            print(f'{pet.get_name()} wants to sleep now!')
        elif hunger()==100:
            print(f'{pet.get_name()} is hungry now! Please feed it.')
    
    ### show the status of pet, and it can also tell you what you can do now.
    def status(self,pet):
        print(f'\n State of {pet.get_name()}')
        print(f'Name: {pet.get_name()} Type: {pet.get_type()} Color: {pet.get_color()}')
        print(f'Hunger: {pet.get_hunger()}/100')
        print(f'Happiness: {pet.get_happiness()}/100')
        print(f'Energy: {pet.get_energy()}/100')
        jump=input("Push 'Eneter' for checking what you can do now")
        print("\n What you can do now:")
        if pet.get_hunger()>0:
            print(f"\n You can feed {pet.get_name()}.")
        if pet.get_happiness()<100 and pet.get_energy()>0 and pet.get_hunger()<100:
            print(f"\n You can play with {pet.get_name()}.")
        if pet.get_energy()<100:
            print(f"\n You can ask {pet.get_name()} to rest now.")
        if pet.get_energy()>0 and pet.get_hunger()<100:
            print(f"\n You can let {pet.get_name()} wander now")

    def reset_account(self,user):
        new_username=input("Input your new user name: ")
        new_password=input("Input your new user password: ")
        user.set_username(new_username)
        user.set_password(new_password)


    ### The game menu, you can choose what you want to do here, or quit game
    def pet_menu(self, pet, user):
        while True:
            id=user.get_username()

            print("\nPet Menu")
            print("0. Reset your account")
            print("1. Feed")
            print("2. Play")
            print("3. Rest")
            print("4. Voice")
            print("5. Rename Pet")
            print("6. View Status and check what you can do")
            print("7. Wandering")
            print("8. Back to the menu")

            choice = input("Choose an option: ").strip()
            if choice == "0":
                self.reset_account(user)
                print("Your account has been reset!")
                print(f"Your new username: {user.get_username()}")
                print(f"Your new password: {user.get_password()}")
            elif choice == "1":
                self.feed(pet)
            elif choice == "2":
                self.play(pet)
            elif choice == "3":
                self.rest(pet)
            elif choice == "4":
                if pet.get_type() == "dog":
                    pet.bark()
                elif pet.get_type() == "cat":
                    pet.meow()
            elif choice == "5":
                new_name = input("Enter new name for your pet: ")
                pet.set_name(new_name)
                print(f"Pet renamed to {new_name}.")
            elif choice == "6":
                self.status(pet)
            elif choice == "7":
                self.wandering(pet)
            elif choice == "8":
                print("Exiting game...")
                break
            else:
                print("Invalid choice.")
                continue

            if choice !="6" and choice!="0":
                self.status(pet)
            back=input("\nPush 'Enter' for going back!")
            # update the information to json file
    
            user.set_pet(pet.__dict__)
            self.mapper.update_user(user,id)

    # It will get the inforamtion of pet, and use it to initialize the pet entity every time you login.
    def create_pet_from_data(self, pet_data):
        pet_type = pet_data.get("type", "dog").lower()
        if pet_type == "dog":
            pet = Dog(pet_data["name"], pet_data["color"])
        elif pet_type == "cat":
            pet = Cat(pet_data["name"], pet_data["color"])
        else:
            raise ValueError("Unsupported pet type")

        pet.set_hunger(pet_data.get("hunger", 50))
        pet.set_happiness(pet_data.get("happiness", 50))
        pet.set_energy(pet_data.get("energy", 50))
        return pet