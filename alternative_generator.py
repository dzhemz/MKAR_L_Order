import random
disciplines = ["СПО",
               "ОС",
               "Управление_данными",
               "Корпоративные_информационные_системы",
               "Теория_вероятности_и_математическая_статистика",
               "Дифференциальные_уравнения",
               "Математический_анализ",
               "Физическая_культура",
               "Элективный_курс_по_физической_культуре"]


print("\n".join(
    list(map(lambda discipline: f'alternative {discipline} ' + ' '.join([str(random.randint(4, 10)) for i in range(14)]),
             disciplines))))
