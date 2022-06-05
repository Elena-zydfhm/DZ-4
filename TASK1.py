 #Дан список чисел. Создать список в который попадают числа, 
 #описывающие возрастающую последовательность и содержащие 
 #максимальное количество элементов. 
 #Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
 #[5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7] Порядок элементов менять нельзя

numbers = [5, 2, 3, 4, 6, 1, 7]
lenghts = [1]*len(numbers)
order = list(range(len(numbers)))

for k in range(len(numbers)):
    for i in range(k):
        if numbers[i] < numbers[k]:
            if lenghts[i] >= lenghts[k]:
                lenghts[k] = lenghts[i] + 1
                order[k] = i

new_num = []
ind = lenghts.index(max(lenghts))
while order[ind] != ind:
    new_num.append(numbers[ind])
    ind = order[ind]
new_num.append(numbers[ind])

print(sorted(new_num))