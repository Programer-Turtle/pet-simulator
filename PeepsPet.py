import random
import time

def load_save_data():
    try:
        with open("SaveData\health.txt", "r") as saved_health:
            health = int(saved_health.read())
        with open("SaveData\hunger.txt", "r") as saved_hunger:
            hunger = int(saved_hunger.read())
        with open("SaveData\happiness.txt", "r") as saved_happiness:
            happiness = int(saved_happiness.read())
        return health, hunger, happiness
            
    except:
        with open("SaveData\health.txt", "w") as saved_health:
            saved_health.write("20")
        with open("SaveData\hunger.txt", "w") as saved_hunger:
            saved_hunger.write("5")
        with open("SaveData\happiness.txt", "w") as saved_happiness:
            saved_happiness.write("5")
        
        #returns defaults
        return 20, 5, 5
    
def reset_data():
    with open("SaveData\health.txt", "w") as saved_health:
            saved_health.write("20")
    with open("SaveData\hunger.txt", "w") as saved_hunger:
            saved_hunger.write("5")
    with open("SaveData\happiness.txt", "w") as saved_happiness:
            saved_happiness.write("5")
    
    print("Data Reset!")

def Save_Data(health, hunger, happiness):
    with open("SaveData\health.txt", "w") as saved_health:
            saved_health.write(str(health))
    with open("SaveData\hunger.txt", "w") as saved_hunger:
            saved_hunger.write(str(hunger))
    with open("SaveData\happiness.txt", "w") as saved_happiness:
            saved_happiness.write(str(happiness))

def cycle(health, hunger, happiness):
    drop_chance = random.randint(0, 10)
    hunger_chance = random.randint(0, 10)
    happiness_chance = random.randint(0, 10)

    #changes values if should
    if drop_chance == hunger_chance:
        hunger -= 2

    if drop_chance == happiness_chance:
        happiness -= 2

    #if variables under zero reset to zero
    hunger = max(hunger, 0)
    happiness = max(happiness, 0)

    #lowers health
    if hunger == 0 or happiness == 0:
        health -= 5

    Save_Data(health, hunger, happiness)

    #checks if health is under zero
    if health == 0:
        print("X  X")
        print("____")
        time.sleep(3)
        reset_data()
        health , hunger, happiness = 20, 5, 5

    return health, hunger, happiness
        

def feed(hunger):
    hunger += 2
    if hunger > 5:
        hunger = 5
    print(f"Hunger is {hunger}.")
    return hunger

def play(happiness):
    counter = 0
    answer = random.randint(1, 10)

    while counter < 6:
        print("Guess a number between 1 and ten")
        guess = int(input())

        if guess == answer:
            print("yay:]")
            happiness +=2
            if happiness > 5:
                happiness = 5
            print(f"Happiness is {happiness}")
            return happiness
        
        elif guess < answer:
            print("Number is higher")
        
        else:
            print("Number is lower")
        counter += 1
    print("You Failed :{")
    return happiness
    

def checkcommand(command, health, hunger, happiness):
    if command == 1:
        hunger = feed(hunger)

    elif command == 2:
        happiness = play(happiness)

    elif command == 3:
        print("One cycle passed.")
    
    elif command == 4:
        print(f"Health:{health} Hunger:{hunger} Happiness:{happiness}")

    elif command == 5:
        reset_data()
        health , hunger, happiness = 20, 5, 5

    return health, hunger, happiness

def main():
    health, hunger, happiness = load_save_data()
    while True:
        print("1 Feed. 2 play. 3 idle. 4 data. 5 reset.")
        try:
            user_command = int(input())
            if user_command > 6 or user_command < 1:
                print("Invalid Command!")
                continue

            health, hunger, happiness = cycle(health, hunger, happiness)
            health, hunger, happiness = checkcommand(user_command, health, hunger, happiness)

        except:
            print("Must be number!")

if __name__ == "__main__":
    main()