print('Тестирование\n')

print('\nТестирование функции\n')

# пример простого тестирования разобран в name_function.py + names.py

print('\nПрохождение теста\n')

# Чтобы написать тестовый сценарий для функции, импортируйте модуль unittest и функцию,
# которую необходимо протестировать.
# Затем создайте класс, наследующий от unittest.TestCase, и напишите серию методов для
# тестирования различных аспектов поведения своей функции.

# пример сценария в test_name_function.py(где тестируется код выше написанных функций)

print('\nСбой теста\n')

# пример работы в name_function.py в закоменченом виде

print('\nДобавление новых тестов\n')

# пример добавления сценария в test_name_function.py

print('\nТестирование класса\n')

# Классы будут использоваться во многих ваших программах,
# поэтому возможность доказать, что ваши классы работают правильно, будет безусловно полезной.

print('\nРазные методы assert\n')

# Класс unittest.TestCase содержит целое семейство проверочных методов assert.
# Эти методы проверяют, выполняется ли условие, которое
# должно выполняться в определенной точке вашего кода.

# С их помощью можно проверить, что возвращаемые значения равны или не равны ожидаемым,
# что значения равны True или False или что значения входят или не входят в заданный список. 
# Эти методы могут использоваться только в классах, наследующих от unittest

# Методы assert, предоставляемые модулем unittest
# Метод                       Использование
# assertEqual(a, b)            Проверяет, что a == b
# assertNotEqual(a, b)         Проверяет, что a != b
# assertTrue(x)                Проверяет, что значение x истинно
# assertFalse(x)               Проверяет, что значение x ложно
# assertIn(элемент, список)    Проверяет, что элемент входит в список
# assertNotIn(элемент, список) Проверяет, что элемент не входит в список

print('\nКласс для тестирования\n')

# Тестирование класса имеет много общего с тестированием функции
# — значительная часть работы направлена на тестирование поведения методов класса
# пример работы программы в survey.py + language_survey.py

print('\nТестирование класса survey.py\n')

# сценарий тестирования в test_survey.py

print('\nМетод setUp()\n')

#Класс unittest.TestCase содержит метод setUp(),
# который позволяет создать эти объекты один раз,
# а затем использовать их в каждом из тестовых методов.

# Если в класс TestCase включается метод setUp(),
# Python выполняет метод setUp() перед запуском каждого метода,
# имя которого начинается с test_.

# пример использования метода setUp() в test_survey_2.py
