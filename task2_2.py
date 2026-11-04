from datetime import date, timedelta

year = int(input("Введіть рік народження: "))
month = int(input("Введіть місяць народження: "))
day = int(input("Введіть день народження: "))

# Створюємо об'єкт із датою народження
happy = date(year, month, day)

# Назви днів тижня
weekdays = [
    "понеділок",
    "вівторок",
    "середа",
    "четвер",
    "п’ятниця",
    "субота",
    "неділя"
]

# Визначаємо день тижня
weekday = weekdays[happy.weekday()]

# Додаємо до дати народження 13 330 днів
result = happy + timedelta(days=13330)

# Записуємо відповіді у файл
with open("birthday.txt", "w", encoding="utf-8") as file:
    file.write("Яка дата вашого народження?: "
               + happy.strftime("%d.%m.%Y") + "\n")

    file.write("У який день тижня ви народилися?: "
               + weekday + "\n")

    file.write("Коли вам буде (або вже було) 13 330 днів від народження?: "
               + result.strftime("%d.%m.%Y") + "\n")

print("Відповіді записано у файл birthday.txt")