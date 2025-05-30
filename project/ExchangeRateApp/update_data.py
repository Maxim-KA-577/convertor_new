from get_historical_cur_rates import get_historical_rates
from datetime import datetime
import time
import json
from api import get_data
START_YEAR = 2015
update_time = '23:52'
current_year = 2025
currency_data = get_data()


def historical_rates_update():
    print('UPDATING_HISTORICAL_DATA')
    global current_year
    current_year = get_historical_rates(START_YEAR, current_year)


def update():
    print('UPDATING_LATEST_DATA...')
    latest_currency_data = get_data()
    with open('serv/latest_rates.json', 'w') as lf:
        json.dump(latest_currency_data, lf)


while True:
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == update_time:
            historical_rates_update()
            update()
            print('update_finished')
            time.sleep(60)
        else:
            time.sleep(1)
