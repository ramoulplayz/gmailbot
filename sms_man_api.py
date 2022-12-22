import json
from time import sleep

import requests

from logger import logger

smsman_token = '7jum0G6_tqXLCIZoAbMo8luIh6HW2IgQ'
URL = 'http://api.sms-man.ru/control'
LOGGER = logger('sms_man')


# def countries():
#     data = {
#         '$api_key': smsman_token,
#     }
#     return requests.get(f'http://api.sms-man.ru/stubs/handler_api.php?action=getCountries', data=data)
#

def balance():
    result = requests.get(f'{URL}/get-balance?token={smsman_token}').json().get('balance')
    return result


def limits(country_id):
    result = requests.get(f'http://api.sms-man.ru/stubs/handler_api.php?'
                          f'action=getPrices'
                          f'&api_key={smsman_token}'
                          f'&country={country_id}').json()
    LOGGER.info(result)
    return result
    # return requests.get(f'{URL}/limits?token={smsman_token}&country_id=${country_id}&application_id=${application_id}')


def get_number(country_id: int, application_id: str):
    result = requests.get(f'http://api.sms-man.ru/stubs/handler_api.php?action=getNumber&'
                          f'api_key={smsman_token}&'
                          f'service={application_id}&'
                          f'country={country_id}')
    return result
    # return requests.get(f'{URL}/get-number?token={smsman_token}&country_id={country_id}&application_id={application_id}').json()


def get_sms(request_id):
    result = requests.get(f'{URL}/get-sms?token={smsman_token}&request_id={request_id}').json()
    return result


def set_status(request_id, status):
    result = requests.get(f'{URL}/set-status?token={smsman_token}&request_id={request_id}&status={status}').json()
    return result


def countries():
    result = requests.get(
        f'http://api.sms-man.ru/stubs/handler_api.php?action=getCountries&api_key={smsman_token}').json()
    return result


def applications():
    result = requests.get(f'{URL}/applications?token={smsman_token}').json()
    return result
