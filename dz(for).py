list = ['BMB', 'MB', 'LADA', 'KIA', 'HONDA']
#for i in list:
    #print('Я езжу на автомабиле марки', i)
cars_count = 0
for j in range (len(list)):
    cars_count += int(list[j])
    print(int(cars_count*10))