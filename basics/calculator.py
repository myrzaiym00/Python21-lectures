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


class Solution:
    def twoSum(nums, target):
        nums1 = nums.copy()
        for i in nums:
            nums1.pop(0)
            for j in nums1:
                if i + j == target:
                    index1 = nums.index(i)
                    if nums.count(i) > 1 and nums[0] != i:
                        index2 = nums1.index(j) + 2
                    else:
                        index2 = nums1.index(j) + 1
                    result = [index1, index2]
                    return result