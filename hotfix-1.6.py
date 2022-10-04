class fridge:

    def __init__(s, name, count):
        s.name = name
        s.count = count

    def display_fridge(s):
        print('Продукт: {}. кол-во: {}'.format(s.name, s.count))
B = 10
mi = 0
me = 0
c = 0
s = 0
beer = fridge("Певко", B)
milk = fridge("Молоко", mi)
meat = fridge("Мясо", me)
cheese = fridge("Сыр", c)
sweet = fridge("Вкусняшка", s)

flag = True
while flag:
    print("Возможные команды:")
    print('1) Посмотреть на содержимое')
    print('2) Добавить')
    print('3) Забрать')
    print('4) Завершить')

    print("Введите номер команды:")
    comand = input()
    if comand == '1':
        milk.display_fridge()
        meat.display_fridge()
        cheese.display_fridge()
        sweet.display_fridge()
        beer.display_fridge()

    elif comand == '2':
        print('Что вы хотите добавить')
        print('1) Молоко\n2) Мясо\n3) Сыр\n4) Вкусняшку\n5) Певко')
        print('Введите номер подукта:')
        comand = input()

        if comand == '1':
            print('Количество:')
            comand = int(input())
            mi += comand
            print('Вы закинули', comand, 'литров')
            milk = fridge("Молоко", mi)
            print('Нажмите Enter чтобы начать с начала')
            comand = input()
            continue

        elif comand == '2':
            print('Количество:')
            comand = int(input())
            me += comand
            print('Вы закинули', comand, 'килограмм')
            meat = fridge("Мясо", me)
            print('Нажмите Enter чтобы начать с начала')
            comand = input()
            continue

        elif comand == '3':
            print('Количество:')
            comand = int(input())
            c += comand
            print('Вы закинули', comand, 'кусочков')
            cheese = fridge("Сыр", c)
            print('Нажмите Enter чтобы начать с начала')
            comand = input()
            continue

        elif comand == '4':
            print('Количество:')
            comand = int(input())
            s += comand
            print('Вы закинули', comand, 'вкусняшек')
            sweet = fridge("Вкусняшки", s)
            print('Нажмите Enter чтобы начать с начала')
            comand = input()
            continue

        elif comand == '5':
            print('Количество:')
            comand = int(input())
            B += comand
            print('Вы закинули', comand, 'банок певка')
            beer = fridge("Певко", B)
            print('Нажмите Enter чтобы начать с начала')
            comand = input()
            continue

    elif comand == '3':
        print('Что вы хотите спиздить')
        print('1) Молоко\n2) Мясо\n3) Сыр\n4) Вкусняшку\n5) Певко')
        print('Введите номер подукта:')
        comand = input()

        if comand == '1' and not(mi <= 0):
            print('В наличии', mi, 'л.')
            print('Количество:')
            mi_take = int(input())
            if mi - mi_take < 0:
                print('В холодильнике нет столько молока', '\n', 'вы забираете то, что есть.')
                print('Вы забрали', mi, 'л.')
                mi *= 0
                print('Нажмите Enter чтобы начать с начала')
                milk = fridge("Молоко", mi)
                comand = input()
                continue
            elif mi > mi_take:
                print('Вы забрали', mi_take, 'л.')
                mi -= mi_take
                print('Осталось', mi, 'л.')
                milk = fridge("Молоко", mi)
                print('Нажмите Enter чтобы начать с начала')
                comand = input()
                continue
            else:
                print('Вы забрали', mi, 'л.')
                mi *= 0
                print('Молока не осталось')
                milk = fridge("Молоко", mi)
                print('Нажмите Enter чтобы начать с начала')
                comand = input()
                continue
        elif comand == '1' and mi == 0:
            print('В холодильнике нет молока')
            print('Нажмите Enter чтобы начать с начала')
            comand = input()
            continue

        if comand == '2' and not(me <= 0):
            print('Количество:')
            me_take = int(input())
            if me - me_take < 0:
                print('В холодильнике нет столько килограмм мяса', '\n', 'вы забираете то, что есть.')
                print('Вы забрали', me, 'кг.')
                me *= 0
                print('Нажмите Enter чтобы начать с начала')
                meat = fridge("Мясо", me)
                comand = input()
                continue
            elif me > me_take:
                print('Вы забрали', me_take, 'кг.')
                me -= me_take
                print('Осталось', me, 'кг.')
                meat = fridge("Мясо", me)
                print('Нажмите Enter чтобы начать с начала')
                comand = input()
                continue
            else:
                print('Вы забрали', me, 'кг.')
                me *= 0
                print('Мяса не осталось')
                meat = fridge("Мясо", me)
                print('Нажмите Enter чтобы начать с начала')
                comand = input()
                continue
        elif comand == '2' and me == 0:
            print('В холодильнике нет мяса')
            print('Нажмите Enter чтобы начать с начала')
            comand = input()
            continue

        if comand == '3' and not(c <= 0):
            print('Количество:')
            c_take = int(input())
            if c - c_take < 0:
                print('В холодильнике нет столько сыра', '\n', 'вы забираете то, что есть.')
                print('Вы забрали', c, 'кусочков')
                c *= 0
                cheese = fridge("Сыр", c)
                print('Нажмите Enter чтобы начать с начала')
                comand = input()
                continue
            elif c > c_take:
                print('Вы забрали', c_take, 'кусочков')
                c -= c_take
                print('Осталось', c, 'кусочков')
                cheese = fridge("Сыр", c)
                print('Нажмите Enter чтобы начать с начала')
                comand = input()
                continue
            else:
                print('Вы забрали', c, 'кусочков')
                c *= 0
                print('Сыра не осталось')
                cheese = fridge("Сыр", c)
                print('Нажмите Enter чтобы начать с начала')
                comand = input()
                continue
        elif comand == '3' and c == 0:
            print('В холодильнике нет сыра')
            print('Нажмите Enter чтобы начать с начала')
            comand = input()
            continue

        if comand == '4' and not(s <= 0):
            print('Количество:')
            s_take = int(input())
            if s - s_take < 0:
                print('В холодильнике нет столько вкусняшек', '\n', 'вы забираете то, что есть.')
                print('Вы забрали', s, 'вкусняшек')
                s *= 0
                sweet = fridge("Вкусняшка", s)
                print('Нажмите Enter чтобы начать с начала')
                comand = input()
                continue
            elif s > s_take:
                print('Вы забрали', s_take, 'вкусняшек')
                s -= s_take
                print('Осталось', s, 'вкусняшек')
                sweet = fridge("Вкусняшка", s)
                print('Нажмите Enter чтобы начать с начала')
                comand = input()
                continue
            else:
                print('Вы забрали', s, 'вкусняшек')
                s *= 0
                print('Вкусняшек не осталось')
                sweet = fridge("Вкусняшка", s)
                print('Нажмите Enter чтобы начать с начала')
                comand = input()
                continue
        elif comand == '4' and s == 0:
            print('В холодильнике нет вкусняшек')
            print('Нажмите Enter чтобы начать с начала')
            comand = input()
            continue

        if comand == '5' and not(B <= 0):
            print('Количество:')
            B_take = int(input())
            if B - B_take < 0:
                print('В холодильнике нет столько певка', '\n', 'вы забираете то, что есть.')
                print('Вы забрали', B, 'банок певка')
                B *= 0
                beer = fridge("Певко", B)
                print('Нажмите Enter чтобы начать с начала')
                comand = input()
                continue
            elif B > B_take:
                print('Вы забрали', B_take, 'банок певка')
                B -= B_take
                print('Осталось', B, 'банок певка')
                beer= fridge("Певко", B)
                print('Нажмите Enter чтобы начать с начала')
                comand = input()
                continue
            else:
                print('Вы забрали', B, 'банок певка')
                B *= 0
                print('Певка не осталось')
                beer= fridge("Певко", B)
                print('Нажмите Enter чтобы начать с начала')
                comand = input()
                continue
        elif comand == '5' and B == 0:
            print('В холодильнике нет банок певка')
            print('Нажмите Enter чтобы начать с начала')
            comand = input()
            continue

    elif comand == '4':
        break
