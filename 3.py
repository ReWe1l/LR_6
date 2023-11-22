import random

def find_max_element(data):
    n = 0
    max_element = data[0]
    for i in range(len(data)):
        if data[i] > max_element:
            max_element = data[i]
            n = i
    return n

def sum_negative_elements(data):
    total = 0
    for i in range(len(data)):
        if data[i] < 0:
            total += data[i]
    return total

size = int(input("Введите размер списка: "))
my_list = [random.randint(-100, 100) for _ in range(size)]

print("Исходный список:", my_list)

max_index = find_max_element(my_list)
my_list[0], my_list[max_index] = my_list[max_index], my_list[0]

print("Список после перестановки наибольшего элемента с первым:", my_list)

negative_sum = sum_negative_elements(my_list)
print("Сумма отрицательных элементов:", negative_sum)
