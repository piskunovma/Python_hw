"""
5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

my_f = open("text5.txt", "w")
numbers = input('Введите строку чисел, разделенных пробелом: \n')
try:
    my_f.write(numbers)
    my_f.close()

    my_f = open("text5.txt", "r")
    data_file = my_f.read()
    result = sum(map(int, data_file.split()))
    print(result)
    my_f.close()
except ValueError:
    print("Введите числа, а не символы!")

my_f.close()
