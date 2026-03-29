import json
import logging
from pathlib import Path


logger = logging.getLogger("json_validator")
logger.setLevel(logging.ERROR)

file_handler = logging.FileHandler("json__your_second_name.log", encoding="utf-8")
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter("%(asctime)s  %(levelname)-7s  %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# ────────────────────────────────────────────────
# Шлях до папки (можна передати аргументом, але тут захардкодимо)
# ────────────────────────────────────────────────

FOLDER = Path("lesson_16/work_with_json")

def main():
    if not FOLDER.is_dir():
        print(f"Папка {FOLDER} не існує або це не директорія")
        return

    json_files = list(FOLDER.glob("*.json"))

    if not json_files:
        print("У папці немає файлів *.json")
        return

    print(f"Знайдено {len(json_files)} json-файлів\n")

    invalid_count = 0

    for path in sorted(json_files):
        try:
            with path.open("r", encoding="utf-8") as f:
                json.load(f)
            print(f"  ✓  {path.name}")
        except json.JSONDecodeError as e:
            invalid_count += 1
            msg = f"{path.name}  →  невалідний JSON\n    {e.msg}  (рядок {e.lineno}, позиція {e.pos})"
            print(f"  ✗  {msg}")
            logger.error(msg)
        except Exception as e:
            invalid_count += 1
            msg = f"{path.name}  →  не вдалося прочитати файл: {type(e).__name__}  {e}"
            print(f"  !  {msg}")
            logger.error(msg)

    print(f"\nПеревірка завершена. Знайдено {invalid_count} невалідних файлів.")
    if invalid_count > 0:
        print(f"Деталі помилок записано у файл: json__your_second_name.log")


if __name__ == "__main__":
    main()