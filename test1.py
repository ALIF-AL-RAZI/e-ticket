
from tkinter import *
from tkinter import ttk

import cv2
import webbrowser

win= Tk()

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

# def page4():
#    for widgets in win.winfo_children():
#       widgets.destroy()
#
#    scan()


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

   b = webbrowser.open(str(a))
   cap.release()
   cv2.destroyAllWindows()




Label(win, text= "Input departure and destination", font= ('Helvetica 17 bold')).pack(pady=30)

Label(win, text= "Departure", font= ('Helvetica 17 bold')).place(x=30, y=150)
Label(win, text= "Destination", font= ('Helvetica 17 bold')).place(x=450, y=150)

code1 =StringVar()
Entry(textvariable=code1, width=15, bd=0, font=("arial", 25)).place(x=30, y=200)

code2 =StringVar()
Entry(textvariable=code2, width=15, bd=0, font=("arial", 25)).place(x=450, y=200)

ttk.Button(win, text="Search", command=page2).place(x=325, y=350)
win.mainloop()