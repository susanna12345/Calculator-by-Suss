from tkinter import *
popoxakan = ""
#------buttons function------
def sxmel(num):
    global popoxakan
    popoxakan = popoxakan + str(num)
    popoxakan2.set(popoxakan)

def func1():
    try:
        global popoxakan
        total = str(eval(popoxakan))
        popoxakan2.set(total)
        popoxakan = ""
    except:
        popoxakan2.set(" error ")
        popoxakan = ""

def maqrel():
    global popoxakan
    popoxakan = ""
    popoxakan2.set("")
#-----Buttons functions-----


#-------Buttons---------
if __name__ == "__main__":

#------Window creating-------
    win = Tk()
    win.configure(background = "white")
    # win.resizable(0,0)
    win.title("Calculator by Suss")
    win.geometry("240x260")
    popoxakan2 = StringVar()
    pp1 = Label(win, textvariable = popoxakan2)
    pp1.grid(columnspan = 4, ipadx = 70)
#--------Window creating-------

    button1 = Button(win, text = ' 1 ', fg = 'cyan', bg = 'gray', command = lambda: sxmel(1), height = 2, width = 3)
    button1.grid(row=2, column=0)
 
    button2 = Button(win, text = ' 2 ', fg = 'cyan', bg = 'gray', command = lambda: sxmel(2), height = 2, width = 3)
    button2.grid(row=2, column=1)

    button3 = Button(win, text = ' 3 ', fg = 'cyan', bg = 'gray', command = lambda: sxmel(3), height = 2, width = 3)
    button3.grid(row=2, column=2)
 
    button4 = Button(win, text = ' 4 ', fg = 'cyan', bg = 'gray', command = lambda: sxmel(4), height = 2, width = 3)
    button4.grid(row=3, column=0)

    button5 = Button(win, text = ' 5 ', fg = 'cyan', bg = 'gray', command = lambda: sxmel(5), height = 2, width = 3)
    button5.grid(row=3, column=1)
 
    button6 = Button(win, text = ' 6 ', fg = 'cyan', bg = 'gray', command = lambda: sxmel(6), height = 2, width = 3)
    button6.grid(row=3, column=2)
 
    button7 = Button(win, text = ' 7 ', fg = 'cyan', bg = 'gray', command = lambda: sxmel(7), height = 2, width = 3)
    button7.grid(row=4, column=0)
 
    button8 = Button(win, text = ' 8 ', fg = 'cyan', bg = 'gray', command = lambda: sxmel(8), height = 2, width = 3)
    button8.grid(row=4, column=1)

    button9 = Button(win, text = ' 9 ', fg = 'cyan', bg = 'gray', command = lambda: sxmel(9), height = 2, width = 3)
    button9.grid(row=4, column=2)
 
    button0 = Button(win, text = ' 0 ', fg = 'cyan', bg = 'gray', command = lambda: sxmel(0), height = 2, width = 3)
    button0.grid(row=5, column=0)
 
    plus = Button(win, text = ' + ', fg = 'cyan', bg = 'gray', command = lambda: sxmel("+"), height = 2, width = 3)
    plus.grid(row=2, column=3)

    minus = Button(win, text = ' - ', fg = 'cyan', bg = 'gray', command = lambda: sxmel("-"), height = 2, width = 3)
    minus.grid(row = 3, column = 3)
 
    bazapatkum = Button(win, text = ' * ', fg = 'cyan', bg = 'gray', command = lambda: sxmel("*"), height = 2, width = 3)
    bazapatkum.grid(row = 4, column = 3)
    
    bajanum = Button(win, text = ' / ', fg = 'cyan', bg = 'gray', command=lambda: sxmel("/"), height = 2, width = 3)
    bajanum.grid(row = 5, column = 3)
 
    havasar = Button(win, text = ' = ', fg = 'cyan', bg = 'gray', command = func1, height = 2, width = 3)
    havasar.grid(row = 5, column = 2)
 
    clear = Button(win, text = 'Clear', fg = 'cyan', bg = 'gray', command = maqrel, height = 2, width = 3)
    clear.grid(row = 5, column = '1')
 
    ket = Button(win, text = '.', fg = 'cyan', bg = 'gray', command = lambda: sxmel('.'), height = 2, width = 3)
    ket.grid(row = 6, column = 0)

win.mainloop()
