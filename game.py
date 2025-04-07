'''dunno if this is the main index but it probably is'''

import gamefunctions

name = input('Enter your name please: ')
gamefunctions.playerStats['Name'] = name
print(f'Welcome {name}.')
input(f'You wake up in a village, sweaty and trembling as if you were chased out the night before.\nPress enter to continue')
input(f'Looking to the nightstand, a club sits. You pick it up as you get off the bed, but as you do the club seemingly absorbs into you!')
input('A surge of power channels through you, and then nothing...')
input('"Maybe I should vist the shop and see what else i could absorb. That power felt amazing", you say to yourself')
input('Just then the inn maid walks into your room, letting you know that your stay is over unless you can cover the coin needed. You exit the inn')
print()

playerInput = input(f'What will you do today?\n\n1) Go out and hunt a monster\n2) Stay the night at the inn (Heal): 5g\n3) Quit\n4) Stats\n5) Shop\n6) Inventory\n7) Save and Quit\n8) Load\n\nEnter a number choice here: ')

while playerInput != '3':
   
   if playerInput == '1':
    
    gamefunctions.attackMoment()
      
   elif playerInput == '2' and gamefunctions.playerStats['Gold'] >= 5:
        gamefunctions.rest()
   
   elif playerInput == '4':
      for i in gamefunctions.playerStats:
         print(i, gamefunctions.playerStats[i])
      input('press key to continue')

   elif playerInput == '5':
      gamefunctions.town_shop()

   elif playerInput == '6':
      gamefunctions.inv()

   elif playerInput == '7':
      gamefunctions.savquit()
      

   elif playerInput == '8':
      gamefunctions.load()

      
      
   else:
        print('Please choose one of the options asshole')
        
   playerInput = input(f'What will you do today?\n\n1) Go out and hunt a monster\n2) Stay the night at the inn (Heal): 5g\n3) Quit\n4) Stats\n5) Shop\n6) Inventory\n7) Save and Quit\n8) Load\n\nEnter a number choice here: ')