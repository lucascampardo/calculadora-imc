from tkinter import *
from tkinter import ttk

# Cores
cor0 = '#ffffff' # branco / white
cor1 = '#444466' # preto / black
cor2 = '#4065a1' # azul / blue

# Config
janela = Tk()
janela.title('Calculadora de IMC')
janela.geometry('295x220')
janela.configure(bg=cor0)

# Fazendo a divisão da janela em duas partes
frame_superior = Frame(janela, width=295, height=40, bg=cor2, pady=0, padx=0, relief='flat')
frame_superior.grid(row=0, column=0, sticky=NSEW)

frame_inferior = Frame(janela, width=295, height=180, bg=cor0, pady=0, padx=0, relief='flat')
frame_inferior.grid(row=1, column=0, sticky=NSEW)

# Configurando frame superior
app_name = Label(frame_superior, text='Calculadora de IMC', width=19, height=1, padx=0, relief='flat', anchor='center', font=('Verdana 16 bold'), bg=cor0, fg=cor1)
app_name.place(x=0, y=0)

app_linha = Label(frame_superior, width=400, height=1, padx=0, relief='flat', anchor='center', font=('Verdana 1'), bg=cor1, fg=cor1)
app_linha.place(x=0, y=-25)

# Configurando frame inferior
label_peso = Label(frame_inferior, text='Digite seu peso:', height=1, padx=0, relief='flat', anchor='center', font=('Verdana 10 bold'), bg=cor0, fg=cor2)
label_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=1)
entry_peso = Entry(frame_inferior, width=5 , relief='solid', font=('Verdana 10'), justify='center')
entry_peso.grid(row=0, column=1, pady=10, padx=3)


label_altura = Label(frame_inferior, text='Digite seu peso atual:', height=1, padx=0, relief='flat', anchor='center', font=('Verdana 10 bold'), bg=cor0, fg=cor2)
label_altura.grid(row=1, column=0, sticky=NSEW, pady=10, 
padx=1)
entry_altura = Entry(frame_inferior, text='Digite sua altura:', width=5 ,relief='solid', font=('Verdana 10'), justify='center')
entry_altura.grid(row=1, column=1, pady=10, padx=3)


label_resultado = Label(frame_inferior, text='---', width=5,height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Verdana 14 bold'), bg=cor2, fg=cor0)
label_resultado.place(x=212, y=15)


label_resultado_txt = Label(frame_inferior, text='Seu IMC é: Abaixo do Peso', width=35, height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Verdana 10 bold'), bg=cor0, fg=cor1)
label_resultado_txt.place(x=0, y=85) 

janela.mainloop()