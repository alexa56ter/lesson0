my_list=['apple','banana','orange','kiwi']
print('List',(my_list))
print ('First element:', (my_list[1]))
print('Last elenent:', (my_list[-1]))
print('Sablist:', (my_list[2:5]))
my_list[2]='peach'
print('Modified list:', (my_list))


my_dict = { 'Grape': 'виноград', 'Coconut':'кокос', 'Rain':'дождь', 'Sun': 'солнце'}
print('Dictionaly:', (my_dict))
print('Translation:', (my_dict.get('Sun')))
my_dict['Grape']='Виноград'
my_dict.update({'World': 'мир'})
print('Modified dictionary:' ,(my_dict))