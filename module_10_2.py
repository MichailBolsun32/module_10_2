from threading import Thread # Для мультипоточной работы
import time

#Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
#    Атрибут name - имя рыцаря. (str)
#    Атрибут power - сила рыцаря. (int)

class Knight(Thread):# Наследует от Thread, для создания потоков
    NUMBER_ENEMY = 100 # кол-во врагов

    def __init__(self, nama, power):
        super().__init__()  # т.к. в родителе Thread в .start() есть проверка на __init__ и его надо сохранить
        self.nama = nama
        self.power = power

#   А также метод run, в котором рыцарь будет сражаться с врагами:
#    При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
#    Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
#    В процессе сражения количество врагов уменьшается на power текущего рыцаря.
#    По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>..., осталось <кол-во воинов> воинов."
#    После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!

    def run(self):
        print(f'{self.nama}, на нас напали!')
        num_dey = self.NUMBER_ENEMY // self.power
        for deys in range(num_dey):
            time.sleep(1)
            print(f'{self.nama}, сражается {deys + 1} день(дня), осталось {self.NUMBER_ENEMY - self.power * (deys + 1)} воинов')

        print(f'{self.nama}, одержал победу спустя {deys + 1} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились')
