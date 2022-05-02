"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
класса (метод __init__()), который должен принимать данные
(список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода
матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для сложения двух
объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
"""

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str,self.matrix[l]))
                          for l in range(len(self.matrix))])

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or\
                len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError(f'Матрицы разных размеров')

        res = [map(sum, zip(*i)) for i in zip(self.matrix,other.matrix)]
        return Matrix(res)


if __name__ == '__main__':
    m_1 = Matrix([[3,0,32.6],[-1,64,-8]])
    print('Matrix 1')
    print(m_1)
    print()

    m_2 = Matrix([[3,5,8],[25,-64,28]])
    print('Matrix 2')
    print(m_2)
    print()

    print('New Matrix')
    print(m_1 + m_2)

# Matrix 1
# 3	0	32.6
# -1	64	-8
#
# Matrix 2
# 3	5	8
# 25	-64	28
#
# New Matrix
# 6	5	40.6
# 24	0	20
