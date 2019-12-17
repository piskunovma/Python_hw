# class MyError(Exception):
#
#     def __init__(self, message: str = ''):
#         self.message = message
#         Exception.__init__(self)
#
#     def __str__(self):
#         return self.message
#
# try:
#     a = 1 + 1
#     raise MyError('Тут что-то не так')
# except MyError:
#     print(1)

class FuncTools:

    @staticmethod
    def func1():
        return  'func1'

    @staticmethod
    def func2():
        return 'func2'

FuncTools.func1()

string = "Hello world!"

print(string[:-2])