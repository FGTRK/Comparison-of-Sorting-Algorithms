from random import randint
from time import time


def bubbleSort(mas):
    for i in range(len(mas) - 1):
        for j in range(len(mas) - 1 - i):
            if mas[j] > mas[j + 1]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]


def selectSort(mas):
    for i in range(len(mas)):
        min_ind = i
        for j in range(i, len(mas)):
            if mas[j] < mas[min_ind]:
                min_ind = j
        mas[i], mas[min_ind] = mas[min_ind], mas[i]


def insertionSort(mas):
    for i in range(1, len(mas)):
        j = i
        while j > 0 and mas[j] < mas[j - 1]:
            mas[j], mas[j - 1] = mas[j - 1], mas[j]
            j -= 1


def quickSort(mas, left, right):
    i, j = left, right
    pivot = mas[(i + j) // 2]
    while i <= j:
        while mas[i] < pivot:
            i += 1
        while mas[j] > pivot:
            j -= 1
        if i <= j:
            mas[i], mas[j] = mas[j], mas[i]
            i += 1
            j -= 1

    if j > left:
        quickSort(mas, left, j)
    if i < right:
        quickSort(mas, i, right)


def calcTime(func, mas, rec=False):
   # new_mas = mas[:]
    start = time()
    if rec:
        func(mas, 0, len(mas) - 1)
    else:
        func(mas)
    print("Прошло времени: ", time() - start)


a = [randint(1, 500) for i in range(8)]
b, c, d = a[:], a[:], a[:]

"""
calcTime(bubbleSort, b)
calcTime(selectSort, c)
calcTime(insertionSort, d)
"""

calcTime(quickSort, a, True)
print(a)
