from tkinter import *
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import requests
import json

def validate_input(char):
    return char.isdigit()


def converting(money_1, currency_1):    
    money = money_1.get()
    currency = currency_1.get()
    
    if currency == "USD":
        with open("ExchangeRateApp\\serv\\latest_rates.json", "r") as file:
            test = eval(file.read())

        cost = test['data']
        cost = cost['usd']
        cost = round(1/cost, 2)

        answer = int(money)//cost
        answer = int(answer)

        resp = requests.get('http://127.0.0.1:5000/eur')
        resp = resp.json()
        resp = json.loads(resp)

        lst = resp['data']
        lst2 = []
        for i in lst:
            lst2.append(int(1/i))

        lst1 = resp['dates']

        plt.plot(lst1, lst2)
        plt.show()

        txt = "у вас получилось: " + str(answer) + " долларов"
        result = tk.Label(window, text = txt, font=("Arial", 10))

        result.place(x = 150, y = 200)
        
    elif currency == "EUR":
        with open("ExchangeRateApp\\serv\\latest_rates.json", "r") as file:
            test = eval(file.read())

        cost = test['data']
        cost = cost['eur']
        cost = round(1/cost, 2)

        answer = int(money)//cost
        answer = int(answer)

        resp = requests.get('http://127.0.0.1:5000/eur')
        resp = resp.json()
        resp = json.loads(resp)

        lst = resp['data']
        lst2 = []
        for i in lst:
            lst2.append(int(1/i))

        lst1 = resp['dates']

        plt.plot(lst1, lst2)
        plt.show()

        txt = "у вас получилось: " + str(answer) + " евро"
        result = tk.Label(window, text = txt, font=("Arial", 10))

        result.place(x = 150, y = 200)

    elif currency == "KZT":
        with open("ExchangeRateApp\\serv\\latest_rates.json", "r") as file:
            test = eval(file.read())

        cost = test['data']
        cost = cost['usd']
        cost = round(1/cost, 2)

        answer = int(money)//cost
        answer = int(answer)

        resp = requests.get('http://127.0.0.1:5000/eur')
        resp = resp.json()
        resp = json.loads(resp)

        lst = resp['data']
        lst2 = []
        for i in lst:
            lst2.append(int(1/i))

        lst1 = resp['dates']

        plt.plot(lst1, lst2)
        plt.show()

        txt = "у вас получилось: " + str(answer) + " тенге"
        result = tk.Label(window, text = txt, font=("Arial", 10))

        result.place(x = 150, y = 200)

    elif currency == "CNY":
        with open("ExchangeRateApp\\serv\\latest_rates.json", "r") as file:
            test = eval(file.read())

        cost = test['data']
        cost = cost['usd']
        cost = round(1/cost, 2)

        answer = int(money)//cost
        answer = int(answer)

        resp = requests.get('http://127.0.0.1:5000/eur')
        resp = resp.json()
        resp = json.loads(resp)

        lst = resp['data']
        lst2 = []
        for i in lst:
            lst2.append(int(1/i))

        lst1 = resp['dates']

        plt.plot(lst1, lst2)
        plt.show()

        txt = "у вас получилось: " + str(answer) + " юаней"
        result = tk.Label(window, text = txt, font=("Arial", 10))

        result.place(x = 150, y = 200)

    
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

convert = ttk.Button(text = "конвертировать", command = lambda: converting(money_1, currency_1))

convert.place(x = 195, y = 160)
