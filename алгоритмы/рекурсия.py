import random
from utils import get_random_list, timer

# В книге эти функции были реализованы более красиво, но я оставлю так как сделал сам
@timer
def sum(list):
    if len(list) == 0:
        return 0
    elif len(list) == 1:
        return list[0]

    item = list.pop(0)
    return item + sum(list)


@timer
def get_items_count(list):
    if list == []:
        return 0

    list.pop(0)
    return 1 + get_items_count(list)


@timer
def get_largest(list):
    if len(list) == 0:
        return None
    elif len(list) == 1:
        return list[0]

    if list[0] < list[1]:
        list.pop(0)
    else:
        list.pop(1)

    return get_largest(list)


def binary_search(list, item):
    return "В прошлом бинарном поиске результатом функции служил индекс искомого элемента. Думая как реализовать этот алгоритм с рекурсией я пришел к выводу, что нужно делить массив и передавать его часть в следующую итерацию. Но как тогда получить индекс искомого элемента? По итогу у нас останется массив с 1-2 элементами. И что, возвращать индекс 0 или 1? Мне в голову пришел только вариант с добавлением дополнительных аргументов в функцию. Но я считаю это костыльным путем, поэтому не буду реализовывать бинарный поиск таким способом, и вообще не буду его реализовывать. Погуглю еще варианты как можно сделать это, но, даже если найду, этот момент оставлю как есть"


def main():
    while True:
        lenght = random.randint(1, 10)

        list = get_random_list(lenght)
        print(f"list: {list}")

        type = input("Сортировать - 1)сумма 2)количество элементов 3)наибольшее число 4)бинарный поиск: ")

        value = 0
        
        if type == "1":
            value = sum(list)
        elif type == "2":
            value = get_items_count(list)
        elif type == "3":
            value = get_largest(list)
        elif type == "4":
            list.sort()
            value = binary_search(list, 0)

        print(f"result: {value}")

        print()


if __name__ == "__main__":
    main()