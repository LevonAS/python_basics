"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса
(комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""
# Суммой двух комплексных чисел z1=a+bi и z2=c+di
#   является комплексное число z1+z2 = (a+c)+(b+d)i
# Умноженем двух комплексных чисел z1=a+bi и z2=c+di
#   является комплексное число z1+z2 = (ac-bd)+(bc+ad)i
# Комплексное число всегда имеет мнимую часть, а реальная не обязательна.
# Если нет реальной части, то она подразумевается равной 0,
# если нет мнимой части, то подразумевается, что она равна 0j


class ComplexNum:
    def __init__(self, real, imag=0):
        self.z = complex(real, imag)

    def __add__(self, other):
        return ComplexNum(round(self.z.real + other.z.real,2),
                          round(self.z.imag + other.z.imag,2))

    def __mul__(self, other):
        r = round(self.z.real * other.z.real - self.z.imag * other.z.imag,2)
        im = round(self.z.imag * other.z.real + self.z.real * other.z.imag,2)
        return ComplexNum(r,im)

    def __str__(self):
        return str(f'{self.z.real} + {self.z.imag}i')


if __name__ == '__main__':
    z1 = ComplexNum(4.3, -3)
    z2 = ComplexNum(-8, 5)
    print('z1 + z2 =',z1 + z2)
    print('z1 + z2 =',z1 * z1)

    print()
    z3 = ComplexNum(4)
    z4 = ComplexNum(0, 5.11)
    print('z3 + z4 =',z3 + z4)
    print('z3 * z4 =',z3 * z4)

# z1 + z2 = -3.7 + 2.0i
# z1 + z2 = 9.49 + -25.8i
#
# z3 + z4 = 4.0 + 5.11i
# z3 * z4 = 0.0 + 20.44i
