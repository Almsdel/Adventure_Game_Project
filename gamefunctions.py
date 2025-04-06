'''functions for cs150 game'''
#This is a header for Game fuctions python 
import random
import math


#part 1
def purchase_item(itemPrice,startingMoney,quantityToPurchase= 1):
    purchase = startingMoney - (itemPrice * quantityToPurchase)
    if purchase > 0:
        return print(f'You have {purchase} remaining after buying {int(quantityToPurchase)}')
    elif purchase < 0:
        quantityToPurchase = (startingMoney / itemPrice)
        purchase = startingMoney - (itemPrice * quantityToPurchase)
        return print(f'Insuficant funds. Instead you can purchase {int(quantityToPurchase)} with a remaining {purchase}')
def new_random_monster():
    chance = random.randint(1,6)
    if chance ==1:
        goblin = {'name':'a goblin', 'description':'little guy haunched up on his heels', 'health' : 2, 'power' : 1, 'money' : 1.7}
    
        return goblin
    elif chance==2:
        goblin_raider = {'name':'a goblin raider', 'description':'little guy haunched up on his heels but a bit angry', 'health' : 3, 'power' : 2, 'money' : 4.6}
    
        return goblin_raider
    else:
        goblin_archer = {'name':'a goblin archer', 'description':'little guy haunched up on his heels with a bow', 'health' : 1, 'power' : 5, 'money' : 3}
    
        return goblin_archer


#part 2   
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
    print(f"You've encountered a monster! Its a {monster['name']}. Its a {monster['description']}.")
    attackInput = input(f'What will you do?\n\n1) Attack (Lose {monster['power']}hp)\n2) Run (Return to town)\n')
    if attackInput =='1':
      monsterHP = monster.copy()
      while monsterHP['health'] > 0:
        monsterHP['health'] -= playerStats['Attack']
      if monsterHP['health'] <= 0:
        input(f'You won! Gained {monsterHP['money']} Gold\nPress any key to continue.')
        playerStats['Gold'] += monsterHP['money']
def rest():
    print('You feel well rested')
    playerStats['Health'] += 30
    if playerStats['Health'] > 30:
      playerStats['Health'] = 30
    input('press key to continue')   
def town_shop():
    print('Welcome to our Amazing Bazzar')
    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
    while shop != '4':
        if shop == '1':
            for i, d in enumerate(weapoons):
                print(i+1 ,d['weap'])
            pick = input(f'Choose something will ya!\n')
            costs = [d['cost'] for d in weapoons]
            if pick == '1':
                pick = input(f'Purchase for {costs[0]}?\ny/n\n')
                if pick == 'y' or 'Y' and playerStats['Gold'] > costs[0]:
                    playerStats['Gold'] -= costs[0]
                    input(f'Purchase successful\npress enter to continue')
                    playerInvW.append(weapoons[0])
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
                elif pick != 'y' or 'Y':
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')

            elif pick == '2':
                pick = input(f'Purchase for {costs[1]}?\ny/n\n')
                if pick == 'y' or 'Y' and playerStats['Gold'] > costs[1]:
                    playerStats['Gold'] -= costs[1]
                    input(f'Purchase successful\npress enter to continue')
                    playerInvW.append(weapoons[1])
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
                elif pick != 'y' or 'Y':
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
            
            elif pick == '3':
                pick = input(f'Purchase for {costs[0]}?\ny/n\n')
                if pick == 'y' or 'Y' and playerStats['Gold'] > costs[2]:
                    playerStats['Gold'] -= costs[2]
                    input(f'Purchase successful\npress enter to continue')
                    playerInvW.append(weapoons[2])
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
                elif pick != 'y' or 'Y':
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')

        if shop == '2':
            for i, d in enumerate(armor):
                print(i+1 ,d['de'])
            pick = input(f'Choose something will ya!\n')
            costs = [d['cost'] for d in armor]
            
            if pick == '1':
                pick = input(f'Purchase for {costs[0]}?\ny/n\n')
                if pick == 'y' or 'Y' and playerStats['Gold'] > costs[0]:
                    playerStats['Gold'] -= costs[0]
                    input(f'Purchase successful\npress enter to continue')
                    playerInvA.append(armor[0])
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
                elif pick != 'y' or 'Y':
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
            
            elif pick == '2':
                pick = input(f'Purchase for {costs[1]}?\ny/n\n')
                if pick == 'y' or 'Y' and playerStats['Gold'] > costs[1]:
                    playerStats['Gold'] -= costs[1]
                    input(f'Purchase successful\npress enter to continue')
                    playerInvA.append(armor[1])
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
                elif pick != 'y' or 'Y':
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')

            elif pick == '3':
                pick = input(f'Purchase for {costs[2]}?\ny/n\n')
                if pick == 'y' or 'Y' and playerStats['Gold'] > costs[2]:
                    playerStats['Gold'] -= costs[2]
                    input(f'Purchase successful\npress enter to continue')
                    playerInvA.append(armor[2])
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
                elif pick != 'y' or 'Y':
                    shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')
        if shop == '3':
            print('Not yet')
            shop = input(f'What will it be today, {playerStats["Name"]}\n1) Purchase Weapon\n2) Purchase Armor\n3) Purchase Item\n4) Leave\n')               
def inv():
    print('What would you like to do?')
    chouce = input(f'1) Equip Weapon\n2) Equip Armor\n3) Leave\n')
    while chouce != '3':
        print(playerInv)
        
        
        for i, d in enumerate(playerInvW):

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
                playerStats['Attack']+=playerInvW[1]['power']
            
            elif chouce == '3':
                print('Equiped')
                playerStats['Attack']+=playerInvW[2]['power']
            
            elif chouce == '4':
                print('Equiped')
                playerStats['Attack']+=playerInvW[3]['power']
        
        if chouce == '2':
            print('What would you want to equip?')
            for i, d in enumerate(armors):
             print(i+1, d)
            chouce = input('Enter Number: ')
               
               
            if chouce == '1':
                print('Equiped')
                playerStats['Attack']+=playerInvA[0]['ar']
            
            elif chouce == '2':
                print('Equiped')
                playerStats['Attack']+=playerInvA[1]['ar']
            
            elif chouce == '3':
                print('Equiped')
                playerStats['Attack']+=playerInvA[2]['ar']
            
            elif chouce == '4':
                print('Equiped')
                playerStats['Attack']+=playerInvA[3]['ar']
            
                



    chouce = input(f'1) Equip Weapon\n2) Equip Armor\n3) Leave\n')
            
                
                    



weapoons = [{'weap':'Sword', 'desc':'Normal Sword', 'cost':10, 'power':2}, {'weap':'Spear', 'desc':'A warriors weapon.', 'cost':20, 'power':4}, {'weap':'Hammer','desc':'Big Frickin Hamor', 'cost':15, 'power':3}]
armor = [
    {'de':'Leather Armor', 'desc':'False sense of Security', 'cost':15, 'ar':5},
    {'de':'Plate Armor', 'desc':'Real sense of Security', 'cost':150, 'ar':50},
    {'de':'Chain Armor', 'desc':'Security', 'cost':75, 'ar':25},
]
playerInv = []
playerInvW= [{'weap':'None', 'power':0}]
playerInvA = [{'de':'None', 'ar':'None'}]

playerStats = {'Name' : '' , 'Health':30, 'Attack': 2, 'Gold': 30}
monster = new_random_monster()

if __name__ == '__main__':
    test_function()



