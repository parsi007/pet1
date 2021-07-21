class VirtualPet:
    """Implements virtual pet"""
    def __init__(self,name):
        #Attribues
        self.name = name
        self.hunger = 50
        print("I have been born! My name is {0}".format(name))
        
    #Methods
    def talk(self):
        print("Hello, I am {0}!".format(self.name))
        if self.hunger <= 20:
            print("I am feeling full!")
        elif self.hunger <= 50:
            print("I am a bit hungry.")
        elif self.hunger <= 80:
            print("I am hungry.")
        elif self.hunger <= 100:
            print("I am very hungry! Feed me quickly!")
                  
    def feed(self,food):
        eaten = False
        if food in ["bread","1"]:
            self.hunger -= 10
            eaten = True
        elif food in ["cake","2"]:
            self.hunger -= 30
            eaten = True
        elif food in ["carrot","2"]:
            self.hunger -= 5
            eaten = True
        elif food in ["meat","2"]:
            self.hunger -= 20
            eaten = True
        if eaten:
            print("That was delicious!")
        else:
            print("I don't want to eat that.")
        
def menu_options():
    print()
    print("What do you want to do with your pet?")
    print()
    print("1. Talk to your pet")
    print("2. Feed your pet")
    print("9. Finish interacting with your pet")
    
    
if __name__ == "__main__":
    pet_one = VirtualPet(input("What would you like to call your pet: "))
    done = False
    foods = ["Bread","Cake","Carrot","Meat"]
    while not done:
        menu_options()
        choice = input("\nWhat would you like to do next: \n").lower()
        if choice in ["talk","1"]:
            pet_one.talk()
        elif choice in ["feed","2"]:
            print("Your pet will eat:")
            for count in range(len(foods)):
                print("{0}. {1}".format(count+1,foods[count]))
            pet_one.feed(input("\nWhat would you like to feed your pet: \n").lower())
        elif choice in ["done","finish","9"]:
            done = True
