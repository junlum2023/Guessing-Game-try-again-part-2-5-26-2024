import random

def display_title():
    print("Guess the number!")
    print()
    
def play_game(limit):
    number = random.randint(1, limit)
    print(f"I am thinking of a number 1 to {limit}\n")
    count = 1
    guess = int(input("Your guess?:  "))
    
    while(guess != number):
        if guess < number:
            print("Too low")
            count += 1
        elif guess > number:
            print("Too high")
            count +=1
        guess = int(input("Your guess?: "))
    print(f"You guess it in {count} tries.\n")
    
def main():
    display_title()
    again = "yes"
    while again.lower() == "yes":
        limit = int(input("Enteer the limit: "))
        play_game(limit)
        again = input("Would you like to play again? Enter (yes/no)")
        print()
    print("Bye") 
    
if __name__ == "__main__":
    main()
    
    

    