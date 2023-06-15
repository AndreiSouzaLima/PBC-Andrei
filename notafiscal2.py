from tkinter import *
import os


def imprimir():
    nitens = Label(app, text='PRODUTO', bg='#fff')
    nitens.place(x=15, y=365)
    itens = Label(app, text=nome.get('1.0', END), bg='#fff')
    itens.place(x=15, y=390)

    nquant = Label(app, text='QUANTIDADE', bg='#fff')
    nquant.place(x=85, y=365)
    quant = Label(app, text=qnt.get('1.0', END), bg='#fff')
    quant.place(x=118, y=390)

    np = Label(app, text='PREÇO', bg='#fff')
    np.place(x=175, y=365)
    p = Label(app, text=preco.get('1.0', END), bg='#fff')
    p.place(x=180, y=390)


def gerar():
    janela = Tk()
    janela.title('Nota Fiscal')
    janela.geometry('200x300')

    lista = list()
    lista.append(nome.get('1.0', END))

    #titulo
    Label(janela, text='-'*100).place(x=0, y=10)
    Label(janela, text='CUPOM FISCAL'.center(50)).place(x=0, y=30)
    Label(janela, text='-'*100).place(x=0, y=50)

    #descrição
    Label(janela, text='Descrição').place(x=10, y=70)

    descricao = Label(janela, text=nome.get('1.0', END))
    descricao.place(x=10, y=100)

    #Preço
    Label(janela, text='Preço').place(x=90, y=70)

    valor = Label(janela, text=preco.get('1.0', END))
    valor.place(x=90, y=100)

    #Quantidade
    Label(janela, text='Qtd').place(x=160, y=70)

    quantidade = Label(janela, text=qnt.get('1.0', END))
    quantidade.place(x=164, y=100)

    janela.mainloop()


app = Tk()
app.title('Lista')
app.geometry('330x565')
app.config(bg='#dde')

Label(app, text='Nome do produto', bg='#dde', fg='#000', anchor=W).place(x=10, y=10, width=300, height=20)
nome = Text(app)
nome.place(x=10, y=30, width=300, height=80)

Label(app, text='Quantidade do produto', bg='#dde', fg='#000', anchor=W).place(x=10, y=120, width=300, height=20)
qnt = Text(app)
qnt.place(x=10, y=140, width=300, height=80)

Label(app, text='Preço unitário', bg='#dde', fg='#000', anchor=W).place(x=10, y=230, width=300, height=20)
preco = Text(app)
preco.place(x=10, y=250, width=300, height=80)

Label(app, text='Lista de compras', bg='#dde', fg='#000', anchor=W).place(x=10, y=340, width=300, height=20)
lista = Text(app)
lista.place(x=10, y=360, width=300, height=130)

botao = Button(app, text='Imprimir lista', command=imprimir).place(x=10, y=500, width=100, height=20)

botao2 = Button(app, text='Gerar nota', command=gerar).place(x=10, y=530, width=100, height=20)
app.mainloop()
