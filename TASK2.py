# 2. Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого
# файла по возрастанию.
from random import randint
path = 'fille.txt'
count = 100
with open(path, 'w') as write_file:
  for i in range(count):
    num = str(randint(0, 1000))
    write_file.write(num + '\n')
with open(path, 'r') as read_file:
  list_int = []
  for line in read_file.readlines():
    list_int.extend(line.split())

with open(path, 'w') as write_file:
  nums = []
  for i in list_int:
    nums.append(int(i))
  nums = sorted(nums)
  for num in nums:
    write_file.write(str(num) + '\n')
