"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

my_f = open("text4.txt", "r")

i = 1
for line in my_f:
    word = line.split()[0]
    if line.split()[0] == "One":
        word = "Один"
    elif word == "Two":
        word = "Два"
    elif word == "Three":
        word = "Три"
    elif word == "Four":
        word = "Четыре"
    new_f = open("result.txt", "a")
    new_f.write(f"{word} — {i} \n")
    new_f.close()
    i += 1

my_f.close()