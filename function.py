import os
import sys

from random import choice
from random import sample
from random import randint

sign_hor = '═'
sign_vert = '║'
LINE_LEN = 90


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


path = resource_path('about_1.txt')
with open(path, 'r', encoding='utf-8') as f:
    about_1 = f.read().split('\n\n\n')

path = resource_path('about_2.txt')
with open(path, 'r', encoding='utf-8') as f:
    about_2 = f.read().split('\n\n\n')

path = resource_path('subject')
with open(path, 'r', encoding='utf-8') as f:
    subject = f.read().split('\n')

path = resource_path('district')
with open(path, 'r', encoding='utf-8') as f:
    district = f.read().split('\n')


def print_text(text, len_string):
    s = [f" {(len_string - 2) * sign_hor} ", f"{sign_vert}{(len_string - 2) * ' '}{sign_vert}"]

    for line in text:
        if len(line) + 4 < len_string:
            s.append(f"{sign_vert} {line}{(len_string - len(line) - 4) * ' '} {sign_vert}")
        else:
            s += cut_string(line, len_string)
    s.append(f"{sign_vert}{(len_string - 2) * ' '}{sign_vert}")
    s.append(f" {(len_string - 2) * sign_hor} ")

    return s


def cut_string(text, len_string):
    s = []

    text = text.split(' ')
    lines = []
    now = ''
    for i in text:
        if len(now + ' ' + i) < len_string - 4:
            now += ' ' + i
        else:
            lines.append(now)
            now = i
    lines.append(now)

    for line in lines:
        s.append(f"{sign_vert} {line}{(len_string - 4 - len(line)) * ' '} {sign_vert}")

    return s


class Quest:

    def __init__(self, quest, ant):
        """
        :param quest: Вопрос
        :param ant: Ответ
        """
        self.quest = quest
        self.ant = ant

    def __str__(self):
        return self.quest


def create_rnd_list(min_length: int = 10,
                    max_length: int = 20,
                    min_val: int = 10,
                    max_val: int = 200) -> list[int]:
    """
    Создать список целых чисел случайной длины
    :param min_val: минимальное значение списка
    :param max_val: максимальное значение списка
    :param min_length: минимальная длина списка
    :param max_length: максимальная длина списка
    :return:
    """
    len_list = choice(range(min_length, max_length))
    rnd_list = [randint(min_val, max_val) for _ in range(len_list)]

    return rnd_list


def max_val_list():
    """
    Найти наибольшее значение в списке.
    :return:
    """

    new_list = create_rnd_list()

    s = '\n'
    s += '\n'.join([str(i) for i in new_list])
    s += '\n\nВведите максимальное значение из списка.'

    q = Quest(s, str(max(new_list)))

    return q


def min_val_list():
    """
    Найти минимальное значение в списке.
    :return:
    """

    new_list = create_rnd_list()

    s = '\n'
    s += '\n'.join([str(i) for i in new_list])
    s += '\n\nВведите минимальное значение из списка.'

    q = Quest(s, str(min(new_list)))

    return q


def count_num_list():
    """
    Найти количество цифр в списке
    :return:
    """

    new_list = create_rnd_list()

    len_list = len(new_list)

    s = sample(8 * '!@#$%^&*()QWERTY asdfg', randint(10, 30))
    s += [str(i) for i in new_list]
    s = sample(s, len(s))

    s_1 = '\n'
    s_1 += '\n'.join(s)
    s_1 += '\n\nВведите количество чисел в списке.'

    q = Quest(s_1, str(len_list))

    return q


def sum_list():
    """
    Сумма чисел списка
    :return:
    """

    new_list = create_rnd_list()

    s = '\n'
    s += '\n'.join([str(i) for i in new_list])
    s += '\n\nВведите сумму чисел списка.'

    q = Quest(s, str(sum(new_list)))

    return q


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


def mean_list():
    """
    Среднее значение чисел списка
    :return:
    """

    new_list = create_rnd_list()

    s = '\n'
    s += '\n'.join([str(i) for i in new_list])
    s += '\n\nВведите среднее значение чисел списка.'

    ant = round_num(sum(new_list) / len(new_list))

    q = Quest(s, ant)

    return q


def max_n_num():
    """
    n-й элемент сортированного по убыванию списка.
    :return:
    """

    new_list = create_rnd_list()

    n = randint(1, 8)

    s = '\n'
    s += '\n'.join([str(i) for i in new_list])
    s += f'\n\nВведите {n}-элемент отсортированного по убыванию списка.'

    ant = sorted(new_list, reverse=True)[n - 1]

    q = Quest(s, str(ant))

    return q


def min_n_num():
    """
    n-й элемент сортированного по возрастанию списка.
    :return:
    """

    new_list = create_rnd_list()

    n = randint(1, 8)

    s = '\n'
    s += '\n'.join([str(i) for i in new_list])
    s += f'\n\nВведите {n}-элемент отсортированного по возрастанию списка.'

    ant = sorted(new_list, reverse=False)[n - 1]

    q = Quest(s, str(ant))

    return q


def sum_n_list():
    """
    Сумма n_i, n_i+1 элементов массива
    :return:
    """

    new_list = create_rnd_list()

    n = sample(range(1, len(new_list) - 2), randint(3, 6))

    s = '\n'
    s += '\n'.join([str(i) for i in new_list])
    s += f"\n\nВведите сумму для {';'.join([str(i) for i in n])} -элементов отсортированного по возрастанию списка."

    new_list.sort(reverse=True)

    ant = 0
    for i in n:
        ant += new_list[i - 1]

    q = Quest(s, str(ant))

    return q


def create_tabl_school(n: int = 1000):
    """
    В столбце A записан код округа, в котором учится ученик;
    в столбце B - id ученика,
    в столбце C - выбранный учеником предмет;
    в столбце D - тестовый балл.

    Всего в электронную таблицу были занесены данные по 1000 учеников.
    :param n: Количество строк
    :return:
    """

    a = sample(n * district, n)
    b = sample(range(10, n * 1000), n)
    c = sample(n * subject, n)
    d = [randint(100, 300) for _ in range(n)]

    tabl = 'A;B;C;D\n'
    for i, j, k, l in zip(a, b, c, d):
        tabl += i + ';' + str(j) + ';' + k + ';' + str(l) + '\n'

    return tabl


def mean_if(n: int = 1000):
    """
    Средние значение при условии
    :param n: количество строк в таблице
    :return:
    """
    tabl = create_tabl_school(n)

    my_tabl = tabl.split('\n')[1:-1]
    first_line = choice(my_tabl).split(';')

    var = choice([1, 2, 3, 4])
    s = 'Найди среднее значение учеников'

    count = 0
    sum_var = 0

    match var:
        case 1:
            # Округ
            var = first_line[0]
            s += f' из округа {var}.'

            for i in my_tabl:
                i = i.split(';')
                if len(i) > 1 and var in i:
                    count += 1
                    sum_var += int(i[3])

        case 2:
            # Предмет
            var = first_line[2]
            s += f' выбравших предмет {var}.'

            for i in my_tabl:
                i = i.split(';')
                if len(i) > 1 and var in i:
                    count += 1
                    sum_var += int(i[3])

        case 3:
            # Балл больше
            var = int(first_line[3]) - 1
            s += f' набравших больше {var} баллов.'

            for i in my_tabl:
                i = i.split(';')
                if len(i) > 1 and var < int(i[3]):
                    count += 1
                    sum_var += int(i[3])

        case 4:
            # Балл меньше
            var = int(first_line[3]) + 1
            s += f' набравших меньше {var} баллов.'

            for i in my_tabl:
                i = i.split(';')
                if len(i) > 1 and var > int(i[3]):
                    count += 1
                    sum_var += int(i[3])

    ant = round_num(sum_var / count)

    q = Quest(s + '\n\n' + tabl, ant)

    return q


def sum_if(n: int = 1000):
    """
    Сумма значений при условии
    :param n: количество строк в таблице
    :return:
    """
    tabl = create_tabl_school(n)

    my_tabl = tabl.split('\n')[1:-1]
    first_line = choice(my_tabl).split(';')

    var = choice([1, 2, 3, 4])
    s = 'Найди сумму баллов учеников'

    sum_var = 0

    match var:
        case 1:
            # Округ
            var = first_line[0]
            s += f' из округа {var}.'

            for i in my_tabl:
                i = i.split(';')
                if len(i) > 1 and var in i:
                    sum_var += int(i[3])

        case 2:
            # Предмет
            var = first_line[2]
            s += f' выбравших предмет {var}.'

            for i in my_tabl:
                i = i.split(';')
                if len(i) > 1 and var in i:
                    sum_var += int(i[3])

        case 3:
            # Балл больше
            var = int(first_line[3]) - 1
            s += f' набравших больше {var} баллов.'

            for i in my_tabl:
                i = i.split(';')
                if len(i) > 1 and var < int(i[3]):
                    sum_var += int(i[3])

        case 4:
            # Балл меньше
            var = int(first_line[3]) + 1
            s += f' набравших меньше {var} баллов.'

            for i in my_tabl:
                i = i.split(';')
                if len(i) > 1 and var > int(i[3]):
                    sum_var += int(i[3])

    q = Quest(s + '\n\n' + tabl, str(sum_var))

    return q


def count_if(n: int = 1000):
    """
    Количество значений при условии
    :param n: количество строк в таблице
    :return:
    """
    tabl = create_tabl_school(n)

    my_tabl = tabl.split('\n')[1:-1]
    first_line = choice(my_tabl).split(';')

    var = choice([1, 2, 3, 4])
    s = 'Найди количество учеников'

    count = 0

    match var:
        case 1:
            # Округ
            var = first_line[0]
            s += f' из округа {var}.'

            for i in my_tabl:
                i = i.split(';')
                if var in i:
                    count += 1

        case 2:
            # Предмет
            var = first_line[2]
            s += f' выбравших предмет {var}.'

            for i in my_tabl:
                i = i.split(';')
                if var in i:
                    count += 1

        case 3:
            # Балл больше
            var = int(first_line[3]) - 1
            s += f' набравших больше {var} баллов.'

            for i in my_tabl:
                i = i.split(';')
                if (len(i) > 1) and (var < int(i[3])):
                    count += 1

        case 4:
            # Балл меньше
            var = int(first_line[3]) + 1
            s += f' набравших меньше {var} баллов.'

            for i in my_tabl:
                i = i.split(';')
                if (len(i) > 1) and (var > int(i[3])):
                    count += 1

    q = Quest(s + '\n\n' + tabl, str(count))

    return q


def get_text_1(var):
    """
    Создать текст задания первого блока
    :param var:
    :return:
    """
    os.system("CLS")

    text = print_text(about_1[0].split('\n'), LINE_LEN)

    q = ''

    match var:
        case 1:
            # Максимум
            text += print_text(about_1[1].split("\n"), LINE_LEN)
            q = max_val_list()

        case 2:
            # Минимум
            text += print_text(about_1[2].split('\n'), LINE_LEN)
            q = min_val_list()

        case 3:
            # Cчёт
            text += print_text(about_1[3].split('\n'), LINE_LEN)
            q = count_num_list()

        case 4:
            # Сумма
            text += print_text(about_1[4].split('\n'), LINE_LEN)
            q = sum_list()

        case 5:
            # Среднее
            text += print_text(about_1[5].split('\n'), LINE_LEN)
            q = mean_list()

        case 6:
            text += about_1[6].split('\n')
            q = ''

    return text, q


def get_text_2(var):
    """
    Создать текст задания второго блока
    :param var:
    :return:
    """

    os.system("CLS")

    text = print_text(about_2[0].split('\n'), LINE_LEN)

    q = ''

    match var:
        case 1:
            # Наибольший
            text += print_text(about_2[1].split('\n'), LINE_LEN)
            q = max_n_num()

        case 2:
            # Наименьший
            text += print_text(about_2[2].split('\n'), LINE_LEN)
            q = min_n_num()

        case 3:
            # Сумма Наибольший
            text += print_text(about_2[3].split('\n'), LINE_LEN)
            q = sum_n_list()

        case 4:
            # СЧЁТЕСЛИ
            text += print_text(about_2[4].split('\n'), LINE_LEN)
            q = count_if(100)

        case 5:
            # СУММЕСЛИ
            text += print_text(about_2[4].split('\n'), LINE_LEN)
            q = sum_if(100)

        case 6:
            # СРЗНАЧЕСЛИ
            text += print_text(about_2[4].split('\n'), LINE_LEN)
            q = mean_if(100)

        case 7:
            text += about_2[5].split('\n')
            q = ''

    return text, q
