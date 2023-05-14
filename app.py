command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is alredy started")
        else:
            started = True
        print("Car started ...")
    elif command == "stop":
        if not started:
            print("Car is alredy stoped")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
               start - to start the car
               stop - to stop car
               quit - to quit
               """)
    elif command == "quit":
        break
    else:
        print("Sorry")
