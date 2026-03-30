from http.client import responses

import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth
import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(current_dir, "test_search.log")
results_path = os.path.join(current_dir, "final_results.txt")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(log_path, mode='w', encoding='utf-8'),
        logging.StreamHandler()
    ],
    force=True
)
logger = logging.getLogger(__name__)


class TestSearchCarsI:
    @pytest.fixture(scope="class", autouse=True)
    def session(self):
        with open(results_path, "w", encoding='utf-8') as f:
            f.write("=== ЗВІТ ПОШУКУ ===\n\n")

        s = requests.Session()
        logger.info("--- Початок пошуку: Аутентифікація ---")

        response = s.post(
            "http://127.0.0.1:8080/auth",
            auth=HTTPBasicAuth('test_user', 'test_pass')
        )

        if response.status_code == 200:
            token = response.json().get("access_token")
            s.headers.update({"Authorization": f"Bearer {token}"})
            logger.info("Токен отримано успішно.")
            yield s
        else:
            logger.error(f"Помилка входу: {response.status_code}")
            pytest.fail("Не вдалося отримати доступ")

        logger.info("Завершення роботи тестів")
        s.close()


    @pytest.mark.parametrize("sort_by, limit", [
        ("price", 5),          # Топ 5 найдешевших
        ("year", 3),           # Топ 3 найстаріші
        ("engine_volume", 10), # 10 з найменшим об'ємом
        ("price", 2),          # 2 найдешевші
        ("year", 25),          # Весь список по рокам
        ("engine_volume", 1)   # 1 з найменшим об'ємом
    ])
    def test_search_cars(self, session, sort_by, limit):
        logger.info(f"Тест: сортування за '{sort_by}', ліміт {limit}")
        response = session.get(
            "http://127.0.0.1:8080/cars",
            params={"sort_by": sort_by, "limit": limit}
        )

        assert response.status_code == 200
        data = response.json()

        # Записую final_results,txt
        with open(results_path, "a", encoding='utf-8') as f:
            f.write(f"ПАРАМЕТРИ ПОШУКУ: sort_by={sort_by}, limit={limit}\n")
            f.write(f"ОТРИМАНО ОБ'ЄКТІВ: {len(data)}\n")
            f.write(json.dumps(data, indent=4, ensure_ascii=False))
            f.write("\n" + "="*50 + "\n\n")


        assert len(data) <= limit, f"Отримано {len(data)} машин, треба не більше {limit}"
        #print(response.json()) # це для виводу json в логи консольки
