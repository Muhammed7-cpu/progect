def check_password(user_pas):

    porol_len =len(user_pas)

    low = 'abcdefghijklmnopqrstuvwxyz'
    upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dig = '0123456789'
    sym = '!@#$%^&*()_+-'

    h_low = h_upp = h_dig =  h_sym = False

    for i in range(porol_len):
        if user_pas[i] in low:
            h_low = True
        elif user_pas[i] in upp:
            h_upp = True
        elif user_pas[i] in dig:
            h_dig = True
        elif user_pas[i] in sym:
            h_sym = True

    double = False
    for j in range(1,porol_len):
        if user_pas[j] == user_pas[j - 1]:
            double = True
            break

    sbor = 0

    if h_low:
        sbor += 26
    if h_upp:
        sbor += 26
    if h_dig:
        sbor += 10
    if h_sym:
        sbor += len(sym)

    comb = sbor ** porol_len

    second = comb  / 10000000

    if second < 1:
         wywod= "очень слабый"
    elif second < 60:
        wywod = "слабый"
    elif second < 3600:
        wywod = "средний"
    elif second < 86400:
        wywod = "хороший"
    else:
        wywod = "очень хороший"

    return wywod,double