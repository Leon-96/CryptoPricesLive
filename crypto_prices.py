from tkinter import *
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from pycoingecko import CoinGeckoAPI
from timeit import default_timer as timer
from datetime import timedelta
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

# ===================================================USER INTERFACE====================================================

root = Tk()
root.title("Crypto Prices Live")
root['bg'] = 'wheat'
root.minsize(800, 800)
root.resizable(width=False, height=False)

windowicon = PhotoImage(file="C:\\Users\\GoodBoy69\\Downloads\\icon.png")
root.iconphoto(False, windowicon)

filename1 = PhotoImage(file="C:\\Users\\GoodBoy69\\Pictures\\pattern.gif")
background_label = Label(root, image=filename1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

price = Label(root, text="Crypto   Prices   Live", font=("Edge Of The Galaxy", 40,), bg="aquamarine", fg="black",
              bd=8, anchor='w', relief=RAISED)
price.pack()

price = Label(root, text="Choose Cryptocurrency", font=("cambria", 20, "bold"), bg="salmon", fg="black", bd=8,
              anchor='w', relief=RAISED)
price.place(x=70, y=100)

price = Label(root, text="Choose Currency", font=("cambria", 20, "bold"), bg="salmon", fg="black", bd=8, anchor='w',
              relief=RAISED)
price.place(x=470, y=100)

combostyle = ttk.Style()

combostyle.theme_create('combostyle', parent='alt',
                        settings={'TCombobox':
                                      {'configure':
                                           {'selectbackground': 'purple',
                                            'foreground': "white",
                                            'fieldbackground': 'black',
                                            'background': 'white'}}})

combostyle.theme_use('combostyle')

crypto = ttk.Combobox(root, width=12, font=("Helvetica", 17,))
crypto.place(x=120, y=180)
crypto['values'] = ['Bitcoin', 'Ethereum', 'Ripple', 'Litecoin', 'Dogecoin', 'Cardano', 'Polkadot', 'Chainlink',
                    'Monero', 'Tether', 'Stellar', 'Aave', 'Tron', 'Tezos', 'Cosmos', ]
crypto.current(0)

curr = ttk.Combobox(root, width=12, font=("Helvetica", 17,))
curr.place(x=490, y=180)
curr['values'] = ['INR', 'USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'SEK', 'NZD', 'HKD', 'CNY', 'KRW', 'SGD',
                  'RUB']
curr.current(0)

a = StringVar()
b = StringVar()
c = StringVar()
cg = CoinGeckoAPI()

act_textvar = StringVar()
act_textvar.set("")

raw_dataframe = pd.DataFrame(columns=['CryptoCurrency', 'Currency', 'Price', 'Time'])


# =======================================================FUNCTIONS=====================================================


def get_price(event):
    x = (str(cg.get_price(ids=crypto.get(), vs_currencies=curr.get())).replace("{", "")
         .replace("}", "").replace(":", "").replace("'", ""))
    y = x.replace(" ", "        ")
    z = list(y.split())

    a.set(z[0])
    b.set(z[1])
    if z[1] == "INR" or "inr":
        c.set("")

    c.set("{:,}".format(float(z[2])))

    crypto_name.place(x=100, y=500)
    currency_name.place(x=340, y=500)
    price_label.place(x=530, y=500)


def csv_creation():
    global df
    global raw_dataframe
    global hell

    df = pd.DataFrame(columns=['CryptoCurrency', 'Currency', 'Price', 'Time'])

    df.to_csv("cryptoprice.csv", index=False, sep='\t')
    act_textvar.set("csv file has been created")
    activity_label.place(x=285, y=710)

    x = (str(cg.get_price(ids=crypto.get(), vs_currencies=curr.get())).replace("{", "")
         .replace("}", "").replace(":", "").replace("'", ""))
    y = x.replace(" ", "        ")
    hell = list(y.split())

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    new_dataframe1 = pd.DataFrame([[hell[0], hell[1], int(hell[2]), current_time]],
                                  columns=['CryptoCurrency', 'Currency', 'Price', 'Time'])




def append_to_csv():
    global crypto_csv
    global sched
    global raw_dataframe
    global hell
    activity_label.pack_forget()

    crypto_csv = pd.read_csv("cryptoprice.csv", delim_whitespace=True)

    x = (str(cg.get_price(ids=crypto.get(), vs_currencies=curr.get())).replace("{", "")
         .replace("}", "").replace(":", "").replace("'", ""))
    y = x.replace(" ", "        ")
    hell = list(y.split())

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    new_dataframe = pd.DataFrame([[hell[0], hell[1], "{:,}".format(float(hell[2])), current_time]],
                                 columns=['CryptoCurrency', 'Currency', 'Price', 'Time'])

    crypto_csv = crypto_csv.append(new_dataframe, ignore_index=True)

    crypto_csv.to_csv("cryptoprice.csv", index=False, sep='\t')

    new_dataframe1 = pd.DataFrame([[hell[0], hell[1], int(hell[2]), current_time]],
                                  columns=['CryptoCurrency', 'Currency', 'Price', 'Time'])

    raw_dataframe = raw_dataframe.append(new_dataframe1, ignore_index=True)

    raw_dataframe.to_csv("cryptoraw.csv", index=False)

    print(crypto_csv)
    print("\n")

    act_textvar.set("Appended")

    activity_label.place(x=350, y=710)


def append_to_csv1():
    global crypto_csv
    global sched
    global raw_dataframe
    activity_label.pack_forget()

    crypto_csv = pd.read_csv("cryptoprice.csv", delim_whitespace=True)

    x = (str(cg.get_price(ids=crypto.get(), vs_currencies=curr.get())).replace("{", "")
         .replace("}", "").replace(":", "").replace("'", ""))
    y = x.replace(" ", "        ")
    hell = list(y.split())

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    new_dataframe = pd.DataFrame([[hell[0], hell[1], "{:,}".format(float(hell[2])), current_time]],
                                 columns=['CryptoCurrency', 'Currency', 'Price', 'Time'])

    crypto_csv = crypto_csv.append(new_dataframe, ignore_index=True)

    crypto_csv.to_csv("cryptoprice.csv", index=False, sep='\t')

    print(raw_dataframe)

    new_dataframe1 = pd.DataFrame([[hell[0], hell[1], int(hell[2]), current_time]],
                                  columns=['CryptoCurrency', 'Currency', 'Price', 'Time'])

    raw_dataframe = raw_dataframe.append(new_dataframe1, ignore_index=True)

    raw_dataframe.to_csv("cryptoraw.csv", index=False)

    print("\n")

    act_textvar.set("Appending...")

    activity_label.place(x=350, y=710)


def time_interval_append():
    global sched
    global start
    global delay
    global crypto_csv
    global timelist
    global df

    delay = int(input("Enter the delay time (in seconds) :"))

    if NameError == True:
        csv_creation()


    sched = BackgroundScheduler()
    sched.add_job(append_to_csv1, 'interval', seconds=delay)
    sched.start()
    start = timer()
    print("\n")
    act_textvar.set("Appending...")
    activity_label.place(x=350, y=710)


def stop():
    global sched
    global start
    global delay
    global timelist

    sched.shutdown()
    end = timer()
    act_textvar.set("")

    print("\n")
    print(f"Time Passed : {(timedelta(seconds=end - start))}\n")

    print(
        "==================================================FINISHED==================================================")


def plot_chart():
    global crypto_csv
    global raw_dataframe
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.title("Crypto Prices Graph")
    plt.grid(True)
    plt.ylim()

    plotting_df = pd.read_csv("cryptoraw.csv")

    plt.plot(list(plotting_df['Time']), list(plotting_df['Price']), color='blue',
             linewidth=1.0,
             marker='o')
    plt.show()


# =======================================================BUTTONS=======================================================

price_check = Button(root, text="Check Price", bg="orchid", bd=8, width=20, height=1, relief=RAISED,
                     fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER)
price_check.place(x=275, y=300)

price_check.bind("<Button-1>", get_price)

create_csv = Button(root, text="Create .csv File", bg="orchid", bd=8, width=17, height=3, relief=RAISED,
                    fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER,
                    command=csv_creation)
create_csv.place(x=30, y=600)

append = Button(root, text='''Append New Data
Manually''', bg="orchid", bd=8, width=15, height=3, relief=RAISED,
                fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER, command=append_to_csv)
append.place(x=300, y=600)

time_interval = Button(root, text='''Append Data At
Time Intervals''', bg="orchid", bd=8, width=15, height=3, relief=RAISED,
                       fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER,
                       command=time_interval_append)
time_interval.place(x=550, y=600)

stopbutton = Button(root, text='''Stop''', bg="orchid", bd=8, width=10, height=1, relief=RAISED,
                    fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER, command=stop)
stopbutton.place(x=576, y=710)

plotbutton = Button(root, text='''Plot Chart''', bg="orchid", bd=8, width=10, height=1, relief=RAISED,
                    fg="Black", font=("Unispace", 15, "bold"), anchor="center", justify=CENTER, command=plot_chart)
plotbutton.place(x=65, y=710)

# =======================================================LABELS========================================================

price1 = Label(root, text="CryptoCurrency:", font=("cambria", 15, "bold"), bg="violet", fg="black", bd=8, anchor='w',
               relief=RAISED)
price1.place(x=100, y=450)

price2 = Label(root, text="Currency:", font=("cambria", 15, "bold"), bg="violet", fg="black", bd=8, anchor='w',
               relief=RAISED)
price2.place(x=340, y=450)

price3 = Label(root, text="Price:", font=("cambria", 15, "bold"), bg="violet", fg="black", bd=8, anchor='w',
               relief=RAISED)
price3.place(x=530, y=450)

crypto_name = Label(root, textvariable=a, font=("Exan", 20, "bold"), bg="lightgreen", fg="black", bd=8, anchor='w',
                    relief=RAISED)
crypto_name.pack_forget()

currency_name = Label(root, textvariable=b, font=("Exan", 20, "bold"), bg="lightgreen", fg="black", bd=8, anchor='w',
                      relief=RAISED)
currency_name.pack_forget()

price_label = Label(root, textvariable=c, font=("Exan", 20, "bold"), bg="lightgreen", fg="black", bd=8, anchor='w',
                    relief=RAISED)
price_label.pack_forget()

activity_label = Label(root, textvariable=act_textvar, font=("Book Antiqua", 15, "bold"), bg="black", fg="white", )
activity_label.pack_forget()

mbl = Label(root, text="Made by Shivam (*^▽^*)", font=("Book Antiqua", 15, "bold"), bg="black", fg="white", )
mbl.place(x=280, y=768)

root.mainloop()

# =====================================================================================================================


