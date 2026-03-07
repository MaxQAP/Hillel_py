

import logging
from pathlib import Path
import xml.etree.ElementTree as ET

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-5s | %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

def print_group_incoming(number):
    path = Path("/Users/max/PycharmProjects/Hillel_py/lesson_16/work_with_xml/groups.xml")

    if not path.exists():
        logger.error(f"Файл відсутній: {path.resolve()}")
        return

    try:
        tree = ET.parse(path)
        root = tree.getroot()
        target = str(number)

        for group in root.findall("./group"):
            if group.find("number").text == target:
                inc = group.find("./timingExbytes/incoming")
                val = inc.text.strip() if inc is not None and inc.text else "немає значення"
                logger.info(f"Група {target:>3} → incoming = {val}")
                return

        logger.info(f"Група {target} не знайдена")

    except Exception as e:
        logger.error(f"Помилка: {e}")

if __name__ == "__main__":
    print_group_incoming(-1)
    print_group_incoming(0)
    print_group_incoming(1)
    print_group_incoming(2)
    print_group_incoming(4)
    print_group_incoming(5)
    print_group_incoming(6)
