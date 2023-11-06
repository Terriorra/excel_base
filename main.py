from function import get_text_1
from function import get_text_2
from function import get_text_3

name = input('Как к тебе обращаться? ')
s = f'''
Приветстую тебя, {name}.

В данный момент времени в тренажёре существует три раздела.

Раздел один:
1. МАКС
2. МИН
3. СЧЁТ
4. СУММ
5. СРЗНАЧ

Раздел два:
1. НАИБОЛЬШИЙ
2. НАИМЕНЬШИЙ
3. Комбинирование функций
4. СЧЁТЕСЛИ
5. СУММЕСЛИ
6. СРЗНАЧЕСЛИ

Раздел три:
1. СЧЁТЕСЛИМН
2. СРЗНАЧЕСЛИМН
3. Сумма\Минимум\Максимум\Средние по двум столбцам с условиями
'''

print(s)

var = '0'

while var not in '123':

    var = input(f'Выбери раздел, {name}. [1/2/3] ').strip()

    match var:
        case '1':
            for var in range(1, 6):
                right = 0
                while right < 10:
                    text, q = get_text_1(var)
                    for i in text:
                        print(i)
                    print()
                    print(q)
                    
                    ant = input().strip()

                    if ant == q.ant:
                        right += 1
                        print(f'Верно! Осталось ответить {10 - right} раз.')
                    else:
                        right = 0
                        print(f'Не верно! Правильный ответ {q.ant}. Серия начинается заново.')
                    input("Для продолжения нажмите enter...")

                input('Уровень пройден! Для продолжения нажмите на enter...')

            text, q = get_text_1(6)

            print('\n'.join(text))

            var = 'end'
            input('Уровень пройден! Для продолжения нажмите на enter...')

        case '2':
            for var in range(1, 7):
                right = 0
                while right < 5:
                    text, q = get_text_2(var)
                    for i in text:
                        print(i)
                    print()
                    print(q)
                    ant = input().strip()

                    if ant == q.ant:
                        right += 1
                        print(f'Верно! Осталось ответить {5 - right} раз.')
                    else:
                        right = 0
                        print(f'Не верно! Правильный ответ {q.ant}. Серия начинается заново.')
                    input("Для продолжения нажмите enter...")

                input('Уровень пройден! Для продолжения нажмите на enter...')

            text, q = get_text_2(7)

            print('\n'.join(text))

            var = 'end'
            input('Уровень пройден! Для продолжения нажмите на enter...')

        case '3':
            for var in range(1, 4):
                right = 0
                while right < 5:
                    text, q = get_text_3(var)
                    for i in text:
                        print(i)
                    print()
                    print(q)
                    ant = input().strip()

                    if ant == q.ant:
                        right += 1
                        print(f'Верно! Осталось ответить {5 - right} раз.')
                    else:
                        right = 0
                        print(f'Не верно! Правильный ответ {q.ant}. Серия начинается заново.')
                    input("Для продолжения нажмите enter...")

                input('Уровень пройден! Для продолжения нажмите на enter...')

            text, q = get_text_3(7)

            print('\n'.join(text))

            var = 'end'
            input('Уровень пройден! Для продолжения нажмите на enter...')

        case _:
            print('Неизвестное значение...')
