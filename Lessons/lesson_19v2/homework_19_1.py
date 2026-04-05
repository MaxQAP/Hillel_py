import requests
import os

BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}

# Отримання файлів по nasa_id
asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"

print("Виконую пошук у NASA Library...")
response = requests.get(search_url, params=search_params)
response.raise_for_status()

search_results = response.json()
items = search_results.get("collection", {}).get("items", [])

nasa_ids = [item["data"][0]["nasa_id"] for item in items[:2]]

if not nasa_ids:
    print("Зображень не знайдено.")
else:
    for index, nasa_id in enumerate(nasa_ids, start=1):
        print(f"\nОбробка об'єкта {index} (ID: {nasa_id})...")

        asset_url = f"{BASE_URL}/asset/{nasa_id}"
        asset_response = requests.get(asset_url)
        asset_response.raise_for_status()

        assets = asset_response.json().get("collection", {}).get("items", [])

        image_url = next((item["href"] for item in assets if item["href"].endswith(".jpg")), None)

        if image_url:
            print(f"Завантаження: {image_url}")
            img_data = requests.get(image_url).content

            filename = f"mars_photo{index}.jpg"
            with open(filename, 'wb') as handler:
                handler.write(img_data)

            print(f"Збережено як {filename}")
        else:
            print(f"Не вдалося знайти JPG для  {nasa_id} ID")

print("\nПошук завершено.")