
def new_password(p):
    password = ''
    for i in range(1 , p):
        for j in range(i+1, p):
            if p % (i + j) == 0:
                password += str(i) + str(j)
    return password

for p in range (3, 21):
    password = new_password(p)
    print(f'{p}       {password}')

