# Импорт библиотек для выхода из консоли
import msvcrt
import sys
# Ввод количества сотрудников и проверка на целочисленность
try:
    employeesN = int(input("Введите количество сотрудников, выражаемое целым числом от 1 до 1000: "))
except Exception:
    print("Количество сотрудников не является целым числом, перезапустите программу")
    msvcrt.getch()
    sys.exit()
# Проверка на вхождение employeesN в диапазон
if not ((employeesN>=1) and (employeesN<=1000)):
    print("Количество сотрудников выходит за рамки диапазона")
    msvcrt.getch()
    sys.exit()
# Ввод расстояний до домов сотрудников и проверка на целочисленность
try:
    employeesKM = list(map(int, input("Введите расстояния, проходимые сотрудниками, в формате строки, содержащей целые числа от 1 до 999: ").split()))
except Exception:
    print("Одно или несколько расстояний не являются целыми числами, перезапустите программу")
    msvcrt.getch()
    sys.exit()
# Проверка на вхождение каждого элемента employeesKM в диапазон
for i in employeesKM:
    if (i < 1) and (i > 1000):
        print("Одно или несколько расстояний выходят за рамки диапазона")
        msvcrt.getch()
        sys.exit()
# Ввод тарифов такси и проверка на целочисленность
try:
    taxiCost = list(map(int, input("Введите тарифы таксистов в формате строки, содержащей целые числа от 1 до 9999: ").split()))
except Exception:
    print("Один или несколько тарифов не являются целыми числами, перезапустите программу")
    msvcrt.getch()
# Проверка на вхождение каждого элемента taxiCost в диапазон
for i in taxiCost:
    if (i < 1) and (i > 10000):
        print("Один или несколько тарифов выходят за рамки диапазона")
        msvcrt.getch()
        sys.exit()
# Основная часть работы программы
taxis = {}
workers = {}
for i in range(employeesN):
    taxis[taxiCost[i]] = i+1
    workers[employeesKM[i]] = i+1
employees_sorted = sorted(workers.values())
taxis_sorted = sorted(taxis.values(),reverse=True)
# Вывод данных
print("Выходные данные:")
print("Номера сотрудников:", end=" ")
for key in sorted(workers.keys()):
    print(workers[key], end=" ")
print()
print("Соответствующие номера такси:", end=" ")
for key in sorted(taxis.keys(), reverse=True):
    print(taxis[key], end=" ")
msvcrt.getch()
sys.exit()
