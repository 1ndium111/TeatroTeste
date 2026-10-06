import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import psycopg

DB_CONFIG = {
     "dbname": "cinema",
     "user": "postgres",
     "password": "root",
     "host": "localhost",
     "port": "5432"
}

nome = []
def buscar_assentos_ocupados_sala1():
    status_assentos1 = {}
    
    try:
        conex = psycopg.connect(**DB_CONFIG)
        cur = conex.cursor()
        cur.execute("SELECT fila, numero_cadeira, ocupado FROM assentos_sala1;")
        linhas = cur.fetchall()
        for fila, numero, ocupado in linhas:
            chave = f"{fila}{numero}"
            status_assentos1[chave] = ocupado
            
    except Exception as e:
        print(f"Perdão! Erro ao consultar a database: {e}")
    finally:
        cur.close()
        conex.close()
    return status_assentos1

def buscar_assentos_ocupados_sala2():
    status_assentos2 = {}
    try:
        conex = psycopg.connect(**DB_CONFIG)
        cur = conex.cursor()
        cur.execute("SELECT fila, numero_cadeira, ocupado FROM assentos_sala2;")
        linhas = cur.fetchall()
        for fila, numero, ocupado in linhas:
            chave = f"{fila}{numero}"
            status_assentos2[chave] = ocupado
    except Exception as e:
        print(f"Perdão! Erro ao consultar a database: {e}")
    finally:
        cur.close()
        conex.close()
    return status_assentos2

def buscar_assentos_ocupados_sala3():
    status_assentos3 = {}
    try:
        conex = psycopg.connect(**DB_CONFIG)
        cur = conex.cursor()
        cur.execute("SELECT fila, numero_cadeira, ocupado FROM assentos_sala3;")
        linhas = cur.fetchall()
        for fila, numero, ocupado in linhas:
            chave = f"{fila}{numero}"
            status_assentos3[chave] = ocupado
    except Exception as e:
        print(f"Perdão! Erro ao consultar a database: {e}")
    finally:
        cur.close()
        conex.close()
    return status_assentos3

def alternar_assento(btn):
    global nome
    if btn['bg'] == '#2FA572':
        btn.config(bg='#FF0000', fg="white")
        nome.append(btn['text'])
    else:
        btn.config(bg='#2FA572', fg="white")
        nome.remove(btn['text'])

def reservar(a):
    messagebox.showinfo("Reserva concluída!", f"Os seguintes assentos foram reservados: \n{nome}")

def sumirtudo():
    frame_menu.pack_forget()
    frame_sala1.pack_forget()
    frame_sala2.pack_forget()
    frame_sala3.pack_forget()

def irmenu():
    sumirtudo()
    frame_menu.pack(fill="both", expand=True)

def irsala1():
    sumirtudo()
    frame_sala1.pack(fill="both", expand=True)

def irsala2():
    sumirtudo()
    frame_sala2.pack(fill="both", expand=True)

def irsala3():
    sumirtudo()
    frame_sala3.pack(fill="both", expand=True)

        
FILEIRAS = 10
COLUNAS = 20

app = tk.Tk()
app.title("Gerenciador de Cinema")
app.geometry("1000x600")

assentos_no_banco1 = buscar_assentos_ocupados_sala1()
assentos_no_banco2 = buscar_assentos_ocupados_sala2()
assentos_no_banco3 = buscar_assentos_ocupados_sala3()

frame_menu = tk.Frame(app)
frame_menu.pack(fill="both", expand=True)

titulo_menu = tk.Label(frame_menu, text="Gerenciador de Cinema", font=("Monocraft", 14), fg="#FF0000")
titulo_menu.place(x=395, y=30)

botao1menu = tk.Button(frame_menu, text="Ir para a sala 1", bg="#0CB6A8", fg="#FFFFFF", command=irsala1)
botao1menu.place(x=500, y=100)

botao2menu = tk.Button(frame_menu, text="Ir para a sala 2", bg="#0CB6A8", fg="#FFFFFF", command=irsala2)
botao2menu.place(x=500, y=130)

botao3menu = tk.Button(frame_menu, text="Ir para a sala 3", bg="#0CB6A8", fg="#FFFFFF", command=irsala3)
botao3menu.place(x=500, y=160)

frame_sala1 = tk.Frame(app)

titulo_sala1 = tk.Label(frame_sala1, text="Filme Atual - Minecraft", font=("Monocraft", 14))
titulo_sala1.place(x=395, y=30)

caminhoimagem = "imagens/MINECRAFT.jpg"
imagempil = Image.open(caminhoimagem)
imagemretamanhada = imagempil.resize((100, 133), Image.Resampling.LANCZOS)
imagemtk = ImageTk.PhotoImage(imagemretamanhada)
imagem = tk.Label(frame_sala1, image=imagemtk)
imagem.place(x=450, y=60)

frame_assentos = tk.Frame(frame_sala1)
frame_assentos.place(x = 140, y = 190)

filas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
colunas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for f_idx in range(len(filas)):
    fila = filas[f_idx]
    for c_idx in range(len(colunas)):
        coluna = colunas[c_idx]
        nome_assento1 = f"{fila}{coluna}"
        esta_ocupado1 = assentos_no_banco1.get(nome_assento1)
        if esta_ocupado1:
            cor_fundo = '#FF0000'
            cor_texto = '#FFFFFF'
            estado_botao = "disabled"
        else:
            cor_fundo = '#2FA572'
            cor_texto = '#FFFFFF'
            estado_botao = "normal"
        b1 = tk.Button(frame_assentos, text=nome_assento1 ,font=("Arial", 8, "bold"), bg=cor_fundo, fg=cor_texto, disabledforeground="white", state=estado_botao)
        if estado_botao == "normal":
                    b1.config(command=lambda b=b1: alternar_assento(b))
        b1.grid(row=f_idx + 1, column=c_idx, padx=4, pady=4)


botao1sala1 = tk.Button(frame_sala1, text="Voltar ao menu", bg="#10D0E9", fg="#FFFFFF", command=irmenu)
botao1sala1.place(x=600, y=130)
botaocancelar1 = tk.Button(frame_sala1, text="Cancelar", bg="#E41515", fg="#FFFFFF")
botaocancelar1.place(x=600, y=100)
botaoreservar1 = tk.Button(frame_sala1, text="Reservar", bg="#2A9733", fg="#FFFFFF")
botaoreservar1.place(x=600, y=70)

frame_sala2 = tk.Frame(app)

titulo_sala2 = tk.Label(frame_sala2, text="Filme Atual - Minecraft (Dos Criadores de IASIP)", font=("Monocraft", 14))
titulo_sala2.place(x=305, y=30)

caminhoimagem2 = "imagens/minecraftfiladelfia.jpg"
imagempil2 = Image.open(caminhoimagem2)
imagemretamanhada2 = imagempil2.resize((100, 133), Image.Resampling.LANCZOS)
imagemtk2 = ImageTk.PhotoImage(imagemretamanhada2)
imagem2 = tk.Label(frame_sala2, image=imagemtk2)
imagem2.place(x=450, y=60)

frame_assentos2 = tk.Frame(frame_sala2)
frame_assentos2.place(x = 140, y = 190)

filas2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
colunas2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for f_idx2 in range(len(filas2)):
    fila2 = filas2[f_idx2]
    for c_idx2 in range(len(colunas2)):
        coluna2 = colunas2[c_idx2]
        nome_assento2 = f"{fila2}{coluna2}"
        esta_ocupado2 = assentos_no_banco2.get(nome_assento2)
        if esta_ocupado2:
            cor_fundo = '#FF0000'
            cor_texto = '#FFFFFF'
            estado_botao = "disabled"
        else:
            cor_fundo = '#2FA572'
            cor_texto = '#FFFFFF'
            estado_botao = "normal"
        b2 = tk.Button(frame_assentos2, text=nome_assento2 ,font=("Arial", 8, "bold"), bg=cor_fundo, fg=cor_texto, disabledforeground="white", state=estado_botao)
        if estado_botao == "normal":
            b2.config(command=lambda a=b2: alternar_assento(a))
        b2.grid(row=f_idx2 + 1, column=c_idx2, padx=4, pady=4)

botao1sala2 = tk.Button(frame_sala2, text="Voltar ao menu", bg="#10D0E9", fg="#FFFFFF", command=irmenu)
botao1sala2.place(x=600, y=130)
botaocancelar2 = tk.Button(frame_sala2, text="Cancelar", bg="#E41515", fg="#FFFFFF")
botaocancelar2.place(x=600, y=100)
botaoreservar2 = tk.Button(frame_sala2, text="Reservar", bg="#2A9733", fg="#FFFFFF")
botaoreservar2.place(x=600, y=70)

frame_sala3 = tk.Frame(app)

titulo_sala3 = tk.Label(frame_sala3, text="Filme Atual - Authentic o Filme", font=("Monocraft", 14))
titulo_sala3.place(x=305, y=30)

caminhoimagem3 = "imagens/authentic.jpg"
imagempil3 = Image.open(caminhoimagem3)
imagemretamanhada3 = imagempil3.resize((100, 133), Image.Resampling.LANCZOS)
imagemtk3 = ImageTk.PhotoImage(imagemretamanhada3)
imagem3 = tk.Label(frame_sala3, image=imagemtk3)
imagem3.place(x=450, y=60)

frame_assentos3 = tk.Frame(frame_sala3)
frame_assentos3.place(x = 140, y = 190)

filas3 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
colunas3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for f_idx3 in range(len(filas3)):
    fila3 = filas3[f_idx3]
    for c_idx3 in range(len(colunas3)):
        coluna3 = colunas3[c_idx3]
        nome_assento3 = f"{fila3}{coluna3}"
        esta_ocupado3 = assentos_no_banco3.get(nome_assento3)
        if esta_ocupado3:
            cor_fundo = '#FF0000'
            cor_texto = '#FFFFFF'
            estado_botao = "disabled"
        else:
            cor_fundo = '#2FA572'
            cor_texto = '#FFFFFF'
            estado_botao = "normal"
        b3 = tk.Button(frame_assentos3, text=nome_assento3 ,font=("Arial", 8, "bold"), bg=cor_fundo, fg=cor_texto, disabledforeground="white", state=estado_botao)
        if estado_botao == "normal":
            b3.config(command=lambda c=b3: alternar_assento(c))
        b3.grid(row=f_idx3 + 1, column=c_idx3, padx=4, pady=4)

botao1sala3 = tk.Button(frame_sala3, text="Voltar ao menu", bg="#10D0E9", fg="#FFFFFF", command=irmenu)
botao1sala3.place(x=600, y=130)
botaocancelar3 = tk.Button(frame_sala3, text="Cancelar", bg="#E41515", fg="#FFFFFF")
botaocancelar3.place(x=600, y=100)
botaoreservar3 = tk.Button(frame_sala3, text="Reservar", bg="#2A9733", fg="#FFFFFF")
botaoreservar3.place(x=600, y=70)

app.mainloop()