import random


def get_random_list(lenght):
    list = []

    while len(list) < lenght:
        item = random.randint(0, 100)

        if item not in list: # добавление только уникальных чисел
            list.append(item)

    return list


def get_smallest_index(list):
    smallest = list[0]
    smallest_index = 0

    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i

    return smallest_index


def get_largest_index(list):
    largest = list[0]
    largest_index = 0

    for i in range(1, len(list)):
        if list[i] > largest:
            largest = list[i]
            largest_index = i

    return largest_index
