'''dunno if this is the main index but it probably is'''

import gamefunctions

name = input('Enter your name please: ')
playerStats = {'Name' : name , 'Health':30, 'Attack': 2, 'Gold': 5}
print(f'Welcome {name}.')
playerInput = input(f'What will you do today?\n\n1) Go out and hunt a monster\n2) Stay the night at the inn (Heal): 5g\n3) Quit\n\nEnter a number choice here: ')


while playerInput != '3':
   monster = gamefunctions.new_random_monster()
   if playerInput == '1':
    
    print(f"You've encountered a monster! Its a {monster['name']}. Its a {monster['description']}.")
    attackInput = input(f'What will you do?\n\n1) Attack (Lose {monster['power']}hp)\n2) Run (Return to town)\n')
    if attackInput =='1':
      monsterHP = monster.copy()
      while monsterHP['health'] > 0:
        monsterHP['health'] -= playerStats['Attack']
      if monsterHP['health'] <= 0:
        input(f'You won! Gained {monsterHP['money']} Gold\nPress any key to continue.')
        playerStats['Gold'] += monsterHP['money']
      
   if playerInput == '2' and playerStats['Gold'] >= 5:
    print('You feel well rested')
    playerStats['Health'] += 30
    if playerStats['Health'] > 30:
      playerStats['Health'] = 30
    input()
   else:
        print('Please choose one of the options asshole')
        playerInput = input(f'What will you do today?\n\n1) Go out and hunt a monster\n2) Stay the night at the inn (Heal): 5g\n3) Quit\n\nEnter a number choice here: ')


   playerInput = input(f'What will you do today?\n\n1) Go out and hunt a monster\n2) Stay the night at the inn (Heal): 5g\n3) Quit\n\nEnter a number choice here: ')
          
          
      


    
      
