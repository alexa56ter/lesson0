import random
def new_password(p):
    password = ' '
    for i in range(3, 21):
        for j in range (i + 1, p + 1):
            if p % (i + j) == 0:
                password += str (i) + str (j)
                return password
            numbers1 = range(3, 21)
            p = random.choice(numbers1)
            password = new_password(p)
    print (new_password(p))




