from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

from tkinter import messagebox

import cv2

import pyqrcode
import png
from pyqrcode import QRCode

import webbrowser

win = Tk()

win.geometry("750x500")


def page2():
    # win
    # win.geometry("750x250")
    # win.title("New Window")
    for widgets in win.winfo_children():
        widgets.destroy()

    # for lbl in range(6):
    #    Label(win, text="Route details", font=('Helvetica 17 bold')).pack(pady=lbl+30)

    Label(win, text="Route details", font=('Helvetica 17 bold')).pack(pady=30)

    Label(win, text="Bus", font=('Helvetica 17 bold')).place(x=30, y=150)

    Label(win, text="Fare", font=('Helvetica 17 bold')).place(x=30, y=200)

    ttk.Button(win, text="Confirm", command=page3).place(x=325, y=350)


def page3():
    # win
    # win.geometry("750x250")
    # win.title("New Window")
    for widgets in win.winfo_children():
        widgets.destroy()

    ttk.Button(win, text="Back", command=page2).place(x=30, y=30)
    Label(win, text="Find a bus", font=('Helvetica 17 bold')).pack(pady=30)

    ttk.Button(win, text="Scan Qr code of bus", command=scan).place(x=325, y=350)


def page4(a):
    for widgets in win.winfo_children():
        widgets.destroy()

    Label(win, text="Bus: " + a, font=('Helvetica 17 bold')).place(x=30, y=150)

    Label(win, text="Bus Name: ", font=('Helvetica 17 bold')).place(x=30, y=200)

    ttk.Button(win, text="Confirm", command=page5).place(x=325, y=350)

    strng = 'Departure: Mirpur\nDestination: Jamuna\nTicket Staus: Student\nFare: 10\nPayment Status: Confirmed'
    qr = pyqrcode.create(strng)
    qr.png('Ticketqr.png', scale=10)


def page5():

    for widgets in win.winfo_children():
        widgets.destroy()
    global pswrd
    Label(win, text="Your Ticket", font=('Helvetica 17 bold')).pack(pady=30)

    img = Image.open("main.jpeg")
    img = img.resize((200, 200), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel = Label(win, image=img)
    panel.image = img
    panel.pack()

    Label(win, text="Manage Password To Complete Trip", font=('Helvetica 17 bold')).place(x=30, y=350)
    pswrd = StringVar()
    Entry(textvariable=pswrd, width=15, bd=0, font=("arial", 25), show="*").place(x=30, y=400)
    ttk.Button(win, text="Complete Trip", command=con_pass).place(x=325, y=450)


def con_pass():

    password = pswrd.get()

    if password == "1234":
        win.destroy()


    elif password == "":
        messagebox.showerror("", "Input Password")

    elif password != "1234":
        messagebox.showerror("", "Invalid Password")


def scan():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    while True:
        _, img = cap.read()
        data, one, _ = detector.detectAndDecode(img)
        if data:
            a = data
            break

        cv2.imshow('qrcodescanner app', img)
        if cv2.waitKey(1) == ord('q'):
            break

    # b = webbrowser.open(str(a))
    cap.release()
    cv2.destroyAllWindows()
    page4(a)


Label(win, text="Input departure and destination", font=('Helvetica 17 bold')).pack(pady=30)

Label(win, text="Departure", font=('Helvetica 17 bold')).place(x=30, y=150)
Label(win, text="Destination", font=('Helvetica 17 bold')).place(x=450, y=150)

code1 = StringVar()
Entry(textvariable=code1, width=15, bd=0, font=("arial", 25)).place(x=30, y=200)

code2 = StringVar()
Entry(textvariable=code2, width=15, bd=0, font=("arial", 25)).place(x=450, y=200)

ttk.Button(win, text="Search", command=page2).place(x=325, y=350)
win.mainloop()
