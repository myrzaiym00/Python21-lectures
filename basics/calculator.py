first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))
operation = input("Выберите операцию из следующих +-*/%**// : ")

if operation == "+":
    answer = first_num + second_num
elif operation == "-":
    answer = first_num - second_num
elif operation == "*":
    answer = first_num * second_num
elif operation == "/":
    answer = first_num / second_num
elif operation == "%":
    answer = first_num % second_num
elif operation == "**":
    answer = first_num ** second_num
elif operation == "//":
    answer = first_num // second_num
else:
    answer = "Данной операции нет в системе"

print(f"Ответ: {answer}")