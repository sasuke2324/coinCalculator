#Author: Zachary Miglio
""" this program takes the amount of quarters, dimes, nickels and pennies and
calculates the users total amount of money
"""

import tkinter as tk
from tkinter import messagebox

class QuarterCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Coin Calculator")

        self.create_widgets()

    def create_widgets(self):
        # label 1 Quarter
        self.label = tk.Label(self.master, text="number of quarters:")
        self.label.grid(row=0, column=0, padx=10, pady=5)
        self.entryQuarter = tk.Entry(self.master)
        self.entryQuarter.grid(row=0, column=1, padx=10, pady=5)
        self.entryQuarter.insert(tk.END, "0")  # Default value is 0
        #label 2 Dime
        self.label2 = tk.Label(self.master, text="number of dimes:")
        self.label2.grid(row=1, column=0, padx=10, pady=5)
        # entry 2: Dime
        self.entryDime = tk.Entry(self.master)
        self.entryDime.grid(row=1, column=1, padx=10, pady=5)
        self.entryDime.insert(tk.END, "0")

        # label 3 nickels
        self.label3 = tk.Label(self.master,text="number of nickels: ")
        self.label3.grid(row=2, column=0, padx=10, pady=5)


        # entry 3 nickel
        self.entryNickel = tk.Entry(self.master)
        self.entryNickel.grid(row=2, column=1, padx = 10, pady=5)
        self.entryNickel.insert(tk.END, "0")

        # label pennies
        self.label4 = tk.Label(self.master, text="number of pennies")
        self.label4.grid(row=3, column=0, padx = 10, pady=5)

        #entry 4 pennies
        self.entryPennies = tk.Entry(self.master)
        self.entryPennies.grid(row=3, column=1, padx=10, pady=5)
        self.entryPennies.insert(tk.END, "0")


        calculate_button = tk.Button(self.master, text="Calculate", command=self.calculate_dollars)
        calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.grid(row=5, column=0, columnspan=2)

    def calculate_dollars(self):
        # try statement for error handling 
        try:
            # the getters
            quarters = int(self.entryQuarter.get())
            Dimes = int(self.entryDime.get())
            Nickels = int(self.entryNickel.get())
            Pennies = int(self.entryPennies.get())
            list = [quarters, Nickels, Dimes, Pennies]
            for x in range(len(list)):
                if list[x] < 0:
                    raise ValueError("Negative value not allowed")
            #calculates the total of each coin
            totalquarters = quarters * 0.25
            totalDimes = Dimes * 0.10
            totalNickels = Nickels * 0.05
            totalPennies = Pennies * 0.01
            dollars = totalquarters + totalDimes + totalNickels + totalPennies
            self.result_label.config(text=f"Dollar amount: ${dollars:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input some box left blank")
            self.entryQuarter.delete(0, tk.END)
            self.entryQuarter.insert(tk.END, "0")

# main function
def main():
    root = tk.Tk()
    quarter_calculator = QuarterCalculator(root)
    root.mainloop()

# start of program
main()