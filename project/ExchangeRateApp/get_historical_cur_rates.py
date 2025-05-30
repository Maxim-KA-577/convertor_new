from datetime import datetime
from api import get_data
import json


def get_historical_rates(start_year, server_year):
    curr_year = datetime.today().year
    if server_year < curr_year:
        years_lst = range(start_year, curr_year + 1)
        date_lst = []
        for year in years_lst:
            date_lst.append(str(datetime(year, 1, 1).date()))
        data_cur_lst = []
        for date in date_lst:
            data = get_data(date=date, historical=True)
            if data:
                print(date)
                data_cur_lst.append(data)
            else:
                print(date, 'False')
        print(data_cur_lst)
        write_data(data_cur_lst, years_lst, 'USD')
        write_data(data_cur_lst, years_lst, 'EUR')
        write_data(data_cur_lst, years_lst, 'CNY')
        write_data(data_cur_lst, years_lst, 'KZT')
        return curr_year
    else:
        return server_year


def write_data(data_cur_lst, date_lst, curr_name):
    final_data = []
    if len(data_cur_lst) == date_lst:
        for data in data_cur_lst:
            final_data.append(data['rates'][curr_name])
        json_lists = {'dates': date_lst, 'data': final_data}
        with open(f"serv/historical_{curr_name}.json", "w") as cur_data:
            json.dump(json_lists, cur_data)
    else:
        print('FileWriteError')






