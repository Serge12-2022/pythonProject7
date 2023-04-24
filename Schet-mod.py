'''
ЗАДАНИЕ 1
1. В подпрограмме Мой банковский счет;
2. Добавить сохранение суммы счета в файл.

При первом открытии программы на счету 0
После того как мы воспользовались программой и вышли сохранить сумму счета
При следующем открытии программы прочитать сумму счета, которую сохранили
...
3. Добавить сохранение истории покупок в файл

При первом открытии программы истории нет.
После того как мы что нибудь купили и закрыли программу сохранить историю покупок.
При следующем открытии программы прочитать историю и новые покупки уже добавлять к ней;
...
4. Формат сохранения количество файлов и способ можно выбрать самостоятельно.

'''

cash = 0
pokup = 0
plat_summ = 0
prod = {'сыр':20, 'хлеб':8, 'молоко':12, 'масло':18, 'яйца':14}
buy_hystory = []

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        schet = open('schet.txt', 'r')
        schet = int(schet.read())
        cash_in = int(input('Введите сумму на которую хоите пополнить счет: ',))
        cash = cash + cash_in + schet
        print('Сейчас на счету - ',cash, 'денег')
        schet = open('schet.txt', 'w')
        schet.write(str(cash))
        schet.close()
        pass
    elif choice == '2':
        vibor = input('Выберите из продуктов: сыр, хлеб, молоко, масло, яйца - что будете покупать: ',)
        if vibor in list(prod.keys()):
            buy_prod = open('buy_prod.txt', 'r')
            #bp = buy_prod.read()
            prod1 = prod
            plat = prod1.pop(vibor)
            print('Оставшиеся в продаже продукты: ', prod)
            plat_summ += plat
            cash = cash - plat
            print('Оставшиеся деньги: ', cash)
            buy_hystory.append(vibor)
            bp = buy_prod.read() + ' ' + vibor
            buy_prod = open('buy_prod.txt', 'w')
            buy_prod.write(str(bp))
            buy_prod.close()
        else:
            print('Нет такого продукта.')
    elif choice == '3':
        print('Список купленных продуктов:', buy_hystory)
        print('Потраченная сумма', plat_summ)

    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')