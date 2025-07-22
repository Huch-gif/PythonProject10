import pandas as pd


df = pd.read_csv('dinoDatasetCSV.csv')

print("Первые 5 строк данных:")
print(df.head())

print("\nИнформация о данных (.info()):")
print(df.info())

print("\nСтатистическое описание (.describe()):")
print(df.describe())