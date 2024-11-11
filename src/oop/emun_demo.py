#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "jerry chan"
__doc__ = """ """
__date__ = "2024/10/4 11:44"

from enum import Enum, unique

@unique
class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

if __name__ == "__main__":
    print(Month.JANUARY)
    print(Month.JANUARY.value)
    print(Month.JANUARY.name)
    print(Month(1))
    print(Month(1).value)
    print(Month(1).name)
    print(Month(12))
    print(Month(12).value)

    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)