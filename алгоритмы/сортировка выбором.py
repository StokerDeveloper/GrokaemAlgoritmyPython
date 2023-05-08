import random
from utils import get_random_list, get_smallest_index, get_largest_index, timer


@timer
def selection_sort(list, type):
    new_list = []

    for i in range(len(list)):
        if type == "1":
            current_index = get_smallest_index(list)
        elif type == "2":
            current_index = get_largest_index(list)
        else:
            return []

        new_list.append(list.pop(current_index))

    return new_list


def main():
    while True:
        lenght = random.randint(1, 10)

        list = get_random_list(lenght)
        print(f"list: {list}")

        type = input("Сортировать - 1)по возрастанию 2)по убыванию: ")

        list = selection_sort(list, type)
        print(f"list: {list}")

        print()


if __name__ == "__main__":
    main()