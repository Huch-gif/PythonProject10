import pandas as pd

df = pd.read_csv('dz.csv')

print("Первые строки данных:")
print(df.head())

df_clean = df.dropna(subset=['City', 'Salary'])

df_clean['Salary'] = pd.to_numeric(df_clean['Salary'], errors='coerce')

df_clean = df_clean.dropna(subset=['Salary'])

df_clean['Salary'] = df_clean['Salary'].astype(int)

average_salary = df_clean.groupby('City')['Salary'].mean()

print("\nСредняя зарплата по городам:")
print(average_salary)

print("\nСредняя зарплата (красивый формат):")
for city, avg in average_salary.items():
    print(f"{city}: {avg:,.0f} ₽")