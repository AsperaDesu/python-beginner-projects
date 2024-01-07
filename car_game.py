print("Car Game")
print("--------")

command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car has already started\n")
        else:
            started = True
            print("the car is starting...\n")
    elif command == "stop":
        if not started:
            print("cas has already stopped\n")
        else:
            started = False
            print("car stopped.\n")
    elif command == "help":
        print("""
start - start the car
stop - stop the car
quit - exit the game
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand.\n")

