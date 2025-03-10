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
#went back and fixed these two functions I think, dont really know until you tell me 

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
#purchase items works now i forgot to put print at the end of a return 

if __name__ == '__main__':
    test_function()



