#list = ['BMB', 'MB', 'LADA', 'KIA', 'HONDA']
#for i in list:
    #print('Я езжу на автомабиле марки', i)
#cars_count = 0
#for j in range (len(list)):
    #cars_count += int(list[j])
    #print(int(cars_count*10))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
#not_primes = []
for i in numbers:
    is_prime = True
    for j in range (2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

print('primes:', primes)
print('not_primes:', [ i for i in numbers if i not in primes])

