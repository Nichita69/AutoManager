import requests
from bs4 import BeautifulSoup
import json

base_url = 'https://autazeszwajcarii.pl/'

def extract_images_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        image_tags = soup.find_all('img')
        image_urls = [img['src'] for img in image_tags if '/auction_photos/' in img['src']]
        return image_urls
    except Exception as e:
        print(f"An error occurred while extracting images from {url}: {str(e)}")
        return []

# Открываем файл с уникальными ссылками
with open('unique_links.txt', 'r') as file:
    links = file.readlines()

cars_data = []

# Обработка каждой ссылки
for link in links:
    link = link.strip()
    full_url = base_url + link
    response = requests.get(full_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.text.strip()
        print("Title:", title)  # Выводим заголовок страницы

        # Извлекаем ссылки на изображения
        image_urls = extract_images_from_url(full_url)
        unique_image_urls = list(set(image_urls))  # Преобразуем список в множество для удаления дубликатов

        # Проверяем таблицу с данными о машине
        table = soup.find('table')
        if table:
            rows = table.find_all('tr')
            car_data = {}
            for row in rows:
                cells = row.find_all('td')
                if len(cells) == 2:
                    key = cells[0].text.strip()
                    value = cells[1].text.strip()
                    car_data[key] = value
            car_data['images'] = unique_image_urls  # Добавляем уникальные ссылки на изображения
            print("Car data (from table):", car_data)  # Выводим данные о машине в виде словаря
            cars_data.append(car_data)  # Добавляем данные о машине в список
        else:
            print("Failed to find table on page:", full_url)
        info_div = soup.find('div', class_='auction-details-more-info')
        if info_div:
            rows = info_div.find_all('tr')
            car_data = {}
            for row in rows:
                cells = row.find_all('td')
                if len(cells) == 2:
                    key = cells[0].text.strip()
                    value = cells[1].text.strip()
                    car_data[key] = value
            car_data['images'] = unique_image_urls
            print("Car data (from info div):", car_data)
            cars_data.append(car_data)  # Добавляем данные о машине в список
        else:
            print("Failed to find info div on page:", full_url)
    else:
        print("Failed to fetch page at", full_url)

# Записываем данные в файл JSON
with open('cars_data.json', 'w') as json_file:
    json.dump(cars_data, json_file, indent=4)

print("Данные были сохранены в cars_data.json")
