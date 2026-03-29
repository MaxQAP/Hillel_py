import json
import logging
from pathlib import Path

logger = logging.getLogger("json_checker")
logger.setLevel(logging.ERROR)

handler = logging.FileHandler(
    Path(__file__).with_name("json_logs_lazarets.log"),
    encoding="utf-8"
)
handler.setLevel(logging.ERROR)

formatter = logging.Formatter("%(asctime)s | ERROR | %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)


#FOLDER = Path(".") - для перевірки логів 1
FOLDER = Path(__file__).parent

def main():
    print("Перевірка папки:", FOLDER.absolute())

    json_files = list(FOLDER.glob("*.json"))
    #json_files = list(FOLDER.glob("*.txt")) - для перевірки логів 2
    print(f"Зайдено .json файлов: {len(json_files)}")
    #print(f"Зайдено .txt файлов: {len(json_files)}") - для перевірки логів 2.1
    if json_files:
        print("Імʼя файлів:")
        for f in json_files:
            print("   ", f.name)

    if not json_files:
        print("Нема файлів *.json папці")
        logger.error("Нема файлів *.json в папці " + str(FOLDER.absolute()))
        return

    bad = 0
    for path in json_files:
        try:
            with path.open("r", encoding="utf-8") as f:
                json.load(f)
            print(path.name, "— OK")
        except json.JSONDecodeError as e:
            bad += 1
            msg = f"{path.name} — невалідний JSON: {e.msg} (строка {e.lineno}, поз. {e.pos})"
            print("✗", msg)
            logger.error(msg)
        except Exception as e:
            bad += 1
            msg = f"{path.name} — помилка: {type(e).__name__} {e}"
            print("!", msg)
            logger.error(msg)

    print(f"\n Поганих файлів: {bad}")
    if bad > 0:
        print("Помилки записани в json_logs.log")

if __name__ == "__main__":
    main()