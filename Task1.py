import os
import glob
import time
from datetime import datetime

# Робимо папку програми поточним каталогом
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1. Повний шлях і список файлів поточного каталогу
print("Поточний каталог:", os.getcwd())

print("Файли в каталозі:")
for name in os.listdir():
    if os.path.isfile(name):
        print(name)

# 2. Розмір файла в байтах
size = os.path.getsize("first.txt")
print("\nРозмір first.txt:", size, "байт")

# 3. Пошук файлів за шаблоном
print("\nТекстові файли:")
for name in glob.glob("*.txt"):
    print(name)

# 4. Копіювання даних із першого файла у другий
with open("first.txt", "r", encoding="utf-8") as file:
    text = file.read()

with open("second.txt", "w", encoding="utf-8") as file:
    file.write(text)

# Читання другого файла
with open("second.txt", "r", encoding="utf-8") as file:
    print("\nВміст second.txt:")
    print(file.read())

# Видалення першого файла
os.remove("first.txt")
print("Файл first.txt видалено.")

# 5. Поточна дата й час
now = datetime.now()
print("\nПоточна дата й час:", now.strftime("%d.%m.%Y %H:%M:%S"))

# 6. Кількість повних днів і років від початку епохи Unix
seconds = time.time()
days = int(seconds // (24 * 60 * 60))
years = days // 365

print("\nДнів від початку епохи Unix:", days)
print("Років від початку епохи Unix:", years)