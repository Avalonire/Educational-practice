numbers = [1]
idx = 0
while numbers[idx] < 999:
    numbers.append(numbers[idx] + 2)
    idx += 1
for odd in range(len(numbers)):
    numbers[odd] **= 3
sum_task_1 = 0
sum_task_2 = 0
for idx in range(len(numbers)):
    sum_1 = 0
    num_1 = numbers[idx]
    num_task_2 = numbers[idx] + 17
    sum_2 = 0
    num_2 = num_task_2
    while num_task_2 // 10 > 0:
        sum_2 = sum_2 + num_task_2 % 10
        num_task_2 = num_task_2 // 10
    sum_2 = sum_2 + num_task_2
    if sum_2 % 7 == 0:
        sum_task_2 = sum_task_2 + num_2
    while numbers[idx] // 10 > 0:
        sum_1 = sum_1 + numbers[idx] % 10
        numbers[idx] = numbers[idx] // 10
    sum_1 = sum_1 + numbers[idx]
    if sum_1 % 7 == 0:
        sum_task_1 = sum_task_1 + num_1

print('task a =', sum_task_1)
print('task b =', sum_task_2)
