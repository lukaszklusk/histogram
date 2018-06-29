import matplotlib.pyplot as plt
from matplotlib import interactive
import numpy as np
from tkinter import *
interactive(True)

class Okienko(Frame):
    def gen_dane(self,n=1000,u=0,s=1):
        self.n = n
        self.x = np.random.normal(u, s, n)
    def rys_hist(self,i=0):
        d = int(round(np.sqrt(self.n)))
        if i == 0:
            plt.hist(self.x,d)
        else:
            plt.hist(self.x,i)

    def createWidgets(self):
        self.rysuj = Button(self)
        self.rysuj["text"] = "Rysuj histogram"
        self.rysuj["command"] = self.rys_hist
        self.rysuj.pack({"side":"left"})

        self.gen = Button(self)
        self.gen["text"] = "Generuj nowe dane"
        self.gen["command"] = self.gen_dane
        self.gen.pack({"side":"left"})

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.x = np.random.normal(0, 1, 1000)
        self.n = 1000
        self.pack()
        self.createWidgets()

root = Tk()
root.title("Histogram")
root.geometry("600x400")
app = Okienko(master=root)
root.mainloop()
i = 4
n = 1000
plt.show()