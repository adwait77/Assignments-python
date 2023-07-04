import tkinter as tk
import webbrowser as wb

obj=tk.Tk()
e=tk.Entry(obj,font=("Comic Sans",50),width=50)
e.grid(row=0,column=0)

def display():
    s=e.get()
    wb.open(f"www.youtube.com/results?search_query={s}")
    print("'",s,"' Navigating to youtube") 

b1=tk.Button(obj,text="Search",font=("Comic Sans",50),bg="cyan",height=1,width=6,command=display)
b1.grid(row=1,column=0)
b=tk.Button(obj,text="Close",font=("Comic Sans",50),bg="pink",height=1,width=6,command=obj.destroy)
b.grid(row=2,column=0)
obj.mainloop()
