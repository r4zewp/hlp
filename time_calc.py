from datetime import datetime
import time
import function
import matplotlib.pyplot as plt
import time

###### функции, тестирующие время работы для каждого файла

file_one = "inputs/input_1.txt"
file_two = "inputs/input_2.txt"
file_three = "inputs/input_3.txt"

def test_one():
    t1 = time.time()
    ## выполняем функцию 5 раз для того, чтобы получить усредненный результат
    for i in range(100):
        function.fileReading(file_one)
    t2 = time.time()
    result_one = (t2 - t1)/100
    return result_one

def test_two():
    t1 = time.time()
    for i in range(100):
        function.fileReading(file_two)
    t2 = time.time()
    result_two = (t2 - t1)/100
    return result_two

def test_three():
    t1 = time.time()
    for i in range(100):
        function.fileReading(file_three)
    t2 = time.time()
    result_three = (t2 - t1)/100
    return result_three

###### сохраняем время работы по 3 разным файлам
time_one = test_one()
time_two = test_two()
time_three = test_three()

###### строим график по времени, чтобы увидеть
###### зависимость
data = {'4000 symbols': time_one, '8000 symbols': time_two, '12000 symbols': time_three}
names = list(data.keys())
values = list(data.values())
fig, axs = plt.subplots()
axs.plot(names, values)
plt.savefig(f'outputs/graphic_{datetime.now():%Y-%m-%d-%H-%M-%S}.png')
