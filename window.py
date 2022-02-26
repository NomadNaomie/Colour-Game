import tkinter
import random
import random,math
from tkinter import colorchooser

class Window(tkinter.Frame):
    def __init__(self):
        tkinter.Frame.__init__(self)
        self.master.title('Colour Game Prototype')
        self.master.geometry("600x500+600+0")
        self.squares=[]
        self.after(1000,self.start(self.squares))
        self.mainloop()
    
    def start(self,squares):
        self.level = 1
        square = tkinter.Button(master=self.master,bd=0,height=10,width=15,relief=tkinter.FLAT,bg='red',activebackground='red',command= lambda: self.check(0))
        square.grid(row=0,column=0,padx=5,pady=5)
        self.squares.append([square,None])
        square = tkinter.Button(master=self.master,bd=0,height=10,width=15,relief=tkinter.FLAT,bg='red',activebackground='red',command= lambda: self.check(1))
        square.grid(row=0,column=1,padx=5,pady=5)
        self.squares.append([square,None])
        square = tkinter.Button(master=self.master,bd=0,height=10,width=15,relief=tkinter.FLAT,bg='red',activebackground='red',command= lambda: self.check(2))
        square.grid(row=0,column=2,padx=5,pady=5)
        self.squares.append([square,None])
        square = tkinter.Button(master=self.master,bd=0,height=10,width=15,relief=tkinter.FLAT,bg='red',activebackground='red',command= lambda: self.check(3))
        square.grid(row=1,column=0,padx=5,pady=5)
        self.squares.append([square,None])
        square = tkinter.Button(master=self.master,bd=0,height=10,width=15,relief=tkinter.FLAT,bg='red',activebackground='red',command= lambda: self.check(4))
        square.grid(row=1,column=1,padx=5,pady=5)
        self.squares.append([square,None])
        square = tkinter.Button(master=self.master,bd=0,height=10,width=15,relief=tkinter.FLAT,bg='red',activebackground='red',command= lambda: self.check(5))
        square.grid(row=1,column=2,padx=5,pady=5)
        self.squares.append([square,None])
        square = tkinter.Button(master=self.master,bd=0,height=10,width=15,relief=tkinter.FLAT,bg='red',activebackground='red',command= lambda: self.check(6))
        square.grid(row=2,column=0,padx=5,pady=5)
        self.squares.append([square,None])
        square = tkinter.Button(master=self.master,bd=0,height=10,width=15,relief=tkinter.FLAT,bg='red',activebackground='red',command= lambda: self.check(7))
        square.grid(row=2,column=1,padx=5,pady=5)
        self.squares.append([square,None])
        square = tkinter.Button(master=self.master,bd=0,height=10,width=15,relief=tkinter.FLAT,bg='red',activebackground='red',command= lambda: self.check(8))
        square.grid(row=2,column=2,padx=5,pady=5)
        self.squares.append([square,None])
        self.level_generate(squares,self.level)
        

    def level_generate(self,squares,level):
        level += 1
        real_colour,fake_colour = self.generate()
        randindex = random.randint(0,8)
        self.level_entry = tkinter.Entry(master=self.master,width=10,bg="grey",font=('Helvetica Neue LT',12))
        self.level_entry.grid(row=0,column=5)
        self.level_entry.delete(0,tkinter.END)
        self.level_entry.insert(tkinter.END,str(self.level))
        for i in range(len(squares)):
            if i == randindex:
                squares[i][0].config(bg=fake_colour)
                squares[i][1]=fake_colour
            else:
                squares[i][0].config(bg=real_colour)
                squares[i][1]=real_colour

    
    def generate(self):
        real_colour = [random.randrange(74,181),random.randrange(74,181),random.randrange(74,181)]
        fake_colour = real_colour[:]
        delta_method = random.choice([True,False])
        for colour_channels in range(3):
            if self.level <=10:
                diff = int(30-(1*self.level))
                channel_limit=2
            elif self.level<=20:
                diff = int(22-(.7*self.level))
                channel_limit=2
            elif self.level<=30:
                diff = 34-(self.level)
                channel_limit=3
            else:
                diff = int(math.pow(3,(-0.5*(self.level+3)))+5)
                channel_limit=1
        code = ""
        for channels in range(channel_limit):
            if delta_method:
                fake_colour[channels] = real_colour[channels]-diff
            else:
                fake_colour[channels] = real_colour[channels]+diff
        return self.convert(real_colour),self.convert(fake_colour)

    def check(self,index):
        if self.squares[index][1]!=self.hex_code:
            self.level=1
            self.level_generate(self.squares,self.level)
        else:
            self.level+=1
            self.level_generate(self.squares,self.level)
            

    def convert(self,rgb):
        self.hex_code = ""
        if isinstance(rgb,list) and len(rgb)==3:
            self.hex_code = '#%02x%02x%02x' % tuple(rgb)
        return self.hex_code
    
class Tile():
    def __init__(self,master):
        self.colour ="" 
        self.master = master
    def set_color(self,new_colour):
        if isinstance(new_colour,str):
            if new_colour[0] == "#" and new_colour[1:].isnumeric():
                self.colour = new_colour
        pass
    def get_color(self):
        return self.colour
Window()