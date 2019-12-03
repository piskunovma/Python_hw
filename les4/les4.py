# import time as my_time
# from time import time as my_time1
#
# start = my_time.time()
#
# for _ in range(10):
#     a = 10 ** 10
#
# end = my_time.time()
#
# print(end - start)

# from datetime import datetime, timedelta
# from random import randint
#
#
# print((randint(0, 10)))
# delta = timedelta(days=randint(0, 10), hours=randint(1, 12))
#
# now_date = datetime.now()
#
# print("now", now_date)
#
# print(now_date - delta)


# import  json
#
# import requests
#
# url = 'https://api.github.com/users/gefmar'
#
# respones = requests.get(url)
#
# result = json.loads((respones.text))
# print(type(json.loads(respones.text)))
# print(result)

# import  sys
# import  json
# import os
#
# import requests

# print(sys.platform)
# print(sys.argv)


# base_url = 'https://api.github.com/users/'
# username = sys.argv[1]
#
# url = f'{base_url}{username}'
# response = requests.get(url)
#
# # print(response.json)
#
# file = open('some_file.txt', 'w')
# file.write(response.text)
# file.close()

# import  sys
# import  json
# import os
#
# import requests
#
# base_url = 'https://api.github.com/users/'
# username = sys.argv[1]
#
# url = f'{base_url}{username}'
# response = requests.get(url)
#
# file_folder = os.getcwd()
# file_path = os.path.join(file_folder, 'some_file.txt')
# print(file_path)
#
# with open(file_path, 'w') as file:
#     file.write(response.text)
#
# print(os.getcwd())

# import  sys
# import  json
# import os
#
# import requests
#
# base_url = 'https://api.github.com/users/'
# username = sys.argv[1]
#
# url = f'{base_url}{username}'
# response = requests.get(url)
#
# file_folder = os.getcwd()
# file_path = os.path.join(file_folder, 'some_file.txt')
# print(file_path)
#
# with open(file_path, 'r') as file:
#     data = file.read()
#     print(data)
#     print('*'*15)
#     j_data = json.loads(data)
#     print((j_data))
#
# print(os.getcwd())

# import  json
# import os
#
#
# file_folder = os.getcwd()
# file_path = os.path.join(file_folder, 'some_file.txt')
# print(file_path)
#
# # with open(file_path, 'r') as file:
# #     data = [itm]
#
# list_comp = [itm for itm in range(10)]
# dict_comp = {idx:itm for idx, itm in enumerate(range(10), start=5)}
#
# with open(file_path, 'r') as file:
#     for line in file:
#         print(line)

# from my_package.my_pack import my_func
#
# for itm in my_func(5):
#     print(itm)
#
# if __name__ == '__main__':
#     print('main')


# C помощью лямбды
# def fibo_gen():
#     yield (reduce(lambda x, y: x*y, [i for i in range(1, fact_number + 1)]))

# while True:
#     fact_number = input("Введите число, для расчета факториала числа: \n")
#     try:
#         fact_number = int(fact_number)
#         break
#     except ValueError:
#         print("Введите число!")
