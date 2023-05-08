import random
from utils import get_random_list


def fast_sort(list, type):
    if len(list) < 2:
        return list

    smallests = []
    dublicateds = [ list[0] ]
    largests = []

    for i in range(len(list)):
        if i == 0:
            continue
        if list[i] > dublicateds[0]:
            largests.append(list[i])
        elif list[i] < dublicateds[0]:
            smallests.append(list[i])
        else:
            dublicateds.append(list[i])

    if type == "1":
        return fast_sort(smallests, type) + dublicateds + fast_sort(largests, type)
    elif type == "2":
        return fast_sort(largests, type) + dublicateds + fast_sort(smallests, type)
    else:
        return []


def main():
    while True:
        lenght = random.randint(1, 10)

        list = get_random_list(lenght)
        print(f"list: {list}")

        type = input("Сортировать - 1)по возрастанию 2)по убыванию: ")

        list = fast_sort(list, type)
        print(f"list: {list}")

        print()


if __name__ == "__main__":
    main()