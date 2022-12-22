import pandas as pd


class Data:
    _id = '1zaxjdu9ESYy2MCNuDow0_5PnZpwEsyrdTQ_kk0PMZbw'
    _gid = '1315649221'
    _url = (f'https://docs.google.com/spreadsheets/d/{_id}/'
            f'export?format=csv&id={_id}&gid={_gid}')
    index = 0

    def __init__(self):
        self._dataframe = pd.read_csv(self._url)

    def __call__(self, arg):
        value = self._dataframe[arg].dropna()
        return value
