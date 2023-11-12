from function import get_text_1
from function import get_text_2
from function import get_text_3
from function import get_text_4

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

Раздел четыре:
Генерация задания № 14 
'''

print(s)

var = '0'

while var not in '1234':

    var = input(f'Выбери раздел, {name}. [1/2/3/4] ').strip()

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

        case '4':
            text, task, grades = get_text_4()
            for i in text:
                print(i)

            print()
            tabl = task.tabl
            for i in tabl:
                print(';'.join([str(j) for j in i]))

            ans = 0
            print('\nОтветьте на вопросы:')

            ant = input(f'{task.quest_1.text}\n').strip()
            if ant == str(task.quest_1.ans):
                ans += 1
                print('Верно!\n')
            else:
                print(f'Не верно. Верный ответ: {task.quest_1.ans}\n')

            ant = input(f'{task.quest_2.text}\n').strip()
            if ant == str(task.quest_2.ans):
                ans += 1
                print('Верно!\n')
            else:
                print(f'Не верно. Верный ответ: {task.quest_2.ans}\n')

            match ans:
                case 0:
                    print('Текущая оценка 1')
                case 1:
                    print('Текущая оценка 2')
                case 2:
                    print("Текущая оценка 3")


            ans_3 = 0
            print(f'{task.quest_3.text}')
            for i, a in enumerate(task.quest_3.ans, 1):
                ant = input(f'Число участников для параметра {i}: ').strip()
                if ant == str(a):
                    ans_3 += 1
                    print('Верно!\n')
                else:
                    print(f'Не верно. Верный ответ: {a}\n')

            if ans_3 == i:
                ans += 1

            match ans:
                case 0:
                    print('Текущая оценка 1')
                case 1:
                    print('Текущая оценка 2')
                case 2:
                    print("Текущая оценка 3")
                case 3:
                    print('Текущая оценка 4')


            for i in grades[ans + 1]:
                print(i)

            print('Плюс балл можно получить за демонстрацию диаграммы.')

            var = input('Конец тестирования. ').strip().lower()

        case _:
            print('Неизвестное значение...')
