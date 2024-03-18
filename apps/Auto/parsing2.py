import requests
from bs4 import BeautifulSoup

base_url = 'https://autazeszwajcarii.pl/'


def extract_data_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Найдем элементы с классами 'icon-checkbox-checked red' и 'icon-checkbox-checked grey'
        red_icons = soup.find_all(class_='icon-checkbox-checked red')
        grey_icons = soup.find_all(class_='icon-checkbox-checked grey')

        # Инициализируем списки для данных с классами 'icon-checkbox-checked red' и 'icon-checkbox-checked grey'
        red_data = [icon['title'] for icon in red_icons]
        grey_data = [icon['title'] for icon in grey_icons]

        return red_data, grey_data

    except Exception as e:
        print(f"An error occurred while extracting data from {url}: {str(e)}")
        return [], []


def main():
    with open('unique_links.txt', 'r') as file:
        links = file.readlines()

    with open('red_data.txt', 'w') as red_output_file, open('grey_data.txt', 'w') as grey_output_file:
        for link in links:
            url = base_url + link.strip()
            red_data, grey_data = extract_data_from_url(url)

            # Записываем данные с классом 'icon-checkbox-checked red' в отдельный файл
            for data in red_data:
                red_output_file.write(data + '\n')

            # Записываем данные с классом 'icon-checkbox-checked grey' в отдельный файл
            for data in grey_data:
                grey_output_file.write(data + '\n')

if __name__ == "__main__":
    main()
