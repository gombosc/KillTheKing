'''
Assasinate the king!
You are an enemy spy, tasked with killing the king
Each choice has 2 variants, with 50% chance to happen
Choice #1 - Kill the king directly, during a meeting, with your sword
Choice #2 - Poison the kings meal
Choice #3 - Sneak into the King's Chambers and stealth kill him with a knife
Choice #4 - Set the Palace on fire during night time and block all exits
Choice #5 - Disguise as a servant and backstab the King with a knife

'''

import random
import time    

def displayIntro():
    print()
    print('''You're an enemy spy sent by the opposing empire to kill King Charles.
Choose your desired form of assasination!
Each choice has a 50% chance of failure!
             
             #1 Challenge King Charles to a duel by sword!
             #2 Poison King Charles meal
             #3 Stealth kill him at night inside his chambers
             #4 Ride a dragon and set the castle on fire
             #5 Hire a maid to slit his throat while making love
             #6 Teleport the king to another dimension
             #7 Abandon mission

             Choose wisely! ( 1, 2, 3...)
             ''')
    print()

def chooseChoice():
    probab = random.randint(1,2)
    user_choice = input('Insert your choice:')
    if user_choice == "1" or user_choice == '#1' or user_choice == 'one':
        print("Mission Started!")
        print("...")
        print('''You challenge King Charles to a duel.''')
        time.sleep(2)
        print('He stares at you, eyes wide open. He can\'t believe your stupidity.')
        time.sleep(2)
        if probab == 1:
            print('''He laughs histerically while ordering the guards to capture and imprison you in the castle dungeon.''')
            time.sleep(2)            
            print('''-----------------
-----------------
-----------------''')

            time.sleep(2)
            print('''You haven't seen the sun in ages, your body is weak, your mind is lost in a sea of madness.''')
            time.sleep(2)
            print('The cell door opens with a large figure hidden by darkness.')
            time.sleep(2)
            print('He approaches you with a twisted grin on his face.')
            time.sleep(2)
            print('Knife in hand.')
            time.sleep(2)
            print('The King sends his regards, are the last words you ever hear.\n')
            print('Game Over!')
        else:
                print('''He laughs, everyone laughs. You draw your sword and plunge in for an attack while throwing a spherical shape towards the ground.''')
                time.sleep(2)
                print('''Smoke fills the room, confusion. You hear voices 'Protect the King!'. It's too late.''')
                time.sleep(2)
                print('''-----------------
-----------------''')
                time.sleep(2)
                print('''You jump over a table, sword in hand, you reach the king. His dumb smile now a cry for help, fallen on his butt.''')
                time.sleep(2)
                print('''You strike your sword, straight through the Kings chest. He screams but nobody hears. You slowly withdraw your sword.''')
                time.sleep(2)
                print('The King is dead. Time to go home!')
                time.sleep(2)
                print('You won!')
    elif user_choice == "2" or user_choice == '#2' or user_choice == 'two':
        print("Mission Started!")
        print("...")
        time.sleep(2)
        if probab == 1:
            print("")
        else:
            print("")
    elif user_choice == "3" or user_choice == '#3' or user_choice == 'three':
        print("Mission Started!")
        print("...")
        time.sleep(2)
        if probab == 1:
            print("")
        else:
            print("")
    elif user_choice == "4" or user_choice == '#4' or user_choice == 'four':
        print("Mission Started!")
        print("...")
        time.sleep(2)
        if probab == 1:
            print("")
        else:
            print("")
    elif user_choice == "5" or user_choice == '#5' or user_choice == '5':
        print("Mission Started!")
        print("...")
        time.sleep(2)
        if probab == 1:
            print("")
        else:
            print("")
    elif user_choice == "6" or user_choice == '#6' or user_choice == 'six':
        print("Mission Started!")
        print("...")
        time.sleep(2)
        if probab == 1:
            print("")
        else:
            print("")
    elif user_choice == "7" or user_choice == '#7' or user_choice == 'seven':
        print("Mission Started!")
        print("...")
        time.sleep(2)
        if probab == 1:
            print("")
        else:
            print("")

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    chooseChoice()
    print('Do you want to play again? (yes or no)')
    playAgain = input()


    
    
    
             
