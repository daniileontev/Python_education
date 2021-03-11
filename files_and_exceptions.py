print('Файлы и исключения, чтение из файла:\n')

# На примере числа Пи, разберем открытие и чтение из файла (полный код для чтения файлов в file_reader.py)

# Конструкция с ключевым словом with закрывает файл после того, как надобность в нем отпадет.
with open ('pi_digit.txt') as file_object:
# Функция open() возвращает объект, представляющий файл.
# В данном случае open('pi_digits.txt') возвращает объект, представляющий файл pi_digits txt.
    contents = file_object.read()
# во второй строке программы используется метод read(), который читает все содержимое файла,
# сохраняет его содержимое в одной длинной строке в переменной contents. 
    #print(contents)
# При выводе значения contents на экране появляется все содержимое файла

# Чтобы выполнить любые операции с файлом — даже просто
# вывести его содержимое, сначала необходимо открыть файл.
# Функция open() получает один аргумент: имя открываемого файла:
# Python ищет файл с указанным именем в каталоге, в котором находится файл текущей программы.
# Конструкция с ключевым словом with закрывает файл после того, как надобность в нем отпадет.

print('\nПути к файлам:\n')

# Чтобы открыть файлы из каталога, отличного от того, в котором хранится файл программы,
# необходимо указать путь — то есть приказать Python искать файлы в конкретном месте файловой системы

print('Так выглядит относительный путь к файлу:\n')

# Конструкция с ключевым словом with закрывает файл после того, как надобность в нем отпадет.
with open ('text_files/pi_digit.txt') as file_object:
# Эта строка означает, что файл txt следует искать в каталоге text_files; она предполагает,
# что каталог text_files находится в python_education.
# В данном случае open('pi_digits.txt') возвращает объект, представляющий файл pi_digits txt.
    contents = file_object.read()
# во второй строке программы используется метод read(), который читает все содержимое файла,
# сохраняет его содержимое в одной длинной строке в переменной contents. 
    #print(contents)
# При выводе значения contents на экране появляется все содержимое файла

print('Полный путь:')

# Также можно точно определить местонахождение файла в вашей системе неза-
# висимо от того, где хранится выполняемая программа. 
# Такие пути называются абсолютными и используются в том случае, если относительный путь не работает:

# for Linux OS:

# file_path = '/home/ehmatthes/other_files/text_files/имя_файла.txt'
# with open(file_path) as file_object:

# for Windows OS:

# file_path = 'C:\Users\ehmatthes\other_files\text_files\имя_файла.txt'
# with open(file_path) as file_object:

# все примеры работы программы в файле file_reader.py

print('\nЗапись в пустой файл\n')

# Чтобы записать текст в файл, необходимо вызвать open() со вторым аргументом,
# который сообщает Python, что вы собираетесь записывать данные в файл

# filename = 'programming.txt'
# Первый аргумент, как и прежде, содержит имя открываемого файла. Второй аргумент 'w' сообщает
# Python, что файл должен быть открыт в режиме записи.
# with open (filename, 'w') as file_object:
    #file_object.write('I love programming')

# Файлы можно открывать в режиме чтения ('r'), записи ('w'), присоединения ('a') или в режиме,
# допускающем как чтение, так и запись в файл ('r+')

# пример работы программы указан в write_message.py

print('\nИсключения\n')

# Если при возникновении ошибки Python не знает, что делать дальше, создается объект
# исключения. Если в программу включен код обработки исключения, то выполне-
# ние программы продолжится, а если нет — программа останавливается и выводит
# трассировку с отчетом об исключении.

# Исключения обрабатываются в блоках try-except

print('\nОбработка исключения ZeroDivisionError\n')

# пример работы в division.py

# Если вы предполагаете, что в программе может произойти ошибка, 
# напишите блок try-except для обработки возникающего исключения

print('\nОбработка исключения FileNotFoundError\n')

# пример работы в alice.py

print('\nРабота с несколькими файлами\n')

# работая с несколькими файлами, проще всего определить функции,
# которые будут отвечать за чтение разных файлов в одной программе

# пример работы в count_words.py

print('\nСохранение данных\n')

# Многие ваши программы будут запрашивать у пользователя информацию.
# Например, пользователь может вводить настройки для компьютерной игры или данные
# для визуального представления.
# Чем бы ни занималась ваша программа, информация, введенная пользователем,
# будет сохраняться в структурах данных (таких,как списки или словари).

# Простейший способ сохранения данных основан на использовании модуля json

# Модуль json также может использоваться для обмена данными между программами Python.
# Более того, формат данных JSON не привязан к Python, поэтому данные в этом формате
# можно передавать программам, написанным на многих других языках программирования.

print('\nФункции json dump() и json load()\n')

# Напишем короткую программу для сохранения набора чисел и другую программу,
# которая будет читать эти числа обратно в память.
# Первая программа использует функцию json.dump(), а вторая — функцию json.load().

# пример работы в number_writer.py и number_reader.py

print('\nСохранение и чтение данных, сгенерированных пользователем\n')

# Сохранение с использованием модуля json особенно полезно при работе с данными,
# сгенерированными пользователем, потому что без сохранения эта информация будет потеряна при остановке программы

# пример работы в remember_me.py и greet_user.py
# в следствии мы  объединяем эти программы в один файл (remember_me_3.py).
# Когда пользователь запускает remember_me.py, программа должна взять имя пользователя из памяти,
# если это возможно; соответственно, программа начинается с блока try, который пытается прочитать имя пользователя. 
# Если файл username json не существует, 
# блок except запросит имя пользователя и сохранит его в username json на будущее

print('\Рефакторинг\n')

# Часто возникает ситуация: код работает, но вы понимаете, что его структуру можно усовершенствовать,
# разбив его на функции, каждая из которых решает свою конкретную задачу.
# Этот процесс называется рефакторингом (или переработкой).
# Рефакторинг делает ваш код более чистым, понятным и простым в расширении.

# Основной задачей remember_me_2.py является вывод приветствия для пользователя,
# поэтому весь существующий код будет перемещен в функцию greet_user()

# пример рефакторинга в remember_me_2.py

# Глава закончена, вся основная информаиция по работе кода и тд, в files_and_exceptions_tasks.py



