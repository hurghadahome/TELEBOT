import json
import requests
from config import keys

class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):


        if quote == base:
            raise APIException(f'Не возможно перевести одинаковые валюты {base}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обрабатывать валюту {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обрабатывать валюту {quote}.')

        try:
            amount = float(amount)
        except KeyError:
            raise APIException(f'Не удалось обработать количество {amount}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base





