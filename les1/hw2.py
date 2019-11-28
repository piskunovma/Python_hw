"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""


time = int(input('Введите время в секундах\n'))

time_hours = time // 3600
time_minutes = time / 60 % 60
time_minutes = int(time_minutes)
time_sec = time % 60

full_data = f'Получается следующее время: {time_hours}:{time_minutes}:{time_sec}'
print(full_data)