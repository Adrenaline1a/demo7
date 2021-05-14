#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import math

if __name__ == '__main__':
    a = tuple(map(float, input("Введите элементы списка: ").split()))
    A = int(input("Введите минимальное значение диапазона (A): "))
    B = int(input("Введите максимальное значение диапазона (B): "))
    m = 0
    n = 0
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    b = a[A:B]
    b = len(b)
    print("Количество чисел в диапазоне от А до В = ", b)
    for i in enumerate(a, 0):
        if m < i[1]:
            m = i[1]
            n = i[0]
    c = a[n:]
    g = a[n + 1:]
    s = sum(g)
    j = tuple(sorted(c, key=lambda x: math.fabs(x), reverse=True))
    print("Сумма чисел после максимального элемента, введёного списка", s)
    print(j)
