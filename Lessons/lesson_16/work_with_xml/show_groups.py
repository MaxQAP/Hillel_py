import logging
from pathlib import Path
import xml.etree.ElementTree as ET


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-5s | %(message)s',
    datefmt='%H:%M:%S'
)

logger = logging.getLogger(__name__)


def get_incoming_by_group_number(group_number: int | str) -> str | None:
    xml_path = Path(__file__).parent / "groups.xml"

    if not xml_path.exists():
        logger.error(f"Файл не знайдено: {xml_path.resolve()}")
        logger.error(f"Очікуваний шлях: {xml_path.parent}")
        return None

    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        target = str(group_number).strip()

        for group in root.findall(".//group"):
            num_elem = group.find("number")
            if num_elem is not None and num_elem.text and num_elem.text.strip() == target:
                incoming_elem = group.find(".//incoming")
                if incoming_elem is not None and incoming_elem.text:
                    value = incoming_elem.text.strip()
                    logger.info(f"Група {target:>3} → incoming = {value}")
                    return value
                else:
                    logger.info(f"Група {target:>3} знайдена, але <incoming> відсутній або порожній")
                    return None

        logger.info(f"Група {target} не знайдена")
        return None

    except ET.ParseError as e:
        logger.error(f"Помилка парсингу XML: {e}")
        return None
    except Exception as e:
        logger.error(f"Непередбачена помилка: {type(e).__name__} → {e}")
        return None


if __name__ == "__main__":

    get_incoming_by_group_number(0)
    get_incoming_by_group_number(2)
    get_incoming_by_group_number(4)
    get_incoming_by_group_number(5)
    get_incoming_by_group_number(1)
    get_incoming_by_group_number(3)  # не знайдена