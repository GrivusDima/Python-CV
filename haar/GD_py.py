a = []
dilnyk = 1
okruh = 0
def dodaty(event):
    global a, dilnyk, okruh
    b = text.get("1.0", END).split("\n")
    a += b
    text.delete(1.0, END)
    print(a)

def vyvesty(event):
    r = 0
    dilnyk = float(entry1.get())
    okruh = int(entry2.get())
    for i in a:
        c = 0
        for j in i.split():
            result = round(
                float(j)/dilnyk, okruh)
            print(result)
            label = Label(frame, text=result, bd=0.5, relief="solid")
            label.grid(row=r, column=c)
            c += 1
        r += 1

from tkinter import *
win = Tk()
win.geometry("300x500")
win.resizable(0,0)
win.title("matrica_ultimate>:3")

text = Text(win, width=36, height=5, font="Arial, 11")
text.grid(row=1, column=0, columnspan=2, pady=20, padx=4)

btn1 = Button(win, text = "Dodaty")
btn1.grid(row=2, column=0, pady=20)
btn1.bind("<Button-1>", dodaty)

btn2 = Button(win, text = "Vykonaty")
btn2.grid(row=2, column=1, pady=20)
btn2.bind("<Button-1>", vyvesty)

entry1 = Entry(win, width=36, font="Arial, 11")
entry1.grid(row=3, column=0, columnspan=2, pady=20)
entry2 = Entry(win, width=36, font="Arial, 11")
entry2.grid(row=4, column=0, columnspan=2, pady=20)

frame = Frame(win, bd=0.5, relief="solid")
frame.grid(row=5, column=0, columnspan=2, pady=20)


win.mainloop()