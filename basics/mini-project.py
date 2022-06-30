import random
vegetables = ["помидор", "огурец", "капуста", "редка", "перец"]

while True:
    attempts = 5
    word = random.choice(vegetables)
    word1 = word
    letters = ""
    for w in range(len(word)):
        letters += "*"
    print(f"Угадайте слово (овощь): {letters}")

    while True:
        letter = input("Введите букву: ").lower()
        if letter in word:
            for i in word:
                if letter == i:
                    index = word1.index(i)
                    letters = letters[:index] + letter + letters[index+1:]
                    word1 = word1[:index] + '!' + word1[index+1:]
            print("Правильно")
            print(letters)
            if letters == word:
                print("Вы выиграли!")
                print(f"Загаданное слово: {word}")
                break
        else:
            attempts -= 1
            print("Такой буквы нет в загаданном слове")
            print(f"У вас осталось {attempts} попыток")
            if attempts == 0:
                print("Вы проиграли")
                break
    one_more = input("Хотите сыграть ещё раз? (да/нет): ")
    if one_more.lower() == "нет":
        break