import random

name = input("Введите имя: ")
count = 0

while True:
    desire = input("Хотите ли играть? (Да/Нет) ")
    if desire.lower() == "нет":
        print("Программа завершена")
        break
    else:
        num = random.randint(0, 100)
        while True:
            guess = int(input("Угадайте число от 0 до 20: "))
            if guess != num:
                count += 1
                if count == 5:
                    print("У вас было 5 попыток, вы не угадали число")
                    break
            else:
                print("Поздравляем! Вы угадали!")
                print(f"Вам потребовалось {count} попыток чтобы угадать число")
                break
        continue_ = input("Хотите ли вы продолжить игру? (Да/Нет) ")
        if continue_.lower() != "да":
            print("Игра завершена")
            break
        count = 0