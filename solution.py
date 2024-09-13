import numpy as np

def check_column(column):
    """Проверяет, содержит ли столбец только кратные 5 и 7."""
    for value in column:
        if value % 5 != 0 and value % 7 != 0:
            return False
    return True

def find_valid_columns(array):
    """Находит и возвращает номера столбцов, содержащих только кратные 5 и 7."""
    valid_columns = []
    for col in range(array.shape[1]):
        column_data = array[:, col]
        if check_column(column_data):
            valid_columns.append(col)
    return valid_columns

# Пример двумерных массивов
array1 = np.array([[5, 14, 21],
                   [10, 35, 49],
                   [15, 28, 42]])

array2 = np.array([[3, 10, 21],
                   [6, 14, 35],
                   [9, 20, 49]])

# Поиск и вывод результатов для первого массива
valid_columns1 = find_valid_columns(array1)
if valid_columns1:
    print("В первом массиве номера столбцов с элементами, кратными 5 и 7:", valid_columns1)
else:
    print("В первом массиве нет столбцов с элементами, кратными 5 и 7.")

# Поиск и вывод результатов для второго массива
valid_columns2 = find_valid_columns(array2)
if valid_columns2:
    print("Во втором массиве номера столбцов с элементами, кратными 5 и 7:", valid_columns2)
else:
    print("Во втором массиве нет столбцов с элементами, кратными 5 и 7.")
