import os
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import json
import datetime


async def fetch_html(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    while True:
        async with aiohttp.ClientSession() as session:
            html = await fetch_html(session, 'https://realty.yandex.ru/sankt-peterburg/snyat/kvartira/')

            # Использую BeautifulSoup для парсинга HTML-кода
            soup = BeautifulSoup(html, 'html.parser')

            main_info = {
                "title": soup.title.string,
                "html_content": str(soup),
                "timestamp": str(datetime.datetime.now())
            }

            # Сохраняю основную информацию в JSON файл
            with open('realty_page.json', 'w', encoding='utf-8') as json_file:
                json.dump(main_info, json_file, ensure_ascii=False, indent=4)

            apartments = parse_apartments('realty_page.json')

            script_directory = os.path.dirname(os.path.abspath(__file__))
            artifacts_directory = os.path.join(script_directory, "artifacts")
            os.makedirs(artifacts_directory, exist_ok=True)

            with open(os.path.join(artifacts_directory, "artifact_1.txt"), "a", encoding="utf-8") as file:
                file.write(f"Updated at {datetime.datetime.now()}:\n")

                for apartment in apartments:
                    file.write(f"Здание: {remove_nbsp(apartment['building'])}\n")
                    file.write(f"Квартира: {remove_nbsp(apartment['title'])}\n")
                    file.write(f"Улица: {remove_nbsp(apartment['address'])}\n")
                    file.write(f"Метро: {remove_nbsp(apartment['metro'])}\n")
                    file.write(f"Описание: {remove_nbsp(apartment['description'])}\n")
                    file.write("-" * 30 + "\n")

        await asyncio.sleep(3600)  # Подождать 1 час перед следующим выполнением


def parse_apartments(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    soup = BeautifulSoup(data['html_content'], 'html.parser')
    apartment_items = soup.find_all('li', class_='OffersSerpItem')

    apartments = []
    for item in apartment_items:
        apartment_info = {
            'title': item.find('span', class_='OffersSerpItem__title').text.strip(),
            'building': item.find('div', class_='OffersSerpItem__building').text.strip(),
            'address': item.find('div', class_='OffersSerpItem__address').text.strip(),
            'metro': item.find(class_='MetroStation__title').text.strip() if item.find(
                class_='MetroStation__title') else 'Метро не указано',
            'description': item.find(class_='OffersSerpItem__description').text.strip() if item.find(
                class_='OffersSerpItem__description') else 'Описание не указано',
        }
        apartments.append(apartment_info)

    return apartments


def remove_nbsp(text):
    return text.replace('\xa0', ' ')


if __name__ == "__main__":
    asyncio.run(main())
