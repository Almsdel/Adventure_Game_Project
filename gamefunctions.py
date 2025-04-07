'''functions for cs150 game'''
#This is a header for Game fuctions python 
import random
import math
import json


def purchase_item(itemPrice,startingMoney,quantityToPurchase= 1):
    purchase = startingMoney - (itemPrice * quantityToPurchase)
    if purchase > 0:
        return print(f'You have {purchase} remaining after buying {int(quantityToPurchase)}')
    elif purchase < 0:
        quantityToPurchase = (startingMoney / itemPrice)
        purchase = startingMoney - (itemPrice * quantityToPurchase)
        return print(f'Insuficant funds. Instead you can purchase {int(quantityToPurchase)} with a remaining {purchase}')

def new_random_monster():
    '''Picks one of three monsters for player to fight
        all of which are goblins
    '''
    chance = random.randint(1,3)
    if chance ==1:
        goblin = {'name':'a goblin', 'description':'little guy haunched up on his heels', 'health' : 2, 'power' : 1, 'money' : 1.7}
    
        return goblin
    elif chance==2:
        goblin_raider = {'name':'a goblin raider', 'description':'little guy haunched up on his heels but a bit angry', 'health' : 3, 'power' : 2, 'money' : 4.6}
    
        return goblin_raider
    else:
        goblin_archer = {'name':'a goblin archer', 'description':'little guy haunched up on his heels with a bow', 'health' : 1, 'power' : 3, 'money' : 3}
    
        return goblin_archer
 
def print_welcome(name, width=0):
    '''
    Doctsting here: letting you know this fuction prints given name with "Hello," 
    at the start
    '''
    title = "Hello, " + name +'!'
    print(f'{title:o^20}')
    #o was added for ease of sight

def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    """Whoa this is a docstring"""
    item2Price = f'{item2Price:.2f}'
    #Returns given itemPrice as a string with decimial point 2 spots from center value.
    #If i can add a $ to a float let me know i tried
    item1Price = f'{item1Price:.2f}'
    print('-'*24)
    print(f'| {item1Name:<12} {'$'+item1Price:>8}|')
    print(f'| {item2Name:<12} {'$'+item2Price:>8}|')
    print('-'*24)

def test_function():
    '''helps call functions
    print_shop_menu(item1name, item1price, item2name, item2price)
    print_welcome(name, width=0)
    new_random_monster()
    purchase_item(itemPrice,startingMoney,quantityToPurchase= 1)
    '''

    #part 2 
    print_shop_menu('Milk', 7.90, 'Orange', 1.10)
    print_shop_menu('iPhone 16', 799.99, 'PS5', 600)
    print_shop_menu('Dragon Fruit', 1.30, 'Eggs', 6.40)
    #prints signs, albiet very simple signs
    print_welcome('Jeff')
    print_welcome('Jim Tom')
    print_welcome('Dimioton')
    #prints names with o's at the start and end 

    #part 1
    monter = new_random_monster()
    print(monter['name'])
    print(monter['description'])
    print(monter['health'])
    print(monter['power'])
    print(monter['money'])
    #prints a whole monster
    purchase_item(12.6, 80.0, 3)
    purchase_item(12, 80, 7)
    purchase_item(12, 80)

def attackMoment():
    '''Player fights a monster from new_random_monster
       all actions are dictated by 1 or 2 
       attackInput is the variable that lets user pick an action to fight or run. 
    '''
    monster = new_random_monster()
    monsterHP = monster.copy()
    print(f"You've encountered a monster! Its a {monster['name']}. Its a {monster['description']}.")
    attackInput = input(f'What will you do?\n\n1) Attack (Lose {monster['power']}hp)\n2) Run (Return to town)\n')
    print(f'{playerStats['Name']}: {playerStats["Health"]} hp')
    while monsterHP['health'] > 0:
        if attackInput =='1':
         monsterHP['health'] -= playerStats['Attack']
         playerStats['Health'] -= monsterHP['power']
         if monsterHP['health'] <= 0:
           input(f'You won! Gained {monsterHP['money']} Gold\nPress any key to continue.')
           playerStats['Gold'] += monsterHP['money']
         elif monsterHP['health'] > 0:
          attackInput = input(f"Strike agian? 1) Yes (Lose {monsterHP['power']} hp) 2) No\n")
        elif attackInput =='2':
            break
          
def rest():
    '''Heals player for 30 health and resets player health from items
    
    '''
    print('You feel well rested')
    playerStats['Health'] += 30
    if playerStats['Health'] > 30:
      playerStats['Health'] = 30
    input('press key to continue') 
  
def town_shop():
    '''My over thought out shop it has weapons and armor and eventually items that the player absorbs to boost stats
        spend whole day making this just to read i should have made a durability system. please forgive me Jeff! You should
        teach a class on Godot if you want us to make a game it uses python as well. Game design class would be cool.
    '''
    print('Welcome to our Amazing Bazzar')
    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
    while shop != '4':
        #Weapons tab
        if shop == '1':
            for i, d in enumerate(weapoons):
                print(i+1 ,d['weap'])
            pick = input(f'Choose something will ya!\n')
            costsw = [d['cost'] for d in weapoons]
            if pick == '1':
                #This code block is copied everywhere in this func. Lets player buy weapon if they have the coin and choose yes
                #FIXME for some reason the inn works but this doesnt if the player has too little gold 
                pick = input(f'Purchase for {costsw[0]}?\ny/n\n')
                if pick == 'y' or 'Y':
                    if playerStats['Gold'] > 30:
                        playerStats['Gold'] -= costsw[0]
                        input(f'Purchase successful\npress enter to continue')
                        playerInvW.append(weapoons[0])
                    elif playerStats['Gold'] < 30:
                        print('Come back with the coin and then we will talk')
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
                elif pick != 'y' or 'Y':
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')

            elif pick == '2':
                pick = input(f'Purchase for {costsw[1]}?\ny/n\n')
                if pick == 'y' or 'Y':
                    if playerStats['Gold'] > costsw[1]:
                        playerStats['Gold'] -= costsw[1]
                        input(f'Purchase successful\npress enter to continue')
                        playerInvW.append(weapoons[1])
                    elif playerStats['Gold'] < costsw[1]:
                        print('Come back with the coin and then we will talk')
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
                elif pick != 'y' or 'Y':
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
            
            elif pick == '3':
                pick = input(f'Purchase for {costsw[2]}?\ny/n\n')
                if pick == 'y' or 'Y':
                    if playerStats['Gold'] > costsw[2]:
                        playerStats['Gold'] -= costsw[2]
                        input(f'Purchase successful\npress enter to continue')
                        playerInvW.append(weapoons[2])
                    elif playerStats['Gold'] < costsw[2]:
                        print('Come back with the coin and then we will talk')
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
                elif pick != 'y' or 'Y':
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
        #Armors Tab
        if shop == '2':
            for i, d in enumerate(armor):
                print(i+1 ,d['de'])
            pick = input(f'Choose something will ya!\n')
            costs = [d['cost'] for d in armor]
            
            if pick == '1':
                pick = input(f'Purchase for {costs[0]}?\ny/n\n')
                if pick == 'y' or 'Y':
                    if playerStats['Gold'] > costs[0]:
                        playerStats['Gold'] -= costs[0]
                        input(f'Purchase successful\npress enter to continue')
                        playerInvA.append(armor[0])
                    elif playerStats['Gold'] < costs[0]:
                        print('Come back with the coin and then we will talk')
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
                elif pick != 'y' or 'Y':
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
            
            elif pick == '2':
                pick = input(f'Purchase for {costs[1]}?\ny/n\n')
                if pick == 'y' or 'Y':
                    if playerStats['Gold'] > costs[1]:
                        playerStats['Gold'] -= costs[1]
                        input(f'Purchase successful\npress enter to continue')
                        playerInvA.append(armor[1])
                    elif playerStats['Gold'] < costs[1]:
                        print('Come back with the coin and then we will talk')
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
                elif pick != 'y' or 'Y':
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')

            elif pick == '3':
                pick = input(f'Purchase for {costs[2]}?\ny/n\n')
                if pick == 'y' or 'Y':
                    if playerStats['Gold'] > costs[2]:
                        playerStats['Gold'] -= costs[2]
                        input(f'Purchase successful\npress enter to continue')
                        playerInvA.append(armor[2])
                    elif playerStats['Gold'] < costs[2]:
                        print('Come back with the coin and then we will talk')
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
                elif pick != 'y' or 'Y':
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
        if shop == '3':
            print('Not yet')
            shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n') 
              
def inv():
    
    '''INventory system
        it is lame and a bit dumb but it does the job
        1 2 3 is picked as strings through input
        1 is weapons
        2 is armor
        3 is leave
    '''
    print('What would you like to do?')
    chouce = input(f'1) Equip Weapon\n2) Equip Armor\n3) Leave\n')
    while chouce != '3':
        
        
        
        for i, d in enumerate(playerInvW):
            #Two off load inventories for the respective items
            #No limit to amount of items besides the time it takes to get more than 4 weapons or armors
            weapons = [d['weap'] for d in playerInvW]
        for i, d in enumerate(playerInvA):
            armors = [d['de'] for d in playerInvA]
            
        if chouce == '1':
            print('What would you want to equip?')
            for i, d in enumerate(weapons):
             print(i+1, d)
            chouce = input('Enter Number: ')
            if chouce == '1':
                print('Equiped')
                playerStats['Attack']+=playerInvW[0]['power']
            
            elif chouce == '2':
                print('Equiped')
                playerStats['Attack'] += playerInvW[1]['power']
                del playerInvW[1]

            
            elif chouce == '3':
                print('Equiped')
                playerStats['Attack']+=playerInvW[2]['power']
                del playerInvW[2]


            elif chouce == '4':
                print('Equiped')
                playerStats['Attack']+=playerInvW[3]['power']
                del playerInvW[3]

        elif chouce == '2':
            print('What would you want to equip?')
            for i, d in enumerate(armors):
             print(i+1, d)
            chouce = input('Enter Number: ')
               
               
            if chouce == '1':
                print('Equiped')
                playerStats['Health']+=playerInvA[0]['ar']
            
            elif chouce == '2':
                print('Equiped')
                playerStats['Health']+=playerInvA[1]['ar']
                del playerInvA[1]

            elif chouce == '3':
                print('Equiped')
                playerStats['Health']+=playerInvA[2]['ar']
                del playerInvA[2]
            elif chouce == '4':
                print('Equiped')
                playerStats['Health']+=playerInvA[3]['ar']
                del playerInvA[3]
            
        chouce = input(f'1) Equip Weapon\n2) Equip Armor\n3) Leave\n')
playerStats = {"Name" : "" , "Health":10, "Attack": 1, "Gold": 0}                             
weapoons = [
            {'weap':'Sword', 'desc':'Normal Sword', 'cost':30, 'power':3},
             {'weap':'Spear', 'desc':'A warriors weapon.', 'cost':40, 'power':4}, 
             {'weap':'Club','desc':'Big Frickin Club', 'cost':10, 'power':1}
             ]
def savquit():
    '''This function saves the game
        use y or n to choose yes or no to save
    '''
    yn = input(f'Would you like to save and quit?\ny/n\n')
    while yn != 'n' or 'N':
        global stats_json
        stats_json = [playerStats, playerInvW, playerInvA]
        if yn == 'y' or 'Y':
            with open('save.json', 'w' ) as f:
                json.dump(stats_json, f, indent=4)
                
            input("Save Sucessful")
            exit()
        break    

def load():
    ny = input('Load save?\ny/n')
    global playerStats
    while ny != 'n' or 'N':
        if ny == 'y' or 'Y':
            with open('save.json', 'r' ) as f:
                loading = f.read()
                stats = json.loads(loading)
                playerStats = stats[0]
                playerInvW = stats[1]
                playerInvA = stats[2]
                
                
            input("Load Sucessful")
            break

armor = [
    {'de':'Leather Armor', 'desc':'False sense of Security', 'cost':15, 'ar':5},
    {'de':'Plate Armor', 'desc':'Real sense of Security', 'cost':150, 'ar':50},
    {'de':'Chain Armor', 'desc':'Security', 'cost':75, 'ar':25},
]
stats_json = str(playerStats)
playerInvW= [{'weap':'None', 'power':0}]
playerInvA = [{'de':'None', 'ar': 0}]
if __name__ == '__main__':
    test_function()
