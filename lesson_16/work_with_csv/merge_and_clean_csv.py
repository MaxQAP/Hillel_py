import pandas as pd
from pathlib import Path


folder = Path(".")

csv_files = list(folder.glob("*.csv"))

if len(csv_files) != 2:
    print(f"Знайдено не 2 файли, а {len(csv_files)}: {csv_files}")
    exit()

print("Файли для обробки:")
for f in csv_files:
    print("   ", f.name)

df1 = pd.read_csv(csv_files[0])
df2 = pd.read_csv(csv_files[1])

combined = pd.concat([df1, df2], ignore_index=True)

cleaned = combined.drop_duplicates()

removed = len(combined) - len(cleaned)
print(f"Знайдено та видалено {removed} дублікатів")
print(f"Залишилось рядків: {len(cleaned)}")

#your_surname = "lazarets"
#output_file = folder / f"result_{your_surname}.csv"
output_file = folder / f"result_lazarets.csv"

cleaned.to_csv(output_file, index=False, encoding="utf-8")
print(f"Результат збережено у: {output_file}")