import math

def sizeAlphobetFunc(password):
    config = {
        "lower": 0,
        "upper": 0,
        "number": 0,
        "special": 0
    }

    for c in password:
        if c.islower():
            config['lower'] = 26
        elif not set("0123456789").isdisjoint(c):
            config['number'] = 10
        elif not set("ABCDEFGHIGKLMNOPQRSTUVWXYZ").isdisjoint(c):
            config['upper'] = 26

        if not set(".,:;!_*-+()/#¤%&)").isdisjoint(c):
            config['special'] = 33

    sizeAlphobet = 0

    for citem in config:
        sizeAlphobet += int(config[citem])

    print('Мощность алфавита: ', sizeAlphobet)
    print('Кол-во комбинаций: ', math.pow(sizeAlphobet, len(password)))

    return sizeAlphobet

def timeOfHack(s, m, v, N, length):
    M = math.pow(N, length)

    if (M % m == 0):
        seconds = M/s + (M/m - 1)*v
    else:
        seconds = M/s + M/m*v

    years = seconds / (12 * 30 * 24 * 60 * 60)
    seconds %= 30 * 24 * 60 * 60 * 12

    months = seconds / (30 * 24 * 60 * 60)
    seconds %= 30 * 24 * 60 * 60

    days = seconds / (24 * 60 * 60)
    seconds %= (24 * 60 * 60)

    hours = seconds / (60 * 60)
    seconds %= (60 * 60)

    minuts = seconds / 60
    seconds %= 60

    print(f'YY:{round(years)} MM:{round(months)} DD:{round(days)} HH:{round(hours)} MM:{minuts} SS:{seconds}')
def main():
    while True:
        password = input('Введите пароль: ')

        N = sizeAlphobetFunc(password)

        timeOfHack(150, 4, 0, N, len(password))



if __name__ == '__main__':
    main()