from tkinter import*

def limpar():
    display.delete(0, END)

def inserir(valor):
    display.insert(END, valor)

def calcular():
    texto_display = display.get()
    resultado = eval(texto_display)
    limpar()
    display.insert(0, str(resultado))










window = Tk()
window.title("Calculadora")
window.geometry("300x400")

display = Entry(window, font="Arial 20 bold", bg="#ffffff",
                fg="black",width=19)

display.pack()



panel = Frame(window)

panel.pack()

btn_0 = Button(panel, bg='grey', bd=1, text='0',
               font="Arial 16 bold", width=5, height=3,
               command=inserir)

btn_1 = Button(panel, bg='grey', bd=1, text='1',
               font="Arial 16 bold", width=5, height=3,
               command=lambda: inserir(0))

btn_2 = Button(panel, bg='grey', bd=1, text='2',
               font="Arial 16 bold", width=5, height=3,
               command=lambda: inserir(1))

btn_3 = Button(panel, bg='grey', bd=1, text='3',
               font="Arial 16 bold", width=5, height=3,
               command=lambda: inserir(2))

btn_4 = Button(panel, bg='grey', bd=1, text='4',
               font="Arial 16 bold", width=5, height=3
               , command=lambda: inserir(3))

btn_5 = Button(panel, bg='grey', bd=1, text='5',
               font="Arial 16 bold", width=5, height=3,
               command=lambda: inserir(4))

btn_6 = Button(panel, bg='grey', bd=1, text='6',
               font="Arial 16 bold", width=5, height=3,
               command=lambda: inserir(5))

btn_7 = Button(panel, bg='grey', bd=1, text='7',
               font="Arial 16 bold", width=5, height=3,
               command=lambda: inserir(6))

btn_8 = Button(panel, bg='grey', bd=1, text='8',
               font="Arial 16 bold", width=5, height=3,
               command=lambda: inserir(7))

btn_9 = Button(panel, bg='grey', bd=1, text='9',
               font="Arial 16 bold", width=5, height=3,
               command=lambda: inserir(8))

btn_limpar = Button(panel, bg='grey', bd=1, text='CE',
               font="Arial 16 bold", width=5, height=3, command=limpar)

btn_9 = Button(panel, bg='grey', bd=1, text='9',
               font="Arial 16 bold", width=5, height=3)

btn_igual = Button(panel, bg='grey', bd=1, text='=',
               font="Arial 16 bold", width=5, height=3,
                   command=calcular)

btn_sum = Button(panel, bg='grey', bd=1, text='+',
               font="Arial 16 bold", width=5, height=3,
                 command=lambda: inserir('+'))

btn_sub = Button(panel, bg='grey', bd=1, text='-',
               font="Arial 16 bold", width=5, height=3,
                 command=lambda: inserir('-'))

btn_mult = Button(panel, bg='grey', bd=1, text='x',
               font="Arial 16 bold", width=5, height=3,
                  command=lambda: inserir('x'))

btn_div = Button(panel, bg='grey', bd=1, text='÷',
               font="Arial 16 bold", width=5, height=3,
                 command=lambda: inserir('÷'))

btn_7.grid(row= 0, column=0)
btn_8.grid(row= 0, column=1)
btn_9.grid(row= 0, column=2)

btn_div.grid(row=0, column=3)

btn_4.grid(row= 1, column=0)
btn_5.grid(row= 1, column=1)
btn_6.grid(row= 1, column=2)

btn_mult.grid(row= 1, column=3)



btn_1.grid(row=2 , column=0)
btn_2.grid(row=2 , column=1)
btn_3.grid(row= 2, column=2)

btn_sub.grid(row= 2, column=3)

btn_sum.grid(row= 3, column=3)

btn_igual.grid(row= 3, column=2)

btn_limpar.grid(row= 3, column=0)



btn_0.grid(row= 3, column=1)

# btn_7.grid(row= , column=)
# btn_7.grid(row= , column=)
# btn_7.grid(row= , column=)
# btn_7.grid(row= , column=)
# btn_7.grid(row= , column=)








window.mainloop()