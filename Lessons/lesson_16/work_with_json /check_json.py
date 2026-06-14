import json
import logging
from pathlib import Path


handler = logging.FileHandler("json_logs.log")
handler.setLevel(logging.ERROR)

formatter = logging.Formatter("%(asctime)s | ERROR | %(message)s")
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
logger.addHandler(handler)

FOLDER = Path(__file__).parent

def main():
    print("Перевірка папки:", FOLDER.absolute())

    json_files = list(FOLDER.glob("*.json"))
    print(f"Знайдено .json файлів: {len(json_files)}")

    if json_files:
        print("Імена файлів:")
        for f in json_files:
            print("   ", f.name)
    else:
        print("Немає файлів *.json у папці")
        logger.error(f"Немає файлів *.json в папці {FOLDER.absolute()}")
        return

    bad = 0
    for path in json_files:
        try:
            with path.open("r", encoding="utf-8") as f:
                json.load(f)
            print(path.name, "— OK")
        except json.JSONDecodeError as e:
            bad += 1
            msg = f"{path.name} — невалідний JSON: {e.msg} (рядок {e.lineno}, позиція {e.pos})"
            print("✗", msg)
            logger.error(msg)
        except Exception as e:
            bad += 1
            msg = f"{path.name} — помилка: {type(e).__name__} {e}"
            print("!", msg)
            logger.error(msg)

    print(f"\nНе тих файлів: {bad}")
    if bad > 0:
        print("Помилки записано в json_logs.log")

if __name__ == "__main__":
    main()