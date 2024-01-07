
def play():
    ui = input("> ")
    started = False
    if ui == "start":
        if not started:
            print("The car is starting...")
            started = True
        else:
            print("The car has already started!")
    elif ui == "stop":
        if started:
            print("The car is stopping")
            started = False
        else:
            print("The car has already stopped!")
        
play()

