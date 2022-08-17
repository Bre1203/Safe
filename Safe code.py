print("Can you open the safe?")
print("Choose 4 numbers from 1,2,3,4 or 5")
print("Here is a hint...you wont use 4")
player = input("Whats the code?: ")


player_code = "5321"

if player == "5321":
    print("You got the code! its " + player_code)
    print("Now you can open the safe!")
else:
    print("Nope! you didn't get the code.")
