print("🎲🎲 Roll it 13 🎲🎲")

want_instructions = input("Do you want to read the instructions? ").lower()
# loop for testing purposes
while True:



     # checks users enter yes (y) or no (n)
    if want_instructions == "yes":
        print("you choose yes")
    elif want_instructions == "no":
        print("you choose no")
    else:
        print("You did not choose a valid response")
