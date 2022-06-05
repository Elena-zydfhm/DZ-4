# 3. Вот вам файл с тысячей чисел. https://cloud.mail.ru/public/DQgN/LqoQzPEec
# Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа,
# которые в сумме дают 0. (решение будет долгим, ибо является демонстрационным при теме
# многопоточного программирования).
file = 'TASK 3.py/1Kints.txt'
nums = []
with open(file, 'r') as read_file:
    for line in read_file.readlines():
      nums.extend(line.split())

nums_int = []
for i in nums:
  nums_int.append(int(i))

for i in range(len(nums_int)):
  for j in range(i + 1, len(nums_int)):
    for k in range(j + 1, len(nums_int)):
      if nums_int[i] + nums_int[j] + nums_int[k] == 0:
        print(nums_int[i], nums_int[j], nums_int[k])