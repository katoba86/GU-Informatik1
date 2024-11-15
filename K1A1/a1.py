
def main():
    rounds = []
    numRounds = int(input("Bitte anzahl Runden eingeben: "))
    for n in range(numRounds):
        rounds.append(float(input(f'Runde {n+1} Zeit:')))
    calc(rounds)


def calc(rounds):
    _min = min(rounds)
    _max = max(rounds)
    _sum = 0
    for i in rounds:
        _sum += i
    _avg = _sum/len(rounds)
    print(f'Anzahl Runden: {len(rounds):02}')
    print(f'AVG Time: {_avg:.2f}')
    print(f'Max Time: {_max:.2f}')
    print(f'Min Time: {_min:.2f}')




if __name__ == '__main__':
    main()

