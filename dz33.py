def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = ['moon', 38, False]
values_list_2 = [56, 'sky']
values_dict = {'a':18, 'b':32.5, 'c':0.3}

print_params()
print_params(5, 'sun', False)
print_params(56.7, 'moon')
print_params(b = 25)
print_params(c = [1,2,3])
#print_params(49, 'star', 78, 22) выдает ошибку так как элементов больше чем параметров
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)





