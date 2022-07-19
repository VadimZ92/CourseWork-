from VK import VK
from YandexDisk import YD
import copy
import os
import requests
import time
import json
from pprint import pprint
from tqdm import tqdm
import time

access_token = 'vk1.a.xz2om2riQKMC5a3MgPz792dnFjJkNcVdqhtNBBxDnovy' \
               '4Sa7blXMmlrFXvIZaDeOLBD_4qMTRn_9PKFkHX3-cQzVCXAlA6' \
               'mm355Qj7_FhecBAHt3bRDmzsJAaA5He9mkMa0ADZHyERnWIvg6' \
               '-ZrU1fW2_bkYJnZ6PRAQReTmQrE6JU4ygpVsbC7e4adpfnCT'

user_id = input('Введите ID пользователя ВК: \n')
TokenYandexPoligon = input('Введите токен полигона ЯндексДиска: \n')

if __name__ == '__main__':
    vk = VK(access_token, user_id)
    vk.creation_json_photoList()
    # Вызов метода вне класса VK
    list_photo_url = VK(access_token, user_id).get_list_photo()
    # В объект класса YD пришлось добавить атрибут list_photo_url
    # для вызова метода get_list_photo() класса VK
    ya = YD(TokenYandexPoligon,
            list_photo_url=VK(access_token, user_id).get_list_photo())
    ya.disk_file_path('Photo_VK')
    ya.upload_to_yandexDisk(disk_file_path='Photo_VK')
