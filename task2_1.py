from datetime import datetime

# Отримуємо поточні дату й час
today = datetime.now()

# Записуємо їх у файл як рядок
with open("today.txt", "w", encoding="utf-8") as file:
    file.write(today.strftime("%d.%m.%Y %H:%M:%S"))

# Зчитуємо рядок із файла
with open("today.txt", "r", encoding="utf-8") as file:
    today_string = file.read()

# Перетворюємо рядок на об'єкт дати й часу
date = datetime.strptime(today_string, "%d.%m.%Y %H:%M:%S")

# Виводимо складові
print("День:", date.day)
print("Місяць:", date.month)
print("Рік:", date.year)
print("Година:", date.hour)
print("Хвилина:", date.minute)
print("Секунда:", date.second)