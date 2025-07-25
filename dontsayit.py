import random
speak = ["Don't you say it!", "Don't you dare!", "Don't you dare say it!", "The consequences are dire if you do!", "You better not!"]
def main():
    gameIsDone = False
    while not gameIsDone:
        textbox = input(random.choice(speak) + " ").strip().lower()
        if "the game" in textbox:
            print("You said it!")
            gameIsDone = True
main()