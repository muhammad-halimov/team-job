import numpy as np

# Пример двумерных массивов
array1 = np.array([[5, 14, 21],
                   [10, 35, 49],
                   [15, 28, 42]])

array2 = np.array([[3, 10, 21],
                   [6, 14, 35],
                   [9, 20, 49]])

# Поиск и вывод результатов для первого массива
valid_columns1 = []
for col in range(array1.shape[1]):
    column_data = array1[:, col]
    if all(value % 5 == 0 or value % 7 == 0 for value in column_data):
        valid_columns1.append(col)

if valid_columns1:
    print("В первом массиве номера столбцов с элементами, кратными 5 и 7:", valid_columns1)
else:
    print("В первом массиве нет столбцов с элементами, кратными 5 и 7.")

# Поиск и вывод результатов для второго массива
valid_columns2 = []
for col in range(array2.shape[1]):
    column_data = array2[:, col]
    if all(value % 5 == 0 or value % 7 == 0 for value in column_data):
        valid_columns2.append(col)

if valid_columns2:
    print("Во втором массиве номера столбцов с элементами, кратными 5 и 7:", valid_columns2)
else:
    print("Во втором массиве нет столбцов с элементами, кратными 5 и 7.")