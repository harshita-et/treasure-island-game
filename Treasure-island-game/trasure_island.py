print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to the Treasure Island")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at the crossroad. Where do you want to go next? "Left" or "Right".').lower()    # We use \' to avoid confusion with single quotes inside the string like in "you're".

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. \nType "wait" to wait for a boat. Type "swim" to swim across.').lower()
  
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose?").lower()
     
        if choice3 == "yellow":
            print("You Win!")
        elif choice3 == "red":
            print("It\'s a room full of fire. Game Over.")
        else:
            print("You enter a room of beasts. Game Over.")

    else:
        print("You get attacked by an angry shark. Game Over.")
else :
     print("You fell in a hole. Game over")