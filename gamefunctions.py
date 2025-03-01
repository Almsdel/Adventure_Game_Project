def purchase_item(itemPrice,startingMoney,quantityToPurchase='1'):
    purchase = startingMoney - (itemPrice * int(quantityToPurchase))
    if purchase >= 0:
        return print(f'You have {purchase} remaining after buying {quantityToPurchase}')
    elif purchase < 0:
        quantityToPurchase = (startingMoney / itemPrice)
        purchase = startingMoney - (itemPrice * int(quantityToPurchase))
        return (f'Insuficant funds. Instead you can purchase {int(quantityToPurchase)} with a remaining {purchase}')
def new_random_monster():
    goblin = {'name':'a goblin', 'description':'little guy haunched up on his heels', 'health' : 3, 'power' : 1, 'wealth' : 1}
    goblin_raider = {'name':'a goblin raider', 'description':'little guy haunched up on his heels', 'health' : 3, 'power' : 1, 'wealth' : 1}
    return goblin
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
monter = new_random_monster()
print(monter['name'])
# i dont know what the second part of the assignment ment, you can edit
#the parameter in monter to test the other keys I dont know how you could call the second dictionarary without a parameter
print(monter['description'])
print(monter['wealth'])



print_shop_menu('Milk', 7.90, 'Orange', 1.10)
print_shop_menu('iPhone 16', 799.99, 'PS5', 600)
print_shop_menu('Dragon Fruit', 1.30, 'Eggs', 6.40)

print_welcome('Jeff')
print_welcome('Jim Tom')
print_welcome('Dimioton')





leftover1 = purchase_item(12, 80, 3)
leftover2 = purchase_item(12, 80, 9)
leftover = purchase_item(12, 80)
print(leftover)
print(leftover2)
print(leftover1)




