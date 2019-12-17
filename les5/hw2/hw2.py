"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_f = len(open('text2.txt', "r").readlines())
print(f'Количество строк - {my_f}.')

my_f = open("text2.txt", "r")
i = 1
for line in my_f:
    pos = 0
    word = 0
    for words in line:
        if words != ' ' and pos == 0:
            word += 1
            pos = 1
        elif words == ' ':
            pos = 0
    print(f'В строке {i} - {word} слов.')
    i += 1

my_f.close()
