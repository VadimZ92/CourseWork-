import copy
import os
import requests
import time
import json
from pprint import pprint
from tqdm import tqdm
import time
from VK import VK


class YD:

    def __init__(self, TokenYandexPoligon, list_photo_url):
        self.Token = TokenYandexPoligon
        # атрибут list_photo_url добавлен для вызова метода
        # находящегося в классе VK
        self.list_photo = list_photo_url

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'OAuth {}'.format(self.Token)
        }

    def disk_file_path(self, path):  # Создаем папку на яндекс диске
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        requests.put(f"{url}?path={path}", headers=headers)
        print("Создана папка 'Photo_VK' на Яндекс диске")
        time.sleep(2)
        return f"{url}?path={path}"

    def upload_to_yandexDisk(self, disk_file_path):
        print('Загрузка Фотографий на Яндекс Диск ')
        time.sleep(0.5)
        upload_url = \
            "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        with open('data.json') as file_object:
            # Список имен фотографий для записи на яндекс диск
            list_name_photo = json.load(file_object)
        # в цикле для конкретного файла берется имя для фото
        # и ее URL для записи на яндекс диск (сразу 2 цикла в одном),
        # цикл по двум спискам. tqdm - визуал
        for dikt_name_photo, url_photo in \
                tqdm(zip(list_name_photo, self.list_photo)):
            time.sleep(0.5)
            name = dikt_name_photo['file_name']
            # проверка на максимально возможное ограничение
            # по длине названия файла в Яндекс диске
            if len(name) > 12:
                name = name[:14]
            params = {"path": f'Photo_VK/{name}',
                      'url': url_photo}
            response = \
                requests.post(upload_url, headers=headers, params=params)
            time.sleep(1)  # время, чтобы успевал отработать алгоритм
        if 200 <= response.status_code < 400:
            print('Успешная загрузка Фотографий на Яндекс Диск ')
        elif response.status_code >= 400:
            print(f'Ошибка{response.status_code}')
