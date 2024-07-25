from random import randint

def guess_app():
    while True:
        player = randint(1, 1000)
        counter = 0
        guess = 0

        print("I have selected a number between 1 and 1000. Try to guess it!")

        while guess != player:
            guess = int(input("Guess my number between 1 and 1000: "))
            if guess < 1 or guess > 1000:
                print("Please, enter a valid number between 1 and 1000")
            else:
                counter += 1
                if guess == player:
                    print("Congratulations, you guessed the number!!!")
                elif guess > player:
                    print("Too high. Try again!!!")
                elif guess < player:
                    print("Too low. Try again!!!")

        if counter < 10:
            print(f"Well done Champ!!!, You made {counter} attempts")
        else:
            print(f"You made {counter} attempts. You can do better next time")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye.")
            break


print(guess_app())
