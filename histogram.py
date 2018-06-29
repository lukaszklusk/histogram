import matplotlib.pyplot as plt
from matplotlib import interactive
import numpy as np
from tkinter import *
interactive(True)

class Okienko(Frame):
    def input_i_t(self,inpt):
        if not inpt:
            self.i = 0
            return
        self.i = int(inpt)

    def input_n_t(self,inpt):
        if not inpt:
            self.n = 1000
            return
        self.n = int(inpt)

    def input_u_t(self,inpt):
        if not inpt:
            self.u = 0
            return
        self.u = float(inpt)

    def input_s_t(self,inpt):
        if not inpt:
            self.s = 1
            return
        self.s = float(inpt)

    def gen_dane(self):
        self.input_n_t(self.input_n.get())
        self.input_u_t(self.input_u.get())
        self.input_s_t(self.input_s.get())
        self.x = np.random.normal(self.u, self.s, self.n)

    def rys_hist(self):
        d = int(round(np.sqrt(self.n)))
        self.input_i_t(self.input_i.get())
        if self.i == 0:
            plt.hist(self.x,d)
        else:
            plt.hist(self.x,self.i)

    def createWidgets(self):
        self.label1 = Label(self)
        self.label1["text"] = "Ilosc przedzialow(dla 0 jest rowna pierwiaskowi z ilosci danych)"
        self.label1.grid(row=1)

        self.label2 = Label(self)
        self.label2["text"] = "Ilosc danych(dane sa generowane na podstawie rozkladu normalnego"
        self.label2.grid(row=4)

        self.label3 = Label(self)
        self.label3["text"] = "Wartosc oczekiwana"
        self.label3.grid(row=5)

        self.label4 = Label(self)
        self.label4["text"] = "Odchylenie standardowe"
        self.label4.grid(row=6)

        self.input_i = Entry(self,bd=5)
        self.input_i["width"] = 6
        self.input_i.grid(row=1,column=1)
        self.input_i.delete(0,END)
        self.input_i.insert(0,"0")

        self.input_n = Entry(self, bd=5)
        self.input_n["width"] = 6
        self.input_n.grid(row=4, column=1)
        self.input_n.delete(0, END)
        self.input_n.insert(0, "1000")

        self.input_u = Entry(self, bd=5)
        self.input_u["width"] = 6
        self.input_u.grid(row=5, column=1)
        self.input_u.delete(0, END)
        self.input_u.insert(0, "0")

        self.input_s = Entry(self, bd=5)
        self.input_s["width"] = 6
        self.input_s.grid(row=6, column=1)
        self.input_s.delete(0, END)
        self.input_s.insert(0, "1")

        self.rysuj = Button(self)
        self.rysuj["text"] = "Rysuj histogram"
        self.rysuj["command"] = self.rys_hist
        self.rysuj.grid(row=2,column=1,rowspan=2)

        self.gen = Button(self)
        self.gen["text"] = "Generuj nowe dane"
        self.gen["command"] = self.gen_dane
        self.gen.grid(row=7,column=1,rowspan=2)

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.x = np.random.normal(0, 1, 1000)
        self.n = 1000
        self.i = 0
        self.u = 0
        self.s = 1
        self.pack()
        self.createWidgets()

root = Tk()
root.title("Histogram")
root.geometry("600x200")
app = Okienko(master=root)
root.mainloop()
i = 4
n = 1000