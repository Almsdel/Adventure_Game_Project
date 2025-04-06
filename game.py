'''dunno if this is the main index but it probably is'''

import gamefunctions

name = input('Enter your name please: ')
gamefunctions.playerStats['Name'] = name
print(f'Welcome {name}.')
playerInput = input(f'What will you do today?\n\n1) Go out and hunt a monster\n2) Stay the night at the inn (Heal): 5g\n3) Quit\n4) Stats\n5) Shop\n6) Inventory\n\nEnter a number choice here: ')


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
    
      
      
      
   else:
        print('Please choose one of the options asshole')
        
   playerInput = input(f'What will you do today?\n\n1) Go out and hunt a monster\n2) Stay the night at the inn (Heal): 5g\n3) Quit\n4) Stats\n5) Shop\n6) Inventory\n\nEnter a number choice here: ')
          
          
      


    
      
