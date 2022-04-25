# You can use this workspace to write and submit your adventure game project.
import time
import random
import sys
from os import system, name
from urllib import response


starting_statements1 = [
    "\n You find yourself standing in an open field, under a light post.",
    "filled with grass and yellow wildflowers.",
    "Rumor has it that a wicked fairie is somewhere around here .",
    "and has been terrifying the nearby village.... ",
    "\n What do you want you do?"
    ]

first_stateme = ["Enter 1 if you are brave enough to try your luck with him.",
                 "Enter 2 to stay hidden.\n"]

scenario1_statements = [
    "\n You attack the fairie with your bare hands.",
    "Unfortunately, he's much looks stronger than you.",
    "Plus, he knows karate.",
    "He throws you with force on the ground.",
    "but you countered that mave with your karate moves"]

scenario2_statements = [
    "\n Yo knock the door and the owner opens the door.",
    "You pick up a gun and use your phone to call 911.",
    "You then go back to confront the fairie .\n"]


win_statements1 = [
    "\n Wow, you totally nailed it!",
    "The farrie was overpowered.",
    "Plus, his hostages are  now free.\n"]

win_statements2 = [
    "you were unharmed .",
    "You killed the farrie",
    "but he had a partner that fled unnoticed.\n"]

win_statements3 = [
    "\n A policeman patrol happened to pass by,",
    "and they arrested the farie and his fleeing pathener.",
    "Both you & the villagers escaped without a scratch.\n"]

game_over_statements1 = [
    "\n Your effort was desperate & reckless.",
    "The bad guy killed you.",
    "Plus, he took an inocent village girl hostage.\n"]

game_over_statements2 = [
    "\n Okay, you totally messed it up.",
    "This was the worst decision you ever made.",
    "You really have to act less recklessly next time.",
    "At least, you didn't lose your life.\n"]

game_over_statements3 = [
    "\n The farie got away.",
    "The police came very late.",
    "You were lucky, but a village girl was taken hostage.\n"]


def print_with_delay(statement_to_print):

    '''Takes a statement and prints it with delay.
    Args:
        print_with_delay(string): The statement to print.
    '''
    print(statement_to_print)
    time.sleep(2)


def scenerio_choice():

    ''' When the player makes a choice by selecting 1 or 2 at the beginning ,
    the  scenario of his choice is decided in a random way.
    Args: scenerio_choice()
    '''
    x = random.randint(1, 3)
    if x == 1:
        scenerio_output(scenario1_statements)
    elif x == 2:
        scenerio_output(scenario2_statements)
    elif x == 3:
        scenerio_output(scenario1_statements)


def scenerio_output(starting_statements):
    '''
    prints out the starting statement,
    by iterating over a large number of strings,
    and printing them out with the print_wit_delay function.
    Args:
        scenerio_output(starting_statement).
    '''
    for statement in starting_statements:
        print_with_delay(statement)


def win_statement():
    '''
    Prints the statements of the winning scenarios,
    by randomly selecting from the various winning scenerios statements.
    Args:
        win_statements ():
        The statements of the first winning scenario.
    '''
    x = random.randint(1, 3)
    if x == 1:
        scenerio_output(win_statements1)
    elif x == 2:
        scenerio_output(win_statements2)
    elif x == 3:
        scenerio_output(win_statements3)
    end_with_defeat()


def loose_statement():
    '''
    Prints the statements of  loosing scenarios,
    by randomly selecting from the loosing scenerio statements.

    Args:
        loose_statements():
        The statements of the loosing scenario.
    '''
    x = random.randint(1, 3)
    if x == 1:
        scenerio_output(game_over_statements1)
    elif x == 2:
        scenerio_output(game_over_statements2)
    elif x == 3:
        scenerio_output(game_over_statements3)
    end_with_defeat()


def print_like_typewriter(the_end):
    '''
   A very primitive, special effect to make characters appear in the screen
    as if they are written in a typewriter.
    Args:
        the_end (string): "THE END", "GAME OVER" or "TO BE CONTINUED" messages.
    '''

    for character in the_end:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.25)


def end_with_win():
    '''
    Prints the "THE END" sign when the player wins.
    It is printed after displaying of win_statements.

    Args:
        -
    '''

    print_like_typewriter("=======\n")
    print_like_typewriter("THE END\n")
    print_like_typewriter("=======\n")


def random_win_scenario():
    '''
    When the player makes a good choice at the beginning and therefore wins,
    the win scenario is decided in a random way.

    Args:
        random_win_scenerio():
    '''

    x = random.randint(1, 3)
    if x == 1:
        scenerio_output(win_statements1)
    elif x == 2:
        scenerio_output(win_statements2)
    elif x == 3:
        scenerio_output(win_statements3)
    end_with_win()


def end_with_defeat():
    '''
    Prints the "Game Over" sign when the player loses.
    It is printed after displaying of game_over_statements.
    Args:
        -
    '''

    print_like_typewriter("=========\n")
    print_like_typewriter("GAME OVER\n")
    print_like_typewriter("=========\n")


def decide_win_or_defeat():
    '''
    It takes the variable "decision" that comes from
    the start_game() function, decides win or defeat, and
    runs the relevant function.
    Args:
        decide_win_or_defeat(decision):
    '''
    decision = random.randint(1, 2)

    if decision == 1:
        random_defeat_scenario()
    elif decision == 2:
        random_win_scenario()
    else:
        print("Ops, something went wrong.")


def random_defeat_scenario():
    '''
    When the player makes a bad choice at the beginning and therefore loses,
    the defeat scenario is decided in a random way.
    This is a way to fullfill the requirement to have a result that
    comes from player's choice but also an element of randomness in the plot.
    Args:
        random_defeat_scenario():
    '''

    x = random.randint(1, 3)
    if x == 1:
        scenerio_output(game_over_statements1)
    elif x == 2:
        scenerio_output(game_over_statements2)
    elif x == 3:
        scenerio_output(game_over_statements3)

    end_with_defeat()


def clear():
    '''
    It clears the screen from the previous output in order to start fresh
    when the player decides to play again.
    Args:
        -
    '''

    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')


def start_over():
    '''
    Runs when the player decides to play again.

    Args:
        -
    '''
    start_game()
    ask_for_replay()


def goodbye():
    '''
   Prints the message below when the player does not want to play again.
   Args:
        -
    '''

    print_with_delay("\nHope to see you again!\n")
    print_like_typewriter("===============\n")
    print_like_typewriter("TO BE CONTINUED\n")
    print_like_typewriter("===============\n")


def ask_for_replay():
    '''
    Runs after the end of the game.,
    The player can choose to play again or not.
    Args:
        -
    '''

    print_with_delay("Do you want to play again?\n")
    response = valid_input("enter your desired choice?" +
                           "Please enter yes or no :", ['yes', 'no'])

    if response == "yes":
        clear()
        start_over()

    elif response == "no":
        goodbye()


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print(f'Sorry, the option "{option}" is invalid. Try again!')


def choice_feedback():
    answer = valid_input("enter another desired choice?" +
                         "Please enter 1 or 2: ", ['1', '2'])

    if answer == "1":
        print_with_delay("you choose" + " " + answer)
        print_with_delay("lets see if you choose wisely")
        scenerio_choice()
        decide_win_or_defeat()
    elif answer == "2":
        print_with_delay("You chose " + answer + ".")
        print_with_delay("Let's see if you chose wisely.")
        scenerio_choice()
        decide_win_or_defeat()
    else:
        print("do nothing")


def first_choice():
    scenerio_output(first_stateme)

    answer = valid_input("enter your desired choice?" +
                         "Please enter 1 or 2 : ", ['1', '2'])
    if answer == "1":
        print_with_delay("ok Good lets see what happen next")

    elif answer == "2":
        print_with_delay(" you seem scared but u stil have other choices")


def start_game():

    '''
    This is the main function of the game.
    After displaying the starting statements, the player must make
    their first and decisive choice that will define whether they win or lose.

    Args:
     -
    Returns:
        response(int): The input of player; it can be either 1 or 2.
    '''
    scenerio_output(starting_statements1)
    first_choice()
    choice_feedback()
    ask_for_replay()


if __name__ == '__main__':
    start_game()
