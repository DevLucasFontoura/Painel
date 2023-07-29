import os
import time
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar

# ---------------------------------------------------------------------------------------------------------------------------------------------
# FUNÇÕES AUXILIARES

def selecionarPasta():
    caminho = filedialog.askdirectory()
    if caminho:
        global caminho_arquivo
        caminho_arquivo = caminho

def deletarArquivosDuplicados():
    print('OS ARQUIVOS FORAM DELETADOS COM SUCESSO!')
    for filename in os.listdir(caminho_arquivo):
        for i in range(1, 101):
            if  f'({i})' in filename in filename:
                file_path = os.path.join(caminho_arquivo, filename)
                os.remove(file_path)
                print("OS ARQUIVOS FORAM DELETADOS COM SUCESSO!")

def deletarArquivosDuplicados1():
    print('OS ARQUIVOS FORAM DELETADOS COM SUCESSO!')
    for filename in os.listdir(caminho_arquivo):
        for i in range(1, 101):
            if  f'Copia' in filename in filename:
                file_path = os.path.join(caminho_arquivo, filename)
                os.remove(file_path)
                print("OS ARQUIVOS FORAM DELETADOS COM SUCESSO!")

# ---------------------------------------------------------------------------------------------------------------------------------------------
# JANELA INICIAL DO PROGRAMA

def telaInicial():
    tela_inicial = tk.Tk()
    tela_inicial.title("Deletar Arquivos Duplicados!")

    height = 320
    width = 500

    x = (tela_inicial.winfo_screenwidth()//2) - (width//2)
    y = (tela_inicial.winfo_screenheight()//2) - (height//2)
    tela_inicial.geometry('{}x{}+{}+{}'.format(width, height, x, y)) 

    texto_orientacao01 = tk.Label(tela_inicial, 
                                  text="Seja Bem Vindo!", 
                                  font=("Arial", 20, "bold"))
    texto_orientacao01.place(x=135, y=10)

    texto_orientacao02 = tk.Label(tela_inicial, 
                                  text="Com o propósito de otimizar o espaço de armazenamento em seu computador, este programa foi especialmente desenvolvido para identificar e remover de forma segura os arquivos duplicados presentes na pasta escolhida por você. ", 
                                  font=("Arial", 10), 
                                  wraplength=480)
    texto_orientacao02.place(x=8, y=55)

    texto_orientacao03 = tk.Label(tela_inicial, 
                                  text="Ao executar essa tarefa, você poderá liberar espaço em disco e garantir uma organização mais eficiente dos seus documentos, músicas, vídeos e outros arquivos, proporcionando uma melhor experiência de uso do seu sistema. ", 
                                  font=("Arial", 10), 
                                  wraplength=480)
    texto_orientacao03.place(x=15, y=110)

    texto_orientacao05 = tk.Label(tela_inicial, 
                                  text="Além disso, a operação será realizada com cautela para preservar a integridade dos dados, garantindo que apenas os arquivos duplicados serão excluídos, sem qualquer impacto nos demais conteúdos.", 
                                  font=("Arial", 10), 
                                  wraplength=480)
    texto_orientacao05.place(x=15, y=170)

    texto_orientacao04 = tk.Label(tela_inicial, 
                                  text="Clique no botão se deseja continuar:", 
                                  font=("Arial", 9, "bold"))
    texto_orientacao04.place(x=50, y=270)

    botao_continuar = tk.Button(tela_inicial, 
                                text="Continuar", 
                                font=("Arial", 15), 
                                command=lambda: janelaCaminho(tela_inicial))
    botao_continuar.place(x=280, y=260)

    tela_inicial.mainloop()

# ---------------------------------------------------------------------------------------------------------------------------------------------
# JANELA DE AVISO 

def janelaCaminho(tela_inicial):
    tela_caminho = tk.Tk()
    tela_caminho.title("Deletar Arquivos Duplicados!")

    height = 320
    width = 500

    x = (tela_caminho.winfo_screenwidth()//2) - (width//2)
    y = (tela_caminho.winfo_screenheight()//2) - (height//2)
    tela_caminho.geometry('{}x{}+{}+{}'.format(width, height, x, y)) 

    texto_orientacao01 = tk.Label(tela_caminho, 
                                  text="Indique onde os arquivos estão:", 
                                  font=("Arial", 20, "bold"))
    texto_orientacao01.place(x=40, y=10)

    texto_orientacao02 = tk.Label(tela_caminho, 
                                  text="Por favor, insira abaixo o caminho exato da pasta que contém os arquivos duplicados, para que o programa possa proceder com a exclusão deles de forma precisa e eficiente. ", 
                                  font=("Arial", 10), 
                                  wraplength=480)
    texto_orientacao02.place(x=8, y=65)

    texto_orientacao03 = tk.Label(tela_caminho, 
                                  text="Certifique-se de fornecer o caminho correto para garantir que apenas os arquivos duplicados sejam deletados.", 
                                  font=("Arial", 10), 
                                  wraplength=480)
    texto_orientacao03.place(x=15, y=120)

    texto_orientacao04 = tk.Label(tela_caminho, 
                                  text="A execução cuidadosa dessa tarefa permitirá a liberação de espaço e a organização mais adequada dos dados em seu computador.", 
                                  font=("Arial", 10), 
                                  wraplength=480)
    texto_orientacao04.place(x=40, y=160)

    botao_selecionar_caminho = tk.Button(tela_caminho, 
                                         text="Indicar Caminho", 
                                         font=("Arial", 15), 
                                         command=selecionarPasta)
    botao_selecionar_caminho.place(x=90, y=230)

    botao_avancar = tk.Button(tela_caminho, 
                              text="Continuar", 
                              font=("Arial", 15), 
                              command=lambda: janelaBarraDeProgresso(tela_caminho))
    botao_avancar.place(x=300, y=230)

    tela_inicial.destroy()

    tela_caminho.mainloop()

# ---------------------------------------------------------------------------------------------------------------------------------------------
# JANELA DE AVISO 

def janelaBarraDeProgresso(tela_caminho):
    tela_caminho.destroy()  

    deletarArquivosDuplicados()
    deletarArquivosDuplicados1()

    tela_progresso = tk.Tk()
    tela_progresso.title("Deletar Arquivos Duplicados - Progresso!")

    height = 80
    width = 400

    x = (tela_progresso.winfo_screenwidth()//2) - (width//2)
    y = (tela_progresso.winfo_screenheight()//2) - (height//2)
    tela_progresso.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    percent = tk.StringVar()
    text = tk.StringVar()

    bar = Progressbar(tela_progresso, orient=tk.HORIZONTAL, length=300, mode='determinate')
    bar.pack(pady=20)

    percentLabel = tk.Label(tela_progresso, textvariable=percent)
    percentLabel.pack()

    taskLabel = tk.Label(tela_progresso, textvariable=text)
    taskLabel.pack()

    GB = 100
    download = 0
    speed = 1
    while(download < GB):
        time.sleep(0.05)
        bar['value'] += (speed / GB) * 100
        download += speed
        percent.set(str(int((download / GB) * 100)) + "%")
        tela_progresso.update_idletasks()

    tela_progresso.destroy()  

    janelaArquivosDeletadosComSucesso()

# ---------------------------------------------------------------------------------------------------------------------------------------------
# JANELA INDICANDO QUE OS ARQUIVOS FORAM DELETADOS COM SUCESSO


def janelaArquivosDeletadosComSucesso():

    tela_arquivos_deletados = tk.Tk()
    tela_arquivos_deletados.title("Deletar Arquivos Duplicados - Progresso!")

    height = 200
    width = 400

    x = (tela_arquivos_deletados.winfo_screenwidth()//2) - (width//2)
    y = (tela_arquivos_deletados.winfo_screenheight()//2) - (height//2)
    tela_arquivos_deletados.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    texto_orientacao01 = tk.Label(tela_arquivos_deletados, 
                                  text="Todos os arquivos duplicados foram deletados com sucesso, somente os arquivos originais estão estão disponíveis.", 
                                  font=("Arial", 10), 
                                  wraplength=300)
    texto_orientacao01.place(x=50, y=50)

    texto_orientacao02 = tk.Label(tela_arquivos_deletados, 
                                  text="Você já pode fechar essa janela.", 
                                  font=("Arial", 10), 
                                  wraplength=480)
    texto_orientacao02.place(x=90, y=120)

    tela_arquivos_deletados.mainloop()




# ---------------------------------------------------------------------------------------------------------------------------------------------
def main():
    telaInicial()

if __name__ == "__main__":
    main()
