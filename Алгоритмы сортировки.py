#НОД через деление
##def nod_del ():
##  a = 35
##  b = 14
##  while a != 0 and b != 0:
##    if a > b:
##      a = a% b
##      print (a)
##    else:
##      b = b % a
##      print (b)
##  print (a + b)
##  
##nod_del ()


##НОД через вычитание
##def nod_minus ():
##  a = 50
##  b = 10
##  while a != b:
##    print('a,b', a, b)
##    if a > b:
##      a = a - b
##      print ('a', a)
##    else:
##      b = b - a
##      print ('b', b)
##  print (b)
##
##nod_minus ()



##Алгоритм сортировки выбором
##from random import randint
##n = 10 #длина списка
##arr = [] #список
##for i in range (n): #функция range() возвращает объект, создающий последовательность чисел
##  arr.append (randint (1, 100)) #генерация случайных int через randint
##print (arr)
##arr = sorted (arr) #сортировка через метод sorted
##print (arr)

#напишем функцию для сортировки:
##def vibor_sort (data):
##  lenght = len (data)
##  i = 0 #пойдем с 0-го элемента
##  while i < lenght - 1:
##    m = i #переменная, где мы запоминаем первичный индекс
##    j = i + 1 #переменная для перемещения данных
##    while j < lenght:
##      if data [j] < data [m]:
##        m = j
##      j += 1
##    data [i], data[m] = data[m], data[i]
##    i += 1
##  return data

##vibor_sort (arr)
##print (arr)



##Алгоритм сортировки пузырьком через цикл for
##from random import randint
##n = 10
##arr = []
##for i in range (n):
##  arr.append (randint (1, 100))
##print (arr)

##def bubble_for (data):
##  lenght = len (data)
##  for i in range (lenght - 1):
##    for j in range (lenght - 1 - i):
##      if data [j] > data [j + 1]:
##        data[j], data [j + 1] = data [j + 1], data[j]
##  return data
##
##bubble_for (arr)
##print (arr)


##Алгоритм сортировки пузырьком через цикл while
##def bubble_while (data):
##  lenght = len (data)
##  i = 0
##  while i < lenght - 1:
##    j = 0
##    while j < lenght - 1 - i:
##      if data [j] > data [j + 1]:
##        data [j], data [j + 1] = data[j + 1], data[j]
##      j += 1
##    i += 1
##  return data

##bubble_while (arr)
##print (arr)


##Алгоритм сортировки вставкой
##from random import randint
##n = 10
##arr = []
##for i in range (n):
##  arr.append (randint (1, 100))
##print (arr)

##def insertion (data):
##  for i in range (len (data)):
##    j = i - 1
##    key = data [i]
##    while data[j] > key and j >= 0:
##      data [j + 1] = data [j]
##      j -= 1
##    data [j + 1] = key
##  return data

##insertion (arr)
##print (arr)



from datetime import datetime

## Задача 2.1.

## Создайте две функции maximum и minimum,
## которые получают список целых чисел в качестве входных данных
## и возвращают наибольшее и наименьшее число в этом списке соответственно.
## Например,
### * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
### * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
### * [42, 54, 65, 87, 0]             -> min = 0, max = 87
### * [5]                             -> min = 5, max = 5
### функции sorted, max и min использовать нельзя!
arr = [[4,6,2,1,9,63,-134,566],[-52, 56, 30, 29, -54, 0, -110],[42, 54, 65, 87, 0],[5]]
##print (arr)

def vibor_sort (data):
  lenght = len (data)
  i = 0 #пойдем с 0-го элемента
  while i < lenght - 1:
    m = i #переменная, где мы запоминаем первичный индекс
    j = i + 1 #переменная для перемещения данных
    while j < lenght:
      if data [j] < data [m]:
        m = j
      j += 1
    data [i], data[m] = data[m], data[i]
    i += 1
  return data

def bubble_for (data):
  lenght = len (data)
  for i in range (lenght - 1):
    for j in range (lenght - 1 - i):
      if data [j] > data [j + 1]:
        data[j], data [j + 1] = data [j + 1], data[j]
  return data

def bubble_while (data):
  lenght = len (data)
  i = 0
  while i < lenght - 1:
    j = 0
    while j < lenght - 1 - i:
      if data [j] > data [j + 1]:
        data [j], data [j + 1] = data[j + 1], data[j]
      j += 1
    i += 1
  return data

def insertion (data):
  for i in range (len (data)):
    j = i - 1
    key = data [i]
    while data[j] > key and j >= 0:
      data [j + 1] = data [j]
      j -= 1
    data [j + 1] = key
  return data

def default (data):
  data = sorted (data)
  return data

def minimum (arr):
  print ('Минимальные значения:')
  print ('Алгоритм "vibor_sort":')
  start_time = datetime.now ()
  for data in arr:
    print ('Минимальное значение из списка:', data, vibor_sort (data)[0])
  end_time = datetime.now()
  print ('Продолжительность: {}'.format (end_time - start_time))
 
  print ('Алгоритм "bubble_for":')
  start_time = datetime.now ()
  for data in arr:
    print ('Минимальное значение из списка:', data, bubble_for (data)[0])
  end_time = datetime.now ()
  print ('Продолжительность: {}'.format (end_time - start_time))

  print ('Алгоритм "bubble_while":')
  start_time = datetime.now ()
  for data in arr:
    print ('Минимальное значение из списка:', data, bubble_while (data)[0])
  end_time = datetime.now ()
  print ('Продолжительность: {}'.format (end_time - start_time))

  print ('Алгоритм "insertion":')
  start_time = datetime.now ()
  for data in arr:
    print ('Минимальное значение из списка:', data, insertion (data)[0])
  end_time = datetime.now ()
  print ('Продолжительность: {}'.format (end_time - start_time))
  
  print ('Алгоритм "default":')
  start_time = datetime.now ()
  for data in arr:
    print ('Минимальное значение из списка:', data, default (data)[0])
  end_time = datetime.now ()
  print ('Продолжительность: {}'.format (end_time - start_time))

minimum (arr)

def maximum (arr):
  print ('Максимальные значения:')
  print ('Алгоритм "vibor_sort":')
  start_time = datetime.now ()
  for data in arr:
    print ('Максимальные значение из списка:', data, vibor_sort (data)[-1])
  end_time = datetime.now()
  print ('Продолжительность: {}'.format (end_time - start_time))
 
  print ('Алгоритм "bubble_for":')
  start_time = datetime.now ()
  for data in arr:
    print ('Максимальное значение из списка:', data, bubble_for (data)[-1])
  end_time = datetime.now ()
  print ('Продолжительность: {}'.format (end_time - start_time))

  print ('Алгоритм "bubble_while":')
  start_time = datetime.now ()
  for data in arr:
    print ('Максимальное значение из списка:', data, bubble_while (data)[-1])
  end_time = datetime.now ()
  print ('Продолжительность: {}'.format (end_time - start_time))

  print ('Алгоритм "insertion":')
  start_time = datetime.now ()
  for data in arr:
    print ('Максимальное значение из списка:', data, insertion (data)[-1])
  end_time = datetime.now ()
  print ('Продолжительность: {}'.format (end_time - start_time))
  
  print ('Алгоритм "default":')
  start_time = datetime.now ()
  for data in arr:
    print ('Максимальное значение из списка:', data, default (data)[-1])
  end_time = datetime.now ()
  print ('Продолжительность: {}'.format (end_time - start_time))

maximum (arr)
