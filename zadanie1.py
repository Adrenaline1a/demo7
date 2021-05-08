#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    U = tuple(map(float, input("Введите значения U: ").split()))
    D = tuple(map(float, input("Введите значения D: ").split()))
    B = tuple(map(float, input("Введите значения B: ").split()))
    S = ()
    if len(U) != 7 or len(D) != 7 or len(B) != 7:
        print("Введите значение на каждый день недели, то есть 7 значений для каждой величины")
        exit(1)
    for i in range(7):
        (k, ) = ((U[i]+D[i]+B[i])/3, )
        S = S + (k, )
        (k, ) = (0, )
    print("Среднее значение температуры по дням недели: ", S)
