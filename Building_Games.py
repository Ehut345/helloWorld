#Building a Guessing Game
sceret_number = 9
guess_count = 0
max_guesses = 3
while guess_count < max_guesses:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == sceret_number:
        print("You won!")
        break
else:
    print("Sorry you failed!")
#Building the Car Game
command = ""
is_started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if is_started:
            print("Car is already started ...")
        else:
            is_started = True
            print("Car started ...")
    elif command == "stop":
        if not is_started:
            print("Car is already stopped ...")
        else:
            is_started = False
            print("Car stopped ...")
    elif command == "quit":
        break
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to end the game
        """)
    else:
        print("Sorry, I don't understand that ! ...")