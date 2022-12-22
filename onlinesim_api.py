from configparser import ConfigParser
from time import sleep

from onlinesimru import GetUser, GetNumbers
from onlinesimru.Extentions import RequestException

from logger import logger

config = ConfigParser()
config.read("config.ini")
onlineSim_token = config['online_sim']['onlineSim_token']
LOGGER = logger('tg_reg', file='tg_reg.log')


class OnlineSim:
    def __init__(self):
        self.sim = GetNumbers(onlineSim_token)
        self.user = GetUser(onlineSim_token)

    def balance(self):
        return self.user.balance()["balance"]

    def numbers(self):
        return self.sim.state()

    def get_number(self, service, country):
        return self.sim.get(service, country=country)

    def code(self, tzid):
        for _ in range(15):
            print("Ждем код с OnlineSim")
            try:
                return self.sim.wait_code(tzid, 1)
            except Exception as error:
                LOGGER.error(error)
                continue
        return False

    def state(self, tzid):
        return self.sim.stateOne(tzid)

    def tariffs1(self, ):
        return self.sim.tariffs()


if __name__ == '__main__':
    try:
        service = config['online_sim']['service']
        country = config['online_sim']['country']
        sim = OnlineSim()
        tzid = sim.get_number(service, country)
        print(sim.state(tzid).get('number'))
        while True:
            try:
                number_state = sim.state(tzid)
                print(number_state.get('msg', 'No msg yet'))
                sleep(2)
            except RequestException as error:
                LOGGER.warning(error)
                sleep(15)
    except Exception as error:
        LOGGER.exception(error)
        breakpoint()
