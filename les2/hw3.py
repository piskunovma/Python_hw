"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

# Решение через list

# month = input("Введите номер месяца : ")
# result_list = ["Зима", "Весна", "Лето", "Осень"]
#
# if month.isdigit():
#     month = int(month)
#     if month == 12 or month == 1 or month == 2:
#         result = result_list[0]
#     elif month > 2 and month < 6:
#         result = result_list[1]
#     elif month > 5 and month < 9:
#         result = result_list[2]
#     elif month > 8 and month < 12:
#         result = result_list[3]
#     else:
#         result = f"Вы ввели {month}, введите число от 1 до 12"
# else:
#     result = "Вы ввели не число, введите число от 1 до 12"
# print(result)

# Решение через dict

month = input("Введите номер месяца : ")
result_dict = {
    'time_year1':'Зима',
    'time_year2': 'Весна',
    'time_year3': 'Лето',
    'time_year4': 'Осень'
}

if month.isdigit():
    month = int(month)
    if month == 12 or month == 1 or month == 2:
        result = result_dict['time_year1']
    elif month > 2 and month < 6:
        result = result_dict['time_year2']
    elif month > 5 and month < 9:
        result = result_dict['time_year3']
    elif month > 8 and month < 12:
        result = result_dict['time_year4']
    else:
        result = f"Вы ввели {month}, введите число от 1 до 12"
else:
    result = "Вы ввели не число, введите число от 1 до 12"
print(result)
