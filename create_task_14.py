"""
Задание на ОГЭ - обработка большого массива данных

Генерируется таблица и три задания к ней.
"""
import os
import sys

from random import sample
from random import choice
from random import randint


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


path = resource_path('subject')
with open(path, 'r', encoding='utf-8') as f:
    subject = f.read().split('\n')

path = resource_path('district')
with open(path, 'r', encoding='utf-8') as f:
    district = f.read().split('\n')


class Quest:
    def __init__(self, text, ans):
        self.text = text
        self.ans = ans


class Task:
    def __init__(self, tabl, q1, q2, q3):
        self.tabl = tabl
        self.quest_1 = q1
        self.quest_2 = q2
        self.quest_3 = q3


def generate_tabl(n: int = 1000, tabl_type: int = 1):
    """
    Генерация таблицы
    :param tabl_type:
    :param n: Количество строк
    :return:
    """

    tabl = []

    match tabl_type:
        case 1:
            # Таблица с данными о тестировании учеников по выбранным ими предметам
            # В столбце A записан код округа, в котором учится ученик;
            # в столбце B — фамилия,
            # в столбце C — выбранный учеником предмет;
            # в столбце D — тестовый балл.

            a = sample(n * district, n)
            b = [f'Ученик {count}' for count in range(1, n + 1)]
            c = sample(n * subject, n)
            d = [randint(10, 1000) for _ in range(n)]

            tabl.append(['Код округа', 'Фамилия', 'Предмет', 'Балл'])

            for dis, j, k, m in zip(a, b, c, d):
                tabl.append([dis, j, k, m])
        case 2:
            # Таблица результатов тестирования учащихся по двум предметам из разных школ
            # В столбце А указаны фамилия и имя учащегося;
            # в столбце В — номер школы учащегося;
            # в столбцах С, D — баллы, полученные, по предметам.
            # По каждому предмету можно было набрать от 0 до 100 баллов.

            a = [f'Ученик {count}' for count in range(1, n + 1)]
            b = sample(list(range(1, 11)) * n, n)
            c = [randint(10, 100) for _ in range(n)]
            d = [randint(10, 100) for _ in range(n)]

            sub = sample(subject, 2)

            tabl.append(['Фамилия', 'Школа', sub[0].capitalize(), sub[1].capitalize()])

            for dis, j, k, m in zip(a, b, c, d):
                tabl.append([dis, j, k, m])
        case 3:
            # Таблица оценок за любимый предмет учеников из разных классов

            a = [f'Ученик {count}' for count in range(1, n + 1)]
            b = [randint(5, 11) for _ in range(n)]
            c = sample(n * subject, n)
            d = [randint(3, 5) for _ in range(n)]

            tabl.append(['Фамилия', 'Класс', 'Любимый предмет', 'Оценка за любимый предмет'])

            for dis, j, k, m in zip(a, b, c, d):
                tabl.append([dis, j, k, m])

        case 4:
            # Таблица с медицинского осмотра

            a = [f'Ученик {count}' for count in range(1, n + 1)]
            b = [randint(5, 11) for _ in range(n)]
            c = [randint(150, 200) for _ in range(n)]
            d = [randint(50, 80) for _ in range(n)]

            tabl.append(['Фамилия', 'Класс', 'Рост', 'Вес'])

            for dis, j, k, m in zip(a, b, c, d):
                tabl.append([dis, j, k, m])

        case 5:
            # Результаты сдачи выпускных экзаменов по n предметам

            sub = sample(subject, randint(3, 10))

            tabl.append(['Фамилия'] + [i.capitalize() for i in sub])

            a = [f'Ученик {count}' for count in range(1, n + 1)]

            grades = [len(sub) * [5]]
            for _ in a:
                grades.append([randint(2, 5) for _ in range(len(sub))])

            grades = sample(grades, len(a))

            for i in range(len(a)):
                line = [a[i]] + grades[i]
                tabl.append(line)
        case _:
            print('Не существующее значение')

    return tabl


def round_num(num):
    """
    Округлить число как в функции excel
    1.105 -> 1,11

    :param num:
    :return:
    """

    ant = str(round(num, 2))
    ant = ant.split('.')

    ant = ant[0] + ',' + (ant[1] + '000')[:2]

    b = str(round(num, 3)).split('.')

    if len(b[1]) > 2 and b[1][-1] == '5':
        ant = ant[:-1] + str(int(ant[-1]) + 1)

    return ant


def quest1_1(tabl):
    # Найти количество

    line = choice(tabl[1:])
    quest_type = choice([1, 2, 3])
    text = 'Определите, сколько учеников'
    x2 = line[3]
    x1 = []
    match quest_type:
        case 1:
            # Предмет
            x1 = line[2]
            text += f', которые проходили тестирование по предмету {x1}, '
        case 2:
            # Округ
            x1 = line[0]
            text += f' из округа {x1} '
        case 3:
            # Предмет Округ
            x1 = [line[0], line[2]]
            text += f' из округа {x1[0]}, которые проходили тестирование по предмету {x1[1]}, '

    var = choice([1, 2])
    match var:
        case 1:
            x2 -= 1
            text += f'набрали более {x2} баллов.'
        case 2:
            x2 += 1
            text += f'набрали менее {x2} баллов.'

    count = 0
    for i in tabl[1:]:
        if quest_type == 3:
            if (var == 1) and (i[3] > x2) and (i[0] == x1[0]) and (i[2] == x1[1]):
                count += 1
            elif (var == 2) and (i[3] < x2) and (i[0] == x1[0]) and (i[2] == x1[1]):
                count += 1

        else:
            if (var == 1) and (i[3] > x2):
                if (quest_type == 1) and (i[2] == x1):
                    count += 1
                else:
                    if i[0] == x1:
                        count += 1

            elif (var == 2) and (i[3] < x2):
                if (quest_type == 1) and (i[2] == x1):
                    count += 1
                else:
                    if i[0] == x1:
                        count += 1

    return Quest(text, count)


def quest1_2(tabl):
    # Найти среднее

    # Вопрос
    text = 'Найдите средний тестовый балл учеников'

    line = choice(tabl[1:])

    var_1 = choice([1, 2, 3])

    match var_1:
        case 1:
            # Предмет
            x1 = line[2]
            text += f', которые проходили тестирование по предмету {x1}.'
            tabl = list(filter(lambda x: x[2] == x1, tabl[1:]))

        case 2:
            # Округ
            x1 = line[0]
            text += f' из округа {x1}.'
            tabl = list(filter(lambda x: x[0] == x1, tabl[1:]))

        case 3:
            x1 = [line[0], line[2]]
            text += f' из округа {x1[0]}, которые проходили тестирование по предмету {x1[1]}.'
            tabl = list(filter(lambda x: (x[0] == x1[0]) and (x[2] == x1[1]), tabl[1:]))

    text += ' Ответ на этот вопрос запишите с точностью двух знаков после запятой.'

    tabl = [i[-1] for i in tabl]
    ans = sum(tabl) / len(tabl)

    return Quest(text, round_num(ans))


def quest1_3(tabl):
    text = ''
    ans = []

    match choice([1, 2]):
        case 1:
            x1 = sample(
                list(set([i[2] for i in tabl[1:]])),
                3)
            text += (f'Постройте круговую диаграмму, отображающую соотношение числа участников, '
                     f'сдающих предметы: {", ".join(x1)}.')
            for i in x1:
                ans.append(len(list(filter(lambda x: x[2] == i, tabl))))

        case 2:
            x1 = sample(
                list(set([i[0] for i in tabl[1:]])),
                3)
            text += (f'Постройте круговую диаграмму, отображающую соотношение числа участников'
                     f' из округов с кодами: {", ".join(x1)}.')

            for i in x1:
                ans.append(len(list(filter(lambda x: x[0] == i, tabl))))

    return Quest(text, ans)


def quest2_1(tabl):
    head = tabl[0]
    tabl = tabl[1:]
    line = choice(tabl[1:])

    text = ''
    ans = ''
    match choice(range(1, 16)):
        case 1:
            text += (f'Сколько учащихся школы № {line[1]} набрали по предмету {head[2]} '
                     f'больше баллов, чем по предмету {head[3]}?')
            tabl = list(filter(lambda x: (x[1] == line[1]) and (x[2] > x[3]), tabl))
            ans = len(tabl)
        case 2:
            text += (f'Сколько учащихся школы № {line[1]} набрали по предмету {head[3]} '
                     f'больше баллов, чем по предмету {head[2]}?')
            tabl = list(filter(lambda x: (x[1] == line[1]) and (x[3] > x[2]), tabl))
            ans = len(tabl)
        case 3:
            text += (f'Сколько учащихся школы № {line[1]} набрали по предмету {head[2]} '
                     f'меньше баллов, чем по предмету {head[3]}?')
            tabl = list(filter(lambda x: (x[0] == line[1]) and (x[2] < x[3]), tabl))
            ans = len(tabl)
        case 4:
            text += (f'Сколько учащихся школы № {line[1]} набрали по предмету {head[3]} '
                     f'меньше баллов, чем по предмету {head[2]}?')
            tabl = list(filter(lambda x: (x[1] == line[1]) and (x[3] < x[2]), tabl))
            ans = len(tabl)
        case 5:
            text += (f'Чему равна наименьшая сумма баллов по двум предметам среди школьников, '
                     f'получивших больше {line[2] - 1} баллов по предмету {head[2]} или предмету {head[3]}?')
            tabl = list(filter(lambda x: (x[2] > line[2] - 1) or (x[3] > line[2] - 1), tabl))
            if len(tabl) > 1:
                ans = min([i[2] + i[3] for i in tabl])
            else:
                ans = 0
        case 6:
            text += (f'Чему равна наименьшая сумма баллов по двум предметам среди школьников, '
                     f'получивших больше {line[2] - 1} баллов по предмету {head[2]} и предмету {head[3]}?')
            tabl = list(filter(lambda x: (x[2] > line[2] - 1) and (x[3] > line[2] - 1), tabl))
            if len(tabl) > 1:
                ans = min([i[2] + i[3] for i in tabl])
            else:
                ans = 0
        case 7:
            text += (f'Чему равна наибольшая сумма баллов по двум предметам среди школьников, '
                     f'получивших больше {line[2] - 1} баллов по предмету {head[2]} или предмету {head[3]}?')
            tabl = list(filter(lambda x: (x[2] > line[2] - 1) or (x[3] > line[2] - 1), tabl))
            if len(tabl) > 1:
                ans = max([i[2] + i[3] for i in tabl])
            else:
                ans = 0
        case 8:
            text += (f'Чему равна наибольшая сумма баллов по двум предметам среди школьников, '
                     f'получивших больше {line[2] - 1} баллов по предмету {head[2]} и предмету {head[3]}?')
            tabl = list(filter(lambda x: (x[2] > line[2] - 1) and (x[3] > line[2] - 1), tabl))
            if len(tabl) > 1:
                ans = max([i[2] + i[3] for i in tabl])
            else:
                ans = 0
        case 9:
            text += (f'Чему равна средняя сумма баллов по двум предметам среди школьников, '
                     f'получивших больше {line[2] - 1} баллов по предмету {head[2]} или предмету {head[3]}? '
                     f'Ответ записать с точностью до двух знаков после запятой.')
            tabl = list(filter(lambda x: (x[2] > line[2] - 1) or (x[3] > line[2] - 1), tabl))
            if len(tabl) > 0:
                ans = [i[2] + i[3] for i in tabl]
                ans = round_num(sum(ans) / len(ans))
            else:
                ans = 0
        case 10:
            text += (f'Чему равна средняя сумма баллов по двум предметам среди школьников, '
                     f'получивших больше {line[2] - 1} баллов по предмету {head[2]} и предмету {head[3]}? '
                     f'Ответ записать с точностью до двух знаков после запятой.')
            tabl = list(filter(lambda x: (x[2] > line[2] - 1) and (x[3] > line[2] - 1), tabl))
            if len(tabl) > 0:
                ans = [i[2] + i[3] for i in tabl]
                ans = round_num(sum(ans) / len(ans))
            else:
                ans = 0

        case 11:
            text += (f'Чему равна наименьшая сумма баллов по двум предметам среди школьников, '
                     f'получивших меньше {line[2] + 1} баллов по предмету {head[2]} и предмету {head[3]}?')
            tabl = list(filter(lambda x: (x[2] < line[2] + 1) and (x[3] < line[2] + 1), tabl))
            if len(tabl) > 1:
                ans = min([i[2] + i[3] for i in tabl])
            else:
                ans = 0
        case 12:
            text += (f'Чему равна наибольшая сумма баллов по двум предметам среди школьников, '
                     f'получивших меньше {line[2] + 1} баллов по предмету {head[2]} или предмету {head[3]}?')
            tabl = list(filter(lambda x: (x[2] < line[2] + 1) or (x[3] < line[2] + 1), tabl))
            if len(tabl) > 1:
                ans = max([i[2] + i[3] for i in tabl])
            else:
                ans = 0
        case 13:
            text += (f'Чему равна наибольшая сумма баллов по двум предметам среди школьников, '
                     f'получивших меньше {line[2] + 1} баллов по предмету {head[2]} и предмету {head[3]}?')
            tabl = list(filter(lambda x: (x[2] < line[2] + 1) and (x[3] < line[2] + 1), tabl))
            if len(tabl) > 1:
                ans = max([i[2] + i[3] for i in tabl])
            else:
                ans = 0
        case 14:
            text += (f'Чему равна средняя сумма баллов по двум предметам среди школьников, '
                     f'получивших меньше {line[2] + 1} баллов по предмету {head[2]} или предмету {head[3]}? '
                     f'Ответ записать с точностью до двух знаков после запятой.')
            tabl = list(filter(lambda x: (x[2] < line[2] + 1) or (x[3] < line[2] + 1), tabl))
            if len(tabl) > 1:
                ans = [i[2] + i[3] for i in tabl]
                ans = round_num(sum(ans) / len(ans))
            else:
                ans = 0
        case 15:
            text += (f'Чему равна средняя сумма баллов по двум предметам среди школьников, '
                     f'получивших меньше {line[2] + 1} баллов по предмету {head[2]} и предмету {head[3]}? '
                     f'Ответ записать с точностью до двух знаков после запятой.')
            tabl = list(filter(lambda x: (x[2] < line[2] + 1) and (x[3] < line[2] + 1), tabl))
            if len(tabl) > 1:
                ans = [i[2] + i[3] for i in tabl]
                ans = round_num(sum(ans) / len(ans))
            else:
                ans = 0

    return Quest(text, ans)


def quest2_2(tabl):
    head = tabl[0]
    line = choice(tabl[1:])
    tabl = tabl[1:]
    col = len(tabl)

    text = ''

    match choice(range(1, 6)):
        case 1:
            text += (f'Сколько процентов от общего числа участников составили ученики, '
                     f'получившие по предмету {head[2]} больше {line[2] - 1} баллов? '
                     f'Ответ записать с точностью до двух знаков после запятой.')
            tabl = list(filter(lambda x: x[2] > line[2] - 1, tabl))

        case 2:
            text += (f'Сколько процентов от общего числа участников составили ученики школы № {line[1]}? '
                     f'Ответ записать с точностью до двух знаков после запятой.')
            tabl = list(filter(lambda x: x[1] == line[1], tabl))

        case 3:
            text += (f'Сколько процентов от общего числа участников составили ученики, '
                     f'получившие по предмету {head[3]} больше {line[3] - 1} баллов? '
                     f'Ответ записать с точностью до двух знаков после запятой.')
            tabl = list(filter(lambda x: x[3] > line[3] - 1, tabl))

        case 4:
            text += (f'Сколько процентов от общего числа участников составили ученики, '
                     f'получившие по предмету {head[2]} меньше {line[2] + 1} баллов? '
                     f'Ответ записать с точностью до двух знаков после запятой.')
            tabl = list(filter(lambda x: x[2] < line[2] + 1, tabl))

        case 5:
            text += (f'Сколько процентов от общего числа участников составили ученики, '
                     f'получившие по предмету {head[3]} меньше {line[3] + 1} баллов? '
                     f'Ответ записать с точностью до двух знаков после запятой.')
            tabl = list(filter(lambda x: x[3] < line[3] + 1, tabl))

    ans = len(tabl) / col * 100

    return Quest(text, round_num(ans))


def quest2_3(tabl):
    tabl = tabl[1:]

    text = 'Постройте круговую диаграмму, отображающую соотношение учеников из школ под номерами: '

    num_school = list(set([i[1] for i in tabl]))
    num_school = sample(num_school, randint(2, min(5, len(num_school) - 1)))

    text += f"{', '.join([str(i) for i in num_school])}."

    ans = []
    for num in num_school:
        ans.append(len(list(filter(lambda x: x[1] == num, tabl))))

    return Quest(text, ans)


def quest3_1(tabl):
    tabl = tabl[1:]
    line = choice(tabl)

    text = ''

    match choice(range(1, 8)):
        case 1:
            text += f'Сколько учеников любят предмет {line[2]}?'
            tabl = filter(lambda x: x[2] == line[2], tabl)
        case 2:
            text += f'Сколько учеников в {line[1]} классе любят предмет {line[2]}?'
            tabl = filter(lambda x: (x[1] == line[1]) and (x[2] == line[2]), tabl)
        case 3:
            text += f'Сколько учеников получили за любимый предмет {line[3]}?'
            tabl = filter(lambda x: x[3] == line[3], tabl)
        case 4:
            text += f'Сколько учеников получили за любимый предмет меньше {min([5, line[3] + 1])} баллов?'
            tabl = filter(lambda x: x[3] < min([5, line[3] + 1]), tabl)
        case 5:
            text += f'Сколько учеников получили за любимый предмет больше {max([3, line[3] - 1])} баллов?'
            tabl = filter(lambda x: x[3] > max([3, line[3] - 1]), tabl)
        case 6:
            text += f'Сколько учеников в {line[1]} классе получили меньше {min([5, line[3] + 1])} баллов?'
            tabl = filter(lambda x: (x[3] < min([5, line[3] + 1])) and (x[1] == line[1]), tabl)
        case 7:
            text += f'Сколько учеников в {line[1]} классе получили больше {max([3, line[3] - 1])} баллов?'
            tabl = filter(lambda x: (x[1] == line[1]) and (x[3] > max([3, line[3] - 1])), tabl)

    ans = len(list(tabl))
    return Quest(text, ans)


def quest3_2(tabl):
    tabl = tabl[1:]
    line = choice(tabl)

    text = ''
    len_1 = len(tabl)

    match choice(range(1, 6)):
        case 1:
            grades = sample([3, 4, 5], 2)
            text += (f'Какой процент учеников {line[1]} класса имеют за любимый предмет оценку'
                     f' {grades[0]} или {grades[1]}? Ответ записать с точностью до двух знаков после запятой.')
            tabl = list(filter(lambda x: x[1] == line[1], tabl))
            len_1 = len(tabl)
            tabl = list(filter(lambda x: (x[3] == grades[0]) or (x[3] == grades[1]), tabl))

        case 2:
            text += (f'Какой процент учеников {line[1]} класса имеют оценку {line[3]} за любимый предмет? '
                     f'Ответ записать с точностью до двух знаков после запятой.')
            tabl = list(filter(lambda x: x[1] == line[1], tabl))
            len_1 = len(tabl)
            tabl = list(filter(lambda x: x[3] == line[3], tabl))

        case 3:
            text += (f'Какой процент учеников {line[1]} класса выбрали предмет {line[2]}? '
                     f'Ответ записать с точностью до двух знаков после запятой.')
            tabl = list(filter(lambda x: x[1] == line[1], tabl))
            len_1 = len(tabl)
            tabl = list(filter(lambda x: x[2] == line[2], tabl))

        case 4:
            text += (f'Какой процент учеников выбрали предмет {line[2]}? '
                     f'Ответ записать с точностью до двух знаков после запятой.')
            tabl = list(filter(lambda x: x[2] == line[2], tabl))

        case 5:
            text += (f'Какой процент учеников имеют оценку {line[3]} за любимый предмет? '
                     f'Ответ записать с точностью до двух знаков после запятой.')
            tabl = list(filter(lambda x: x[3] == line[3], tabl))

    len_2 = len(tabl)
    ans = round_num(len_2 / len_1 * 100)

    return Quest(text, ans)


def quest3_3(tabl):
    tabl = tabl[1:]

    text = ''
    ans = []

    match choice(range(1, 4)):
        case 1:
            sub = list(set([i[2] for i in tabl]))
            sub = sample(sub, randint(3, min(6, len(sub))))
            text += (f'Постройте круговую диаграмму, отображающую соотношение любимых предметов: '
                     f'{", ".join(sub)}.')
            for i in sub:
                ans.append(len(list(filter(lambda x: x[2] == i, tabl))))
        case 2:
            grade = sample([3, 4, 5], randint(2, 3))
            text += (f'Постройте круговую диаграмму, отображающую соотношение '
                     f'полученных оценок {", ".join([str(i) for i in grade])} за любимые предметы.')

            for i in grade:
                ans.append(len(list(filter(lambda x: x[3] == i, tabl))))

        case 3:
            cl = list(set([i[1] for i in tabl]))
            cl = sample(cl, randint(3, min(6, len(cl))))
            text += (f'Постройте круговую диаграмму, отображающую соотношение классов:  '
                     f'{", ".join(([str(i) for i in cl]))}.')
            for i in cl:
                ans.append(len(list(filter(lambda x: x[1] == i, tabl))))

    return Quest(text, ans)


def quest4_1(tabl):
    tabl = tabl[1:]

    line = choice(tabl)
    tabl = list(filter(lambda x: x[1] == line[1], tabl))

    text = ''
    ans = ''

    match choice(range(1, 5)):
        case 1:
            text += f'Каков вес самого тяжелого ученика {line[1]} класса?'
            tabl = [i[3] for i in tabl]
            ans = max(tabl)

        case 2:
            text += f'Каков вес самого лёгкого ученика {line[1]} класса?'
            tabl = [i[3] for i in tabl]
            ans = min(tabl)

        case 3:
            text += f'Каков рост самого высокого ученика {line[1]} класса?'
            tabl = [i[2] for i in tabl]
            ans = max(tabl)

        case 4:
            text += f'Каков рост самого низкого ученика {line[1]} класса?'
            tabl = [i[2] for i in tabl]
            ans = min(tabl)

    return Quest(text, ans)


def quest4_2(tabl):
    tabl = tabl[1:]
    line = choice(tabl)

    text = 'Какой процент учеников '

    len_1 = len(tabl)

    choice([f'{line[1]} класса', ''])

    match choice(range(1, 3)):
        case 1:
            text += f'{line[1]} класса имеет '
            tabl = list(filter(lambda x: x[1] == line[1], tabl))
            len_1 = len(tabl)
        case 2:
            text += f'имеет '

    match choice(range(1, 4)):
        case 1:
            text += 'вес '
            match choice(range(1, 3)):
                case 1:
                    d = line[3] - 1
                    text += f'больше {d}?'
                    tabl = list(filter(lambda x: x[3] > d, tabl))
                case 2:
                    d = line[3] + 1
                    text += f'меньше {d}?'
                    tabl = list(filter(lambda x: x[3] < d, tabl))

        case 2:
            text += 'рост '
            match choice(range(1, 3)):
                case 1:
                    d = line[2] - 1
                    text += f'больше {d}?'
                    tabl = list(filter(lambda x: x[2] > d, tabl))
                case 2:
                    d = line[2] + 1
                    text += f'меньше {d}?'
                    tabl = list(filter(lambda x: x[2] < d, tabl))

        case 3:
            a = sample([['вес', 3], ['рост', 2]], 2)
            b = sample(2 * [['больше', '-', '>'], ['меньше', '+', '<']], 2)
            c = choice([['и', 'and'], ['или', 'or']])

            d = [eval(f'{line[a[0][1]]} {b[0][1]} 1'), eval(f'{line[a[1][1]]} {b[1][1]} 1')]

            text += f'{a[0][0]} {b[0][0]} {d[0]} {c[0]} {a[1][0]} {b[1][0]} {d[1]}?'

            tabl = list(filter(lambda x:
                               eval(f'({x[a[0][1]]} {b[0][2]} {d[0]}) {c[1]} ({x[a[1][1]]} {b[1][2]} {d[1]})'),
                               tabl))

    text += ' Ответ записать с точностью до двух знаков после запятой.'

    len_2 = len(tabl)
    ans = round_num(len_2 / len_1 * 100)

    return Quest(text, ans)


def quest4_3(tabl):
    tabl = tabl[1:]

    text = 'Постройте круговую диаграмму, отображающую соотношение учеников из классов: '
    ans = []

    cl = list(set([i[1] for i in tabl]))
    cl = sample(cl, randint(3, min(6, len(cl))))

    text += f'{", ".join([str(i) for i in cl])}.'

    for i in cl:
        ans.append(len(list(filter(lambda x: x[1] == i, tabl))))

    return Quest(text, ans)


def quest5_1(tabl):
    tabl = tabl[1:]

    text = 'Какое количество учащихся получило '

    match choice(range(1, 4)):
        case 1:
            text += f'удовлетворительные оценки (то есть оценки выше 2) на всех экзаменах?'
            tabl = list(filter(lambda x: sum([i > 2 for i in x[1:]]) == len(x[1:]), tabl))
        case 2:
            text += f'хорошие оценки (то есть оценки выше 3) на всех экзаменах?'
            tabl = list(filter(lambda x: sum([i > 3 for i in x[1:]]) == len(x[1:]), tabl))
        case 3:
            text += f'отличные оценки (то есть оценки выше 4) на всех экзаменах?'
            tabl = list(filter(lambda x: sum([i > 4 for i in x[1:]]) == len(x[1:]), tabl))

    ans = len(tabl)

    return Quest(text, ans)


def quest5_2(tabl):
    head = tabl[0]
    tabl = tabl[1:]

    sub = choice([(j, i) for i, j in enumerate(head[1:], 1)])

    text = 'Для группы учащихся, которые получили '

    match choice(range(1, 4)):
        case 1:
            text += f'удовлетворительные оценки (то есть оценки выше 2)'
            tabl = list(filter(lambda x: sum([i > 2 for i in x[1:]]) == len(x[1:]), tabl))
        case 2:
            text += f'хорошие оценки (то есть оценки выше 3)'
            tabl = list(filter(lambda x: sum([i > 3 for i in x[1:]]) == len(x[1:]), tabl))
        case 3:
            text += f'отличные оценки (то есть оценки выше 4)'
            tabl = list(filter(lambda x: sum([i > 4 for i in x[1:]]) == len(x[1:]), tabl))

    sum_grade = sum([i[sub[1]] for i in tabl])

    text += f' на всех экзаменах, посчитайте средний балл, полученный ими на экзамене по предмету {sub[0]}.'

    ans = 0

    if len(tabl) > 1:
        ans = round_num(sum_grade / len(tabl))

    return Quest(text, ans)


def quest5_3(tabl):
    head = tabl[0]
    tabl = tabl[1:]

    sub = choice([(j, i) for i, j in enumerate(head[1:], 1)])
    grade = sample([2, 3, 4, 5], randint(2, 4))

    text = (f'Постройте круговую диаграмму, отображающую соотношение количество оценок '
            f'{", ".join([str(i) for i in grade])} по предмету {sub[0]}.')

    ans = []
    for i in grade:
        ans.append(len(list(filter(lambda x: x[sub[1]] == i, tabl))))

    return Quest(text, ans)


def generate_task(n: int = 1000, task_type: int = 1):
    """
    Создание заданий по таблице
    :param n: количество строк
    :param task_type: тип
    :return:
    """

    tabl = generate_tabl(n, task_type)
    task = ''

    match task_type:
        case 1:
            # Таблица 'Код округа', 'Фамилия', 'Предмет', 'Балл'
            q1 = quest1_1(tabl)
            q2 = quest1_2(tabl)
            q3 = quest1_3(tabl)
            task = Task(tabl, q1, q2, q3)

        case 2:
            # Таблица 'Фамилия', 'Школа', 'Предмет 1', 'Предмет 2'
            q1 = quest2_1(tabl)
            while q1.ans == 0:
                q1 = quest2_1(tabl)

            q2 = quest2_2(tabl)
            while (q2.ans == '0,00') or (q2.ans == '100,00'):
                q2 = quest2_2(tabl)

            q3 = quest2_3(tabl)

            task = Task(tabl, q1, q2, q3)

        case 3:
            # Таблица 'Фамилия', 'Класс', 'Любимый предмет', 'Оценка за любимый предмет'
            q1 = quest3_1(tabl)

            q2 = quest3_2(tabl)
            while (q2.ans == '0,00') or (q2.ans == '100,00'):
                q2 = quest3_2(tabl)

            q3 = quest3_3(tabl)
            task = Task(tabl, q1, q2, q3)

        case 4:
            # Таблица 'Фамилия', 'Класс', 'Рост', 'Вес'
            q1 = quest4_1(tabl)

            q2 = quest4_2(tabl)
            while (q2.ans == '0,00') or (q2.ans == '100,00'):
                q2 = quest4_2(tabl)

            q3 = quest4_3(tabl)
            task = Task(tabl, q1, q2, q3)

        case 5:
            # Таблица 'Фамилия', 'Предмет 1', 'Предмет 2', 'Предмет 3', 'Предмет 4'
            q1 = quest5_1(tabl)
            while q1.ans == 0:
                q1 = quest5_1(tabl)

            q2 = quest5_2(tabl)
            while q2.ans == 0:
                q2 = quest5_2(tabl)

            q3 = quest5_3(tabl)

            task = Task(tabl, q1, q2, q3)

    return task
