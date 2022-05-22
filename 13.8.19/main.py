# Подсчёт общей стоимости билетов на онлайн-конференцию
# v 1.0
# Александр Миронов (QAP-76)

# Ввод данных
visitors = list()
print('=== Онлайн-конференция ===')
n = int(input('Введите количество билетов, которые хотите приобрести: '))
for i in range(1, n + 1):
    while True:
        vAge = input(f'Введите возраст (количество полных лет) посетителя №{i}: ')
        try:
            iAge = int(vAge)
        except ValueError:
            print('Ошибка! Необходимо вводить возраст в числовом формате!')
        else:
            if iAge in range(0, 125):
                visitors.append(int(iAge))
                break
            else:
                print('Ошибка! Необходимо вводить реальный возраст!')

# Расчёт стоимости заказа
summ = 0
for i in visitors:
    if i in range(18, 26):
        summ += 990
    else:
        if i > 25:
            summ += 1390

if len(visitors) > 3:
    summ *= .9
    print('Вам скидка 10%!')

# Выдача результата
print(f'Итоговая сумма стоимости вашего заказа: {round(summ)} руб.')
