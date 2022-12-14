"""
A program that stores info about books

Uses sqlite
"""

from tkinter import *

window=Tk()

l1=Label(window, text="Title")
l1.grid(row=0,column=0)

l2=Label(window, text="Author")
l2.grid(row=0,column=2)

l3=Label(window, text="Year")
l3.grid(row=1,column=0)

l4=Label(window, text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

Author=StringVar()
e1=Entry(window, textvariable=Author)
e1.grid(row=0, column=3)

Year=StringVar()
e1=Entry(window, textvariable=Year)
e1.grid(row=1, column=1)

ISBN1=StringVar()
e1=Entry(window, textvariable=ISBN1)
e1.grid(row=1, column=3)

list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=6)

list1.config(yscrollcommand=sb1.set)
sb1.config(command=list1.yview)

b1=Button(window, text="View all", width=12)
b1.grid(row=2,column=3)

b2=Button(window, text="Search Entry", width=12)
b2.grid(row=3,column=3)

b3=Button(window, text="Add Entry", width=12)
b3.grid(row=4,column=3)

b4=Button(window, text="Update", width=12)
b4.grid(row=5,column=3)

b1=Button(window, text="Delete", width=12)
b1.grid(row=6,column=3
)

b1=Button(window, text="Close", width=12)
b1.grid(row=7,column=3)

window.mainloop()