from time import sleep

from browser import Browser
from database import Data
from logger import logger
import sms_man_api

LOG = logger('client')


class Client:
    def __init__(self):
        self.data = Data()
        self.nicknames = iter(self.data('nickname'))
        self.passwords = iter(self.data('password'))
        self.f_names = iter(self.data('f_name'))
        self.s_names = iter(self.data('s_name'))
        self.proxys = iter(self.data('proxy'))

    def smsman(self):
        _, request_id, number = sms_man_api.get_number(0, 'go').content.decode().split(':')
        if not number:
            return False
        proxy = next(self.proxys)
        f_name = next(self.f_names)
        l_name = next(self.s_names)
        nickname = next(self.nicknames)
        password = next(self.passwords)
        with Browser(proxy) as browser:
            if not browser.reg(number, f_name, l_name, nickname, password):
                return False
            sms_code = None
            for _ in range(20):
                req = (sms_man_api.get_sms(request_id))
                print(req)
                sms_code = req.get('sms_code', None)
                if sms_code is not None:
                    break
                sleep(1)
            if sms_code is not None:
                result = browser.phone_confirmation(sms_code)
            browser.second_page()
            sms_man_api.set_status(request_id, 'reject')
            LOG.info(result)
            return result

    def reg(self, method, amount):
        LOG.info(method)
        methods = {
            'smsman': self.smsman,
        }
        result = 0
        while result < amount:
            if methods.get(method)():
                result += 1


def main():
    client = Client()
    client.reg('smsman', 1)


if __name__ == '__main__':
    try:
        main()
    except BaseException as error:
        LOG.exception(error)
