import requests


API_KEY = 'X1lueg49Lv6Rn7gEuS5oT9ufYopH9LY9'


def get_data(date="latest", historical=False):
    if historical:
        link = f'https://api.apilayer.com/exchangerates_data/{date}?symbols=USD,EUR,CNY,KZT&base=RUB&apikey={API_KEY}'

        resp = requests.get(link)
        resp_json = resp.json()
        print(resp_json)
        try:
            data = {'date': resp_json['date'], 'data': resp_json['rates']}
        except KeyError:
            print('KeyError_Historical')
            return False

    else:
        link = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/v1/currencies/rub.json'
        resp = requests.get(link)
        resp_json = resp.json()
        print(resp_json)
        try:
            data = {'date': resp_json['date'], 'data': {'usd': resp_json['rub']['usd'], 'eur': resp_json['rub']['eur'],
                                                        'cny': resp_json['rub']['cny'], 'kzt': resp_json['rub']['kzt']}}
        except KeyError:
            print('KeyError_Latest')
            return False
    print(data)
    return data


if __name__ == '__main__':
    get_data(historical=True)
