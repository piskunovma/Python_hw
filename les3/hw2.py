"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""
# Вариант с помощью функции с циклом
def user_data(name, surname, year, sity, email, number):
    user_data_dict = {name: f'Введите {name}', surname: f'Введите {surname}', year: f'Введите {year}', sity: f'Введите {sity}', email: f'Введите {email}', number: f'Введите {number}'}
    result_dict = {}
    for key, itm in user_data_dict.items():
        enter_dict = input(f'{itm}: \n')
        result_dict[key] = enter_dict
    return result_dict

print(user_data(name = "имя", surname = "фамилия", year = "год рождения", sity = "город проживания", email = "email", number = "номер телефона"))


# # Вариант с поэтапным вводом данных
# def user_data(name, surname, year, sity, email, number):
#     return f"Имя - {name}, Фамилия - {surname}, Год рождения - {year}, Город проживания - {sity}, Электронная почта - {email}, Номер телефона - {number}"
#
# name = input("Введите имя: \n")
# surname = input("Введите фамилию: \n")
# year = input("Введите год рождения: \n")
# sity = input("Введите город проживания: \n")
# email = input("Введите email: \n")
# number = input("Введите номер телефона: \n")
#
# print(user_data(name = name, surname = surname, year = year, sity = sity, email = email, number = number))

# Вариант с циклом снаружи функции
# def user_data(name, surname, year, sity, email, number):
#     return f"Имя - {name}, Фамилия - {surname}, Год рождения - {year}, Город проживания - {sity}, Электронная почта - {email}, Номер телефона - {number}"
#
# name, surname, year, sity, email, number = 'имя', "фамилия", "год рождения", "город проживания", "email", "номер телефона"
# user_data_dict = {name: f'Введите {name}', surname: f'Введите {surname}', year: f'Введите {year}', sity: f'Введите {sity}', email: f'Введите {email}', number: f'Введите {number}'}
# result_dict = {}
# for key, itm in user_data_dict.items():
#     enter_dict = input(f'{itm}: \n')
#     result_dict[key] = enter_dict
#
# print(user_data(name = result_dict[name], surname = result_dict[surname], year = result_dict[year], sity = result_dict[sity], email = result_dict[email], number = result_dict[number]))