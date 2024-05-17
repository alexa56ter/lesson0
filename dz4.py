immutable_var=(1, 2, 3,[1, 2], True, 'string')
print(immutable_var)
#особенность кортежа в том, что он не изменяемый, можно только изменять объекты которые подверженны изминениям и находятся в нутри кортежа
mutable_list=[1, 2, 'a','b','string']
print(mutable_list)
mutable_list[2]= 'peach'
print(mutable_list)
mutable_list.append('kiwi')
print(mutable_list)
mutable_list.extend([8])
print(mutable_list)
