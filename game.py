'''dunno if this is the main index but it probably is'''
import gamefunctions
name = input('Enter your name please: ')
print(f'Welcome {name}, enjoy your stay.')

gamefunctions.purchase_item(16.5, 80.0, 3)
gamefunctions.print_welcome('Andrew')
gamefunctions.print_shop_menu('Oreos', 7.90, 'The Relic', 999)
monter = gamefunctions.new_random_monster()
print(monter['name'])
print(monter['description'])