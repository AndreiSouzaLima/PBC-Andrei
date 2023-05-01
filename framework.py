#Escreva um programa Python que crie uma interface gráfica do usuário (Aluno) usando um framework de (aluno), como PyQt ou Tkinter.
import tkinter as tk
def processar_click():
    texto_saida.config(text="Olá, " + entrada_nome.get() + "!")

janela = tk.Tk()
janela.title("Minha janela")

rotulo_nome = tk.Label(janela, text="Digite seu nome:")
rotulo_nome.pack()

entrada_nome = tk.Entry(janela)
entrada_nome.pack()

botao_enviar = tk.Button(janela, text="Enviar", command=processar_click)
botao_enviar.pack()

texto_saida = tk.Label(janela, text="")
texto_saida.pack()

janela.mainloop()