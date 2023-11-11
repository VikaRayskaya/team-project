'''
Пользователь вводит свое имя и возраст. Исходя из полученных данных, определите в каком классе или на каком курсе учится
 человек. Принимаем за факт, что в школе человек учится 11 лет с 7 лет до 17 включительно, а в университете
 – 4 года с 18 лет до 21 включительно. Если человек нигде не учится, он считается “entrepreneur”.
 Также определите стаж человека в программировании. Стаж начинает копиться с 9 класса и считается на момент
 окончания года. Для примера, в 9 классе стаж составляет 1 год, в 10 классе – 2 и т.д. Выведите приветственное сообщение
  в формате:
“Hello, vova! You are at 2 course and have 5 years of programming experience. Sounds cool!”.
Соответственно, для человека, который не учится, вы заменяете “You are at 2 course” на “You are entrepreneur”.

'''

name = input()
message = "Hello, {}! ".format(name)

age = int(input())

if 7 <= age <= 17:
    message += "You are in {} grade".format(age - 6)
elif 17 < age <= 21:
    message += "You are at {} course".format(age - 17)
else:
    message += "You are entrepreneur"

if age > 15:
    message += " and have {} years of programming experience. Sounds cool!".format(age - 15)
else:
    message += " and have 0 years of programming experience. Sounds cool!"

print(message)

