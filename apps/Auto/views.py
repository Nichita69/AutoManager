# views.py

import json
from django.http import JsonResponse
from apps.Auto.models import Car

def upload_car_data_from_json_file(request):
    try:
        file_path = 'путь_к_вашему_файлу.json'
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                car = Car.objects.create(
                    Typ=item.get('Typ'),
                    Farbe=item.get('Farbe'),
                    Hubraum=item.get('Hubraum'),
                    Zustand=item.get('Zustand'),
                    Neupreis=item.get('Neupreis'),
                    Referenz=item.get('Referenz'),
                    Zeitwert=item.get('Zeitwert'),
                    Bereifung=item.get('Bereifung'),
                    Letzte_MFK=item.get('Letzte MFK'),
                    Ausstattung=item.get('Ausstattung'),
                    Schaden_Nr=item.get('Schaden-Nr'),
                    Typenschein=item.get('Typenschein'),
                    Reparaturkosten=item.get('Reparaturkosten'),
                    Bauart_Aufbau_Türen=item.get('Bauart / Aufbau / Türen')
                )
            return JsonResponse({"message": "Данные успешно загружены в базу данных"})
    except FileNotFoundError:
        return JsonResponse({"error": "Файл не найден"}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Ошибка декодирования JSON"}, status=400)



