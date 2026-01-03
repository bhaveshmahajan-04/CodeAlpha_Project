import tkinter as tk
from tkinter import messagebox
import csv

STOCK_PRICES = {
 
      # 🇺🇸 US TECHNOLOGY
    "AAPL": 180,      # Apple
    "MSFT": 320,      # Microsoft
    "GOOG": 140,      # Alphabet
    "AMZN": 130,      # Amazon
    "META": 350,      # Meta
    "TSLA": 250,      # Tesla
    "NVDA": 480,      # NVIDIA
    "INTC": 45,       # Intel
    "IBM": 165,       # IBM
    "ORCL": 120,      # Oracle
    "ADBE": 520,      # Adobe
    "CRM": 260,       # Salesforce

    # 🇺🇸 US FINANCE & OTHERS
    "JPM": 155,       # JP Morgan
    "BAC": 35,        # Bank of America
    "WMT": 160,       # Walmart
    "DIS": 95,        # Disney
    "NFLX": 420,      # Netflix
    "KO": 60,         # Coca-Cola
    "PEP": 180,       # Pepsi
    "MCD": 290,       # McDonald's
    "NKE": 110,       # Nike

    # 🇮🇳 INDIAN IT
    "TCS": 3900,
    "INFY": 1550,
    "WIPRO": 480,
    "HCLTECH": 1250,
    "TECHM": 1350,
    "LTIM": 5200,

    # 🇮🇳 INDIAN BANKING
    "HDFCBANK": 1650,
    "ICICIBANK": 1100,
    "SBIN": 650,
    "AXISBANK": 1080,
    "KOTAKBANK": 1750,
    "PNB": 95,
    "BANKBARODA": 230,

    # 🇮🇳 INDIAN INDUSTRY & ENERGY
    "RELIANCE": 2900,
    "ONGC": 240,
    "IOC": 160,
    "BPCL": 480,
    "NTPC": 330,
    "POWERGRID": 300,
    "TATAPOWER": 390,

    # 🇮🇳 AUTOMOBILE
    "TATAMOTORS": 950,
    "MARUTI": 11200,
    "M&M": 1650,
    "BAJAJ-AUTO": 6200,
    "EICHERMOT": 4100,

    # 🇮🇳 FMCG
    "HINDUNILVR": 2600,
    "ITC": 450,
    "NESTLEIND": 24500,
    "DABUR": 560,
    "BRITANNIA": 5200
}

portfolio = []

def add_stock():
    stock = stock_entry.get().upper()
    qty = qty_entry.get()

    if stock not in STOCK_PRICES or not qty.isdigit():
        messagebox.showerror("Error", "Invalid input")
        return

    total = int(qty) * STOCK_PRICES[stock]
    portfolio.append([stock, qty, total])
    listbox.insert(tk.END, f"{stock} | Qty: {qty} | Total: ₹{total}")

def save_file():
    with open("portfolio.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Total"])
        writer.writerows(portfolio)
    messagebox.showinfo("Saved", "Saved to portfolio.csv")

root = tk.Tk()
root.title("Stock Portfolio Tracker")

tk.Label(root, text="Stock Name").pack()
stock_entry = tk.Entry(root)
stock_entry.pack()

tk.Label(root, text="Quantity").pack()
qty_entry = tk.Entry(root)
qty_entry.pack()

tk.Button(root, text="Add Stock", command=add_stock).pack(pady=5)
tk.Button(root, text="Save to CSV", command=save_file).pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack()

root.mainloop()
