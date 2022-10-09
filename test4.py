# from tkinter import *
# from PIL import ImageTk, Image
# from tkinter import filedialog
# import os
#
# root = Tk()
# root.geometry("550x300+300+150")
# root.resizable(width=True, height=True)
#
# def openfn():
#     filename = filedialog.askopenfilename(title='open')
#     return filename
# def open_img():
#     x = openfn()
#     img = Image.open("main.jpeg")
#     img = img.resize((250, 250), Image.ANTIALIAS)
#     img = ImageTk.PhotoImage(img)
#     panel = Label(root, image=img)
#     panel.image = img
#     panel.pack()
#
# btn = Button(root, text='open image', command=open_img).pack()
#
# root.mainloop()


a = '''blah blah blah blah
blah blah blah blah
blah blah blah blah'''
print(a)


link = 'Departure: Mirpur\nDestination: Jamuna\nTicket Staus: Student\nFare: 10\nPayment Status: Confirmed'

print(link)