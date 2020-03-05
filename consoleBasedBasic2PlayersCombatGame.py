import random

def namecoin():  # The main function where everything loops in.
    while True:
        firstheroask = raw_input("----- First Hero -----" + "\n" + "Please type your hero's name: ")  # Asks first player to define his/her name.
        if firstheroask == "" or firstheroask == " ":  # The condition for the situation when user types nothing.
            continue
        else:
            while True:
                secondheroask = raw_input("----- Second Hero -----" + "\n" + "Please type your hero's name: ")  # Asks second player to define his her name.
                if secondheroask == "" or secondheroask == " ":  # The condition for the situation when user types nothing.
                    continue
                elif secondheroask == firstheroask:  # If given usernames are the same asks the question below.
                    print str(secondheroask), "is taken, please choose another name!"
                    continue
                else:
                    restart(firstheroask, secondheroask)  # Calss the "restart" function.
                break  # Exits the seoond while loop to prevent turning the second user name defining part if user wants to play the game again.
        break  # Exits the first while loop to prevent turning all the way back if user wants to play the game again.


def restart(firstHeroAsk, secondheroask):  # This is the function decides which player will start first.
    hp1 = 100
    hp2 = 100
    cointoss = [firstHeroAsk, secondheroask]  # Ehe elements for random.choice function to choose.
    result = random.choice(cointoss)  # the cointoss process.
    print "Coin toss result:", result, "starts first!"
    if result == firstHeroAsk:  # The condition for cointoss result equals to firsthero's name.
        print firstHeroAsk, (61 - len(firstHeroAsk)) * " " + secondheroask, "\n", "HP[" + str(hp1) + "]:", str(hp1 / 2 * "|"), 1 * " ", "HP[" + str(hp2) + "]:", str(hp2 / 2 * "|")
        # Prints the begining health bar.
        attackstart(firstHeroAsk, secondheroask, result, hp1, hp2, firstHeroAsk, secondheroask)  # Calls the attackstart function.
    elif result == secondheroask:  # The condition for cointoss result equals to secondhero's name.
        print secondheroask, (61 - len(secondheroask)) * " " + firstHeroAsk, "\n", "HP[" + str(hp2) + "]:", str(hp2 / 2 * "|"), 1 * " ", "HP[" + str(hp1) + "]:", str(hp1 / 2 * "|")
        # prints the begining health bar.
        attackstart(secondheroask, firstHeroAsk, result, hp1, hp2, firstHeroAsk, secondheroask)  # Calls the attackstart function.


def attackstart(attackhero_1, attackhero_2, result, hp1, hp2, firstheroask, secondheroask):  # the function where all the attack action happening.

    attackline = 15 * "-" + " " + result + " Attacks !! " + 15 * "-"  # The prompt that says who is going to attack.
    while True:
        if result == attackhero_1:  # The first heros' turn to attack according to coin toss result.
            print attackline
            chooseattack = "Choose your attack magnitude between 1 and 50:"
            choosendamage = int(raw_input( chooseattack))  # Asks the first user to define a number to attack and sets it to choosendamage.
            if choosendamage > 50:  # The possibility for user to choose a nuber bigger than 50.
                print "The attack magnitude must be between 1 and 50."  # The warning prompt for user.
            elif choosendamage <= 50 and choosendamage > 0:  # The possibility for user to choose correct number in between the range.
                dealdamage = random.randint(1,
                                            100)  # Decides a number in between 1 and 100, which will be usen later on.
                if 100 - choosendamage < dealdamage:  # The possibilty of missing the shoot.
                    print "Ooopsy!", attackhero_1, "missed the attack!"  # Informs the user  that they missed the shoot.
                    choosendamage = 0   # Sets the choosen damage back to 0 because the shoot is missen and shouldn't hurt the opponent.
                    attack(attackhero_1, attackhero_2, result, hp1, hp2, choosendamage, firstheroask, secondheroask)  # Calls the attack function.
                elif 100 - choosendamage >= dealdamage:  # The possibility of making the shoot.
                    print attackhero_1, "hits", choosendamage, "damage!!"  # Informs the user that their attack is succesfull and shoots with the choosen damage.
                    attack(attackhero_1, attackhero_2, result, hp1, hp2, choosendamage, firstheroask, secondheroask)  # Calls the attack function.

        elif result == attackhero_2:  # The first hero's turn to attack according to coin toss result.
            print attackline
            chooseattack = "Choose your attack magnitude between 1 and 50:"
            choosendamage = int(raw_input( chooseattack))  # Asks the second user to define a number to attack and sets it to choosendamage.
            if choosendamage > 50:  # The possibility for user to choose a nuber bigger than 50.
                print "The attack magnitude must be between 1 and 50."  # The warning prompt for user.
            elif choosendamage <= 50 and choosendamage > 0:  # The possibility for user to choose correct number in between the range.
                dealdamage = random.randint(1,
                                            100)  # Decides a number in between 1 and 100, which will be usen later on.
                if 100 - choosendamage < dealdamage:  # The possibilty of missing the shoot.
                    print "Ooopsy!", attackhero_2, "missed the attack!"  # Informs the user  that they missed the shoot.
                    choosendamage = 0  # Sets the choosen damage back to 0 because the shoot is missen and shouldn't hurt the opponent.
                    attack(attackhero_1, attackhero_2, result, hp1, hp2, choosendamage, firstheroask, secondheroask)  # Calls the attack function.
                elif 100 - choosendamage >= dealdamage:  # The possibility of making the shoot.
                    print attackhero_2, "hits", choosendamage, "damage!!"  # Informs the user that their attack is succesfull and shoots with the choosen damage.
                    attack(attackhero_1, attackhero_2, result, hp1, hp2, choosendamage, firstheroask, secondheroask)  # Calls the attack function.


def attack(attackhero_1, attackhero_2, result, hp1, hp2, choosendamage, firstheroask, secondheroask):  # The function designs the healtbars according to the given damage.

    if result == attackhero_2:  # The second heros' attack situation.
        result = attackhero_2  # Sets the cointoss result manually to second hero.
        hp1 = hp1 - choosendamage  # Sets the first heros' hp bar according to the hit shot by the second user.
        if hp1 == 100:  # The possibilty for missed shots.
            print attackhero_1, (61 - len(attackhero_1)) * " " + attackhero_2, "\n", "HP[" + str(hp1) + "]:", str(hp1 / 2 * "|") + str((100 - hp1) / 2 * " "), 1 * " ", "HP[" + str(hp2) + "]:", str(hp2 / 2 * "|")
            return attackstart(attackhero_1, attackhero_2, attackhero_1, hp1, hp2, firstheroask, secondheroask)  # Saves the variables according to shot and returns to the attackstart function.
        elif hp1 < 100 and hp1 >= 10:  # This is the condition if the fist heros' health has two digits.
            print attackhero_1, (60 - len(attackhero_1)) * " " + attackhero_2, "\n", "HP[" + str(hp1) + "]:", str(hp1 / 2 * "|") + str((100 - hp1) / 2 * " "), 1 * " ", "HP[" + str(hp2) + "]:", str(hp2 / 2 * "|")
            return attackstart(attackhero_1, attackhero_2, attackhero_1, hp1, hp2, firstheroask, secondheroask)  # Saves the variables according to shot and returns to the attackstart function.
        elif hp1 < 10 and hp1 >= 1:  # This is the condition if the fist heros' health has one digits.
            print attackhero_1, (59 - len(attackhero_1)) * " " + attackhero_2, "\n", "HP[" + str(hp1) + "]:", str(hp1 / 2 * "|") + str((100 - hp1) / 2 * " "), 1 * " ", "HP[" + str(hp2) + "]:", str(hp2 / 2 * "|")
            return attackstart(attackhero_1, attackhero_2, attackhero_1, hp1, hp2, firstheroask, secondheroask)  # Saves the variables according to shot and returns to the attackstart function.
        elif hp1 == 0 or hp1 < 0:  # This is the possibiltiy of second hero's winning.
            finish2 = 67 * ("#") + "\n" + ((60 - len(attackhero_2)) / 2 * "#") + attackhero_2 + " Wins !!" + ((60 - len(attackhero_2)) / 2) * "#" + "\n" + 67 * ("#")
            print finish2  # Prints the winning prompt and says second hero won the game.
            finito(firstheroask, secondheroask, hp1, hp2)  # Calls the finito function

    elif result == attackhero_1:  # The first heros' attack situation.
        result = attackhero_1  # Sets the cointoss result manually to first hero.
        hp2 = hp2 - choosendamage  # Sets the second heros' hp bar according to the hit shot by the first user.
        if hp2 == 100:  # The possibilty for missed shots.
            print attackhero_1, (61 - len(attackhero_1)) * " " + attackhero_2, "\n", "HP[" + str(hp1) + "]:", str(hp1 / 2 * "|") + str((100 - hp1) / 2 * " "), 1 * " ", "HP[" + str(hp2) + "]:", str(hp2 / 2 * "|")
            return attackstart(attackhero_1, attackhero_2, attackhero_2, hp1, hp2, firstheroask, secondheroask)  # Saves the variables according to shot and returns to the attackstart function.
        elif hp2 < 100 and hp2 >= 10:  # This is the condition if the second heros' health has two digits.
            print attackhero_1, (60 - len(attackhero_1)) * " " + attackhero_2, "\n", "HP[" + str(hp1) + "]:", str(hp1 / 2 * "|") + str((100 - hp1) / 2 * " "), 1 * " ", "HP[" + str(hp2) + "]:", str(hp2 / 2 * "|")
            return attackstart(attackhero_1, attackhero_2, attackhero_2, hp1, hp2, firstheroask,secondheroask)  # Saves the variables according to shot and returns to the attackstart function.
        elif hp2 < 10 and hp2 >= 1:  # This is the condition if the second heros' health has one digits.
            print attackhero_1, (59 - len(attackhero_1)) * " " + attackhero_2, "\n", "HP[" + str(hp1) + "]:", str(hp1 / 2 * "|") + str((100 - hp1) / 2 * " "), 1 * " ", "HP[" + str(hp2) + "]:", str(hp2 / 2 * "|")
            return attackstart(attackhero_1, attackhero_2, attackhero_2, hp1, hp2, firstheroask,secondheroask)  # Saves the variables according to shot and returns to the attackstart function.
        elif hp2 == 0 or hp2 < 0:  # This is the possibiltiy of first hero's winning.
            finish1 = 67 * ("#") + "\n" + ((60 - len(attackhero_1)) / 2) * "#" + attackhero_1 + " Wins !!" + ((60 - len(attackhero_1)) / 2) * "#" + "\n" + 67 * ("#")
            print finish1  # Prints the winning prompt and says first hero won the game.
            finito(firstheroask, secondheroask, hp1, hp2)  # Calls the finito function.


def finito(firstheroask, secondheroask, hp1, hp2):  # The function which asks the user eigther they want to play again or finish the game.

    while True:
        answer = raw_input("Do you want to play another round Yes (Y) or No (N) ? :")  # Asks user the question.
        if answer == "Yes" or answer == "yes" or answer == "YES" or answer == "Y" or answer == "y":  # The possibilty of user to play again.
            restart(firstheroask, secondheroask)  # Calls the restart function and game start again by cointoss.
        elif answer == "No" or answer == "NO" or answer == "no" or answer == "N" or answer =="n":  # The possibilty of user to and the game.
            print "Thanks for playing! See you again!"  # Prints the anding prompt.
            quit()  # Finishes the whole funcion/s.
        else:  # The possibility of user the write anything else or nothing.
            continue  # Returns back and asks the same question.


namecoin()

# ps: When the program starts, and hp bars shown, thee is a miner problem. Whens the attacks take turn the secon players bar and name move by one space to back and forth. We coukdn't figue it out.
