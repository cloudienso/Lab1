# Получаем число от пользователя
try:
    score = int(input("Введи число: "))
except ValueError:
    print("Ошибка: нужно ввести целое число")
    exit(1)

# Проверяем диапазон и выводим результат
print("Это ", end="")

if 0 <= score < 25:
    print("Ужасно (6)")
elif 25 <= score < 45:
    print("Плохо (5)")
elif 45 <= score < 65:
    print("Сойдет (4)")
elif 65 <= score < 80:
    print("Средне (3)")
elif 80 <= score < 90:
    print("Хорошо (2)")
elif 90 <= score <= 100:
    print("Очень хорошо (1)")
else:
    print("Неправильно (0)")