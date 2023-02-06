print(r'''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')

print("Welcome to Treasure Island!")
print("Your mission is to survive the island and find it's hidden treasure.")

crossroad = input("You just landed on the island and are at a crossroad. Where do you want to go? Type \"Left\" or \"Right\" \n").lower()

if crossroad != "left":
    print("You fell into a whole. GAME OVER")
else:
    lake = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. \n").lower()

    if lake != "wait":
        print("You are attacked by a vicious trout. GAME OVER")
    else:
        island = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()

        if island == "red":
            print("You open to door to find a room full of fire and get burned. GAME OVER")
        elif island == "blue":
            print("It is a room full of beasts and you are their next meal. GAME OVER")
        elif island == "yellow":
            print("You have found the treasure! You win!")
        else:
            print ("You chose a door that doesn't exist, sneaky sneaky. GAME OVER")