import random


def get_random_list(lenght):
    list = []

    while len(list) < lenght:
        item = random.randint(0, 100)

        if item not in list: # добавление только уникальных чисел
            list.append(item)

    return list


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


def main():
    while True:
        lenght = random.randint(1, 10)

        list = get_random_list(lenght)
        list.sort()

        print(f"list: {list}")

        item = int(input("item: "))

        print(f"result: {binary_search(list, item)}\n")


if __name__ == "__main__":
    main()
