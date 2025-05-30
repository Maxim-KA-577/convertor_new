from tkinter import *
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import requests
import json

def validate_input(char):
    return char.isdigit()


def converting(money_1, currency_1, result):
    money = money_1.get()
    currency = currency_1.get()
    
    if currency == "USD":
        with open("ExchangeRateApp\\serv\\latest_rates.json", "r") as file:
            test = eval(file.read())

        cost = test['data']
        cost = cost['usd']
        cost = round(1/cost, 2)
        answer = float(money)/cost
        answer = round(answer, 2)

        resp = requests.get('http://127.0.0.1:5000/usd')
        resp = resp.json()
        resp = json.loads(resp)

        lst = resp['data']
        lst2 = []
        for i in lst:
            lst2.append(float(1/i))

        lst1 = resp['dates']

        txt = "у вас получилось: " + str(answer) + " долларов"
        result.config(text=txt)

        result.place(x = 150, y = 200)
        plt.plot(lst1, lst2)
        plt.show()

    elif currency == "EUR":
        with open("ExchangeRateApp\\serv\\latest_rates.json", "r") as file:
            test = eval(file.read())

        cost = test['data']
        cost = cost['eur']
        cost = round(1/cost, 2)

        answer = float(money)/cost
        answer = round(answer, 2)

        resp = requests.get('http://127.0.0.1:5000/eur')
        resp = resp.json()
        resp = json.loads(resp)

        lst = resp['data']
        lst2 = []
        for i in lst:
            lst2.append(float(1/i))

        lst1 = resp['dates']

        txt = "у вас получилось: " + str(answer) + " евро"
        result.config(text=txt)

        result.place(x = 150, y = 200)
        plt.plot(lst1, lst2)
        plt.show()

    elif currency == "KZT":
        with open("ExchangeRateApp\\serv\\latest_rates.json", "r") as file:
            test = eval(file.read())

        cost = test['data']
        cost = cost['kzt']
        cost = round(1/cost, 2)

        answer =float(money)/cost
        answer = round(answer, 2)

        resp = requests.get('http://127.0.0.1:5000/kzt')
        resp = resp.json()
        resp = json.loads(resp)

        lst = resp['data']
        lst2 = []
        for i in lst:
            lst2.append(float(1/i))

        lst1 = resp['dates']

        txt = "у вас получилось: " + str(answer) + " тенге"
        result.config(text=txt)

        result.place(x = 150, y = 200)
        plt.plot(lst1, lst2)
        plt.show()

    elif currency == "CNY":
        with open("ExchangeRateApp\\serv\\latest_rates.json", "r") as file:
            test = eval(file.read())

        cost = test['data']
        cost = cost['cny']
        cost = round(1/cost, 2)

        answer = float(money)/cost
        answer = round(answer, 2)

        resp = requests.get('http://127.0.0.1:5000/cny')
        resp = resp.json()
        resp = json.loads(resp)

        lst = resp['data']
        lst2 = []
        for i in lst:
            lst2.append(float(1/i))

        lst1 = resp['dates']

        txt = "у вас получилось: " + str(answer) + " юаней"
        result.config(text=txt)

        result.place(x = 150, y = 200)
        plt.plot(lst1, lst2)
        plt.show()

    
window = Tk()
window.title("Конвертор валют")
window.minsize(500,500)
window.maxsize(500,500)

canvas = Canvas(bg = "lightblue", width = 500, height = 500)
canvas.pack()

validate = window.register(validate_input)

money_label = tk.Label(window, text = "Введите сумму", font=("Arial", 10))
money_1 = tk.Entry(window, validate = "key", validatecommand = (validate, "%S"))

money_label.place(x = 190, y = 40)
money_1.place(x = 180, y = 70)

currency_label = tk.Label(window, text = "выберети валюту(USD, EUR, KZT или CNY)", font=("Arial", 10))
currency_1 = tk.Entry(window)

currency_label.place(x = 120, y = 100)
currency_1.place(x = 180, y = 130)
result_label = tk.Label(window)
convert = ttk.Button(text = "конвертировать", command = lambda: converting(money_1, currency_1, result_label))

convert.place(x = 195, y = 160)

window.mainloop()
