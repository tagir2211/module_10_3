from random import choice
from threading import Lock, Thread
from time import sleep


class Bank:
    def __init__(self, balanse):
        self.balanse = balanse
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            rand_add = choice(([x for x in range(50, 500)]))
            self.balanse += rand_add
            if self.balanse >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение:{rand_add} . Баланс:{self.balanse}.')
            sleep(0.001)

    def take(self):
        for i in range(100):
            rand_add = choice(([x for x in range(50, 500)]))
            print(f'Запрос на {rand_add}.')
            if self.balanse < rand_add:
                print('Запрос откланен. Недостаточно средств.')
                self.lock.acquire()
            else:
                self.balanse -= rand_add
                print(f'Снятие: {rand_add}. Баланс: {self.balanse}.')


bk = Bank(100)

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balanse}')
