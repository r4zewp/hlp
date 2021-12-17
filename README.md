# ТЕХНИЧЕСКОЕ ЗАДАНИЕ №3
**Арустамов Тигран Ваграмович**

**ББИ2005**

[![TZ3](https://github.com/r4zewp/hlp/actions/workflows/main2.yml/badge.svg)](https://github.com/r4zewp/hlp/actions/workflows/main2.yml)
----------------------------

**main.py** - в коде файла содержится исключительно запуск функции, отвечающей за считывание чисел из файла и проведение всех нужных вычислений.

**function.py** - в коде файла содержатся функции, отвечающие за вычисление минимального, максимального числа, за вычисление суммы и произведения всех чисел.

**time_calc.py** - файл содержит код, отвечающий за вычисление скорости выполнения основной функции программы с набором из 3 файлов из 4000, 8000 и 12000 символов. (соответственно,
каждый из них имеет разный размер и скорость выполнения различается)

**tests/** - этот каталог содержит набор тестов для всех функций. Датасет для них находится в файле inputs/datasets.py

**inputs/** - каталог с файлами и датасетом, которые используются в процессе работы программы.

**outputs/** - каталог для сохранения изображений графиков, строящихся как показатель зависимости времени работы от размера файлов (задание с проверкой на скорость выполнения)
