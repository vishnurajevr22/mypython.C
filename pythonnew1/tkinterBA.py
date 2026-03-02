from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


accounts = {}


def create_account():
    name = ent1.get()
    amount = ent2.get()
    if name in accounts:
        messagebox.showerror("error", "account already exixts")
    else:
        accounts[name] = int(amount)
        messagebox.showinfo("succesfully", f"account created for {name}")


def deposit():
    name = ent1.get()
    amount = ent2.get()
    if name not in accounts:
        messagebox.showerror("error", "account does not exixst")
    else:
        try:
            accounts[name] += int(amount)
            messagebox.showinfo("success", f"${amount} deposited to {name}")
        except ValueError:
            messagebox.showerror("error", "account does not exists!")


def withdraw():
    name = ent1.get()
    amount = ent2.get()
    if name not in accounts:
        messagebox.showerror("error", "account does not exixst")
    else:
        try:
            amt = amount
            if accounts[name] >= int(amt):
                accounts[name] -= int(amt)
                messagebox.showinfo("success", f"${amt} withdraw from {name}")
            else:
                messagebox.showerror("error", "insufficient balance")

        except ValueError:
            messagebox.showerror("error", "account does not exists!")


def checkbalance():
    name = ent1.get()
    if name not in accounts:
        messagebox.showerror("error", "account does not exixts")
    else:
        balance = accounts[name]
        messagebox.showerror("balance", f"{name}'s balance ${balance}")


def history():
    name = ent1.get()
    amt = ent2.get()
    if name not in accounts:
        messagebox.showerror("error", "account does not exixts")
    else:
        print(f"{name}you have acoount hisory last balance is{amt}")


def credit():
    name = ent1.get()
    amt = ent2.get()
    if name not in accounts:
        messagebox.showerror("error", "account does not exixts")
    else:
        print(f"{name} you are eligible for credit card")


def debit():
    name = ent1.get()
    amt = ent2.get()
    if name not in accounts:
        messagebox.showerror("error", "account does not exixts")
    else:
        print(f" debit card has successfully applied for {name} ")


root = Tk()
root.title("Bank application")
root.geometry("800x700")

img_open = Image.open("Screenshot 2026-02-17 165347.png")
bg_img = ImageTk.PhotoImage(img_open)

# Create label and place it at (0,0) to fill the window
bg_label = Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
Label(root, text="ENTER NAME").grid(row=0, column=0)
ent1 = Entry(root)
ent1.grid(row=0, column=1)
Label(root, text="ENTER AMOUNT").grid(row=3, column=0)
ent2 = Entry(root)
ent2.grid(row=3, column=1)
# Button(root, text="submit").grid(row=3, column=1)
Label(root, text="user dashbaord", font=("Times new roman", 22)).grid(row=6, column=0)
Button(root, text="create account", command=create_account).grid(row=8, column=0)
Button(root, text="check balance", command=checkbalance).grid(row=8, column=1)
Button(root, text="depost", command=deposit).grid(row=10, column=0)
Button(root, text="withdraw", command=withdraw).grid(row=10, column=1)
Button(root, text="history", command=history).grid(row=12, column=0)
Button(root, text="credit card", command=credit).grid(row=12, column=1)
Button(root, text="debit card", command=debit).grid(row=14, column=0)
Button(root, text="settings").grid(row=14, column=1)


root.mainloop()
