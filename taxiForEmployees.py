import msvcrt
import sys
try:
    employeesN = int(input("Введите количество сотрудников, выражаемое целым числом: "))
except Exception:
    print("Количество сотрудников не является целым числом, перезапустите программу")
    msvcrt.getch()
    sys.exit()
if not ((employeesN>=1) and (employeesN<=1000)):
    print("Количество сотрудников выходит за рамки диапазона")
    msvcrt.getch()
    sys.exit()
try:
    employeesKM = list(map(int, input("Введите расстояния, проходимые сотрудниками, в формате строки, содержащие целые числа: ").split()))
except Exception:
    print("Одно или несколько расстояний не являются целыми числами, перезапустите программу")
    msvcrt.getch()
    sys.exit()
for i in employeesKM:
    if (i < 1) and (i > 1000):
        print("Одно или несколько расстояний выходят за рамки диапазона")
        msvcrt.getch()
        sys.exit()
try:
    taxiCost = list(map(int, input("Введите тарифы таксистов в формате строки, содержащие целые числа: ").split()))
except Exception:
    print("Один или несколько тарифов не являются целыми числами, перезапустите программу")
    msvcrt.getch()
for i in employeesKM:
    if (i < 1) and (i > 1000):
        print("Один или несколько тарифов выходят за рамки диапазона")
        msvcrt.getch()
        sys.exit()
taxis = {}
workers = {}
for i in range(employeesN):
    taxis[taxiCost[i]] = i+1
    workers[employeesKM[i]] = i+1
employees_sorted = sorted(workers.values())
taxis_sorted = sorted(taxis.values(),reverse=True)
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
