# Задача 34
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# Ввод: 
# пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод:
# Парам пам-пам

input_list = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
temp_list = input_list.split()
glasnye = ['а', 'у', 'е', 'о', 'ы', 'я', 'и', 'ю']
count_set = set()
for i in temp_list:
    count = 0
    for letter in i:
        if letter in glasnye:
            count = count + 1
    count_set.add(count)

if len(count_set) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')