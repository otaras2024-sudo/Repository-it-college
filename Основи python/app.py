"""
Лабораторна робота: Основи програмування на Python
Студент: Олександр Тарас (КН-31)
"""

from random import randint

# 1. Ознайомлення з основними типами даних
student_name = "Олександр Тарас"
group_code = "КН-31"
course_year = 3
gpa_score = 4.8
skills = ["Python", 3.12, True, "ООП"]
student_profile = {"name": student_name, "group": group_code, "course": course_year}
location = (49.8429, 24.0311)
study_topics = {"kn31", "python_basics", "lviv_polytechnic"}

print(f"Студент: {student_name}, Група: {group_code}, Курс: {course_year}, Рейтинг: {gpa_score}")
print(f"Список навичок: {skills}")
print(f"Словник студента: {student_profile}")
print(f"Координати: {location}")
print(f"Множина тегів: {study_topics}")

# 2. Вбудовані константи та ключові слова
print("Константа True:", True)
print(f"Константа False: {False}")
print(f"Константа None: {None}, тип: {type(None)}")
print(f"Константа Ellipsis: {...}, тип: {type(...)}")

# 3. Вбудовані функції
print(abs(-18.7), f"дорівнює {abs(18.7)}, перевірка рівності:", abs(-18.7) == abs(18.7))
print(f"Кількість елементів списку: {len(skills)}")
print(f"Тип змінної gpa_score: {type(gpa_score)}")

# 4. Цикли for та while з else
study_modules = ["Змінні", "Типи даних", "Умовні оператори", "Функції"]
for i in range(len(study_modules)):
    print(f"Модуль {i + 1}: {study_modules[i]}")
else:
    print("Цикл for завершився без break")

counter = 0
while counter < 3:
    print(f"Ітерація while: {counter}")
    counter += 1
else:
    print("Цикл while успішно завершився")

# 5. Розгалуження
is_active = randint(0, 1)
print(f"Статус активний ({is_active})" if is_active else f"Статус неактивний ({is_active})")

# 6. Обробка винятків try -> except -> finally
divisor = 0
try:
    print("Ділення числа на нуль:")
    res = 50 / divisor
except ZeroDivisionError as err:
    print("Перехоплено виняток:", err)
finally:
    print("Блок finally виконано")

# 7. Контекстний менеджер with для роботи з файлами
try:
    with open("README.md", "r", encoding="utf-8") as file:
        print("Перші рядки файлу README.md:")
        for line_no, line in enumerate(file):
            if line_no < 5:
                print(f"  {line_no + 1}: {line.strip()}")
except FileNotFoundError:
    print("Файл README.md не знайдено.")

# 8. Лямбда-функції
def get_user_data(name, group):
    return name, group

show_user = lambda name, group: f"Студент: {name}, Група: {group}"
print("Звичайна функція:", get_user_data)
print("Лямбда-функція:", show_user)
print("Прямий виклик лямбди:", show_user("Олександр", "КН-31"))
print("Виклик із розпакуванням:", show_user(*get_user_data("Олександр", "КН-31")))
