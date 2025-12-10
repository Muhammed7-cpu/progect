import random

def generate(level,dlina):

    low = 'abcdefghijklmnopqrstuvwxyz'
    upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dig = '0123456789'
    sym = '!@#$%^&*()_+-'

    easy = low + dig
    medium = upp + low + dig
    hard = low + upp + dig + sym

    porol = ''

    if level == 1:
        if dlina < 8:
            dlina = 8
            print("не правильный ввод автоматически 8 элементов\n")
    elif level == 2:
        if dlina < 10:
            dlina = 10
            print("не правильный ввод автоматически 10 элементов\n")
    else:
        if dlina < 12:
            dlina = 12
            print("не правильный ввод автоматически 12 элементов\n")

    dop = 2

    porol += random.choice(low)
    porol += random.choice(dig)

    if level != 1:
        porol += random.choice(upp)
        dop += 1
        if level != 2:
            dop += 1
            porol += random.choice(sym)

    for i in range(dlina - dop):
        if level == 1:
            kambayn = random.choice(easy)

        elif level == 2:
            kambayn = random.choice(medium)

        else :
            kambayn = random.choice(hard)
        porol += kambayn

    while True:
        s_porol = ''.join(random.sample(porol, len(porol)))
        wyhod = True

        for j in range(len(s_porol)-1):
            if s_porol[j] == s_porol[j+1]:
                wyhod = False
                break

        if wyhod:
            return s_porol