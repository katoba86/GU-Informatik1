weekdays = ['Mo','Di','Mi','Do','Fr','Sa','So']
sleepHours = []
checkMin = 0
checkMax = 16
toSleep = 8


def ask(w):
    t = int(input(f'Anzahl Schlafstunden am {weekdays[w]}?'))
    if t<checkMin or t>checkMax:
        print(f'Eingabe nicht gültig! Zwischen {checkMin} und {checkMax}!')
        ask(w)
    return t


def calc():
    sum = 0
    for s in sleepHours:
        sum +=s
    ret = (len(weekdays)*toSleep) - sum
    if ret <= 0:
        print("Gut geschlafen!")
    else:
        print(f'Schlafmangel von {ret} Stunden! Bitte Feierabend machen!')

def main():
    for w in range(len(weekdays)):
        _h = ask(w)
        sleepHours.append(_h)
    calc()


if __name__ == '__main__':
    main()