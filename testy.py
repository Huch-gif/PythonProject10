import pandas as pd
import numpy as np

np.random.seed(42)

names = [
    'Александр', 'Мария', 'Дмитрий', 'Елена', 'Андрей',
    'Ольга', 'Иван', 'Анна', 'Сергей', 'Наталья'
]

subjects = ['Математика', 'Физика', 'Химия', 'Русский язык', 'Английский язык']

grades = np.random.randint(2, 6, size=(10, 5))

df = pd.DataFrame(grades, index=names, columns=subjects)

print("Оценки учеников:")
print(df)
print("-" * 60)

print("1. Средняя оценка по каждому предмету:")
print(df.mean())
print()

print("2. Медианная оценка по каждому предмету:")
print(df.median())
print()

print("3. Стандартное отклонение по каждому предмету:")
print(df.std().round(3))  # округляем до 3 знаков
print()

print("4. Квартили и IQR по математике:")
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print(f"   Q1 (25-й перцентиль): {Q1_math}")
print(f"   Q3 (75-й перцентиль): {Q3_math}")
print(f"   IQR (межквартильный размах): {IQR_math}")
print()


print("Дополнительно: описательная статистика по математике")
print(df['Математика'].describe())
