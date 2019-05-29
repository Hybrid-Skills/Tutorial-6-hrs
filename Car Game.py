i = 1
car_on = False
print('type in "help" if this is your first time')
while i <= 5:
    command = input().lower()
    if command == "start":
        if car_on == False:
            print("Car started... Ready to go")
            car_on = True
        else:
            print("Car is already on.")

    elif command == "stop":
        if car_on == True:
            print("Car stopped.")
            car_on = False
        else:
            print("Car is already off.")

    elif command == "quit":
        want_to_quit = input("Are you sure(Y/N): ")
        if want_to_quit.lower() == "y":
            break
        else:
            print("Yeah nobody likes to leave!")
    elif command == "help":
        print(
"""start - to start the car
stop - to stop the car
quit - to exit""")
    else:
        print("I don't understand that...")
