# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def sum_cloth(self):
        pass


class Coat(Cloth):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            self.__size = 40
        elif size > 60:
            self.__size = 60
        else:
            self.__size = size

    def sum_cloth(self):
        return f'На пошив пальто потребуется {round((self.size / 6.5 + 0.5),2)} метра ткани'


class Suit(Cloth):
    def __init__(self, height):
        self.height = height

    def sum_cloth(self):
        return f'На пошив пальто потребуется {round((2 * self.height + 0.3),2)} метра ткани'


red_coat = Coat(38)
print(red_coat.sum_cloth())

blue_suit = Suit(195)
print(blue_suit.sum_cloth())

