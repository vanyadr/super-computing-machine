import pygame
import sys
import os
import requests

API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'


def geocode(address):
    # Собираем запрос для геокодера.
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": API_KEY,
        "geocode": address,
        "format": "json"}

    # Выполняем запрос.
    response = requests.get(geocoder_request, params=geocoder_params)

    if response:
        # Преобразуем ответ в json-объект
        json_response = response.json()
    else:
        print(response.status_code)

    features = json_response["response"]["GeoObjectCollection"]["featureMember"]
    return features[0]["GeoObject"] if features else None


def get_ll_span(address):
    toponym = geocode(address)
    if not toponym:
        print('Server error')
    else:
        print(toponym)
    a = toponym['boundedBy']['Envelope']
    print(a)

    spn1 = abs(float(a['lowerCorner'][0]) - float(a['upperCorner'][0]))
    spn2 = abs(float(a['lowerCorner'][1]) - float(a['upperCorner'][1]))
    spn = [spn1 + 0.006, spn2 + 0.006]

    ll = toponym['Point']['pos']
    ll = ll.split()
    ll = ','.join(ll)
    return ll, spn


def create_map(ll_spn=None, map_type="map", add_params=None):
    if ll_spn:
        map_request = f"http://static-maps.yandex.ru/1.x/?{ll_spn}&l={map_type}"
    else:
        map_request = f"http://static-maps.yandex.ru/1.x/?l={map_type}"

    if add_params:
        map_request += "&" + add_params
    response = requests.get(map_request)

    if not response:
        pass

    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)


toponym_to_find = input()


ll, spn = get_ll_span(toponym_to_find)
ll_spn = f"ll={ll}&spn={spn[0]},{spn[1]}"
create_map(ll_spn, "map", add_params=f"pt={ll}")
