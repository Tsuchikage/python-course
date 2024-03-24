import aiohttp
from bs4 import BeautifulSoup
import json
import datetime
import pandas as pd
from pathlib import Path
from aiomisc import new_event_loop, PeriodicCallback


async def fetch_html(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch_html(session, 'https://realty.yandex.ru/sankt-peterburg/snyat/kvartira/')

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

        artifacts_directory = Path("artifacts")
        artifacts_directory.mkdir(parents=True, exist_ok=True)

        # Записываем информацию о квартирах в CSV файл
        csv_file_path = artifacts_directory / "apartments_info.csv"
        df = pd.DataFrame(apartments)
        df.to_csv(csv_file_path, index=False)


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


if __name__ == "__main__":
    loop = new_event_loop()
    periodic = PeriodicCallback(main)

    periodic.start(3600, delay=0)
    loop.run_forever()
