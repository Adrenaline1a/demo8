flot = []
while True:
    com = input('Введите команду: ').lower()
    if com == 'Выход':
        break
    elif com == "Добавить":
        tip = input('Введите тип самолёта: ')
        nomer = input('Введите номер самолёта: ')
        mesto = input('Введите место прибытия: ')
        aflot = {
            'nomer': nomer,
            'mesto': mesto,
            'tip': tip
        }
        flot.append(aflot)
        if len(flot) > 1:
            flot.sort(key=lambda x: x.get('mesto', ''))
    elif com == 'Список':
        for ind, reys in enumerate(flot, 1):
            print(ind, 'Место прибытия: ',
                    reys.get('mesto', ''), "\n",
                  'Номер: ',
                    reys.get('nomer', ''), "\n",
                  'Тип: ',
                    reys.get('tip', ''))
    elif com == 'Выбрать':
        nom = input('Введите тип желаемого самолёта: ')
        for i, num in enumerate(flot, 1):
            if nom == num.get('tip', ''):
                print("Тип: ", num.get('tip', ''), "\n", "Номер: ", num.get('nomer', ''), "\n", "Место прибытия: ",
                      num.get('mesto', ''))
