from pycoingecko import CoinGeckoAPI
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import ttk

root= Tk()
root.title("Crypto Prices Live")
root['bg']='wheat'
root.minsize(800,800)
root.resizable(width=False,height=False)

filename1 = PhotoImage(file="C:\\Users\\GoodBoy69\\Pictures\\pattern.gif")
background_label = Label(root, image=filename1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

price = Label(root, text="Crypto    Prices    Live", font=("Edge Of The Galaxy", 40, ), bg="aquamarine", fg="black", bd=8, anchor='w', relief=RAISED)
price.pack()

price = Label(root, text="Choose Cryptocurrency", font=("cambria", 20, "bold"), bg="salmon", fg="black", bd=8, anchor='w', relief=RAISED)
price.place(x=70,y=100)

price = Label(root, text="Choose Currency", font=("cambria", 20, "bold"), bg="salmon", fg="black", bd=8, anchor='w', relief=RAISED)
price.place(x=470,y=100)

combostyle = ttk.Style()

combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'purple',
                                       'fieldbackground': 'white',
                                       'background': 'white'}}} )

combostyle.theme_use('combostyle')


crypto = ttk.Combobox(root, width=12, font=("Helvetica", 17,))
crypto.place(x=120,y=180)
crypto['values'] = ['Bitcoin', 'Ethereum', 'Ripple','Litecoin','Dogecoin','Cardano','Polkadot','Chainlink','Monero']
crypto.current(0)



curr = ttk.Combobox(root, width=12, font=("Helvetica", 17,))
curr.place(x=490,y=180)
curr['values'] = ['INR', 'USD', 'EUR','GBP','JPY','AUD','CAD','CHF','SEK','NZD','HKD','CNY','KRW','SGD','RUB']
curr.current(0)


a=StringVar()
cg=CoinGeckoAPI()

def get_price(event):

    x=(str(cg.get_price(ids=crypto.get(), vs_currencies=curr.get())).replace("{","").replace("}","").replace(":","").replace("'",""))
    y=x.replace(" ","        ")
    a.set(y)

price_check = Button(root, text="Check Price", bg="orchid", bd=8, width=20, height=1, relief=RAISED,
                    fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER)
price_check.place(x=275, y=300)

price_check.bind("<Button-1>",get_price)
root.bind("<Return>",get_price)



price1 = Label(root, text="CryptoCurrency:", font=("cambria", 15, "bold"), bg="violet", fg="black", bd=8, anchor='w', relief=RAISED)
price1.place(x=100,y=450)

price2 = Label(root, text="Currency:", font=("cambria", 15, "bold"), bg="violet", fg="black", bd=8, anchor='w', relief=RAISED)
price2.place(x=340,y=450)

price3 = Label(root, text="Price:", font=("cambria", 15, "bold"), bg="violet", fg="black", bd=8, anchor='w', relief=RAISED)
price3.place(x=530,y=450)


price = Label(root, textvariable=a, font=("Exan", 20, "bold"), bg="lightgreen", fg="black", bd=8, anchor='w', relief=RAISED)
price.place(x=100,y=500)


mbl = Label(root, text="Made by Leon (*^▽^*)", font=("Book Antiqua", 15, "bold"), bg="black", fg="white", )
mbl.place(x=280, y=768)


root.mainloop()