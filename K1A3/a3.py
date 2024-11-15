def ask(_str,_min,_max = None):
    val = int(input(_str))
    if _max is None and val < _min:
        print('Invalid input!')
        ask(input,_min)
    if _max is not None and val > _max:
        print('invalid input')
        ask(input,_min,_max)
    return val


def table(start,dailyGrowInPercent,numGrowDays):
    _val = start
    for k in range(numGrowDays):
        print(f'{k+1:<10} {_val:02.03f}')
        _val = _val + _val * (dailyGrowInPercent/100)


def main():
    start = ask('Startwert',1)
    dailyGrowInPercent = ask('Tägliche Zunahme in P',1,100)
    numGrowDays = int(ask('Anzahl Tage',1))
    table(start,dailyGrowInPercent,numGrowDays)

if __name__ == '__main__':
    main()