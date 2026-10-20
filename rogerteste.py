import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 
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

def criar_botoes_sala1():
    # Remove todos os widgets (botões) existentes dentro do frame_assentos para evitar duplicação
    for widget in frame_assentos.winfo_children():
        widget.destroy()
        
    # Busca o status mais atualizado do banco de dados
    global assentos_no_banco1
    assentos_no_banco1 = buscar_assentos_ocupados_sala1()

    filas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    colunas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for f_idx in range(len(filas)):
        fila = filas[f_idx]
        for c_idx in range(len(colunas)):
            coluna = colunas[c_idx]
            nome_assento1 = f"{fila}{coluna}"
            esta_ocupado1 = assentos_no_banco1.get(nome_assento1)
            
            if esta_ocupado1:
                cor_fundo = '#FF0000'  # Vermelho (Ocupado)
            else:
                cor_fundo = '#2FA572'  # Verde (Disponível)
                
            cor_texto = '#FFFFFF'
            
            b1 = tk.Button(frame_assentos, text=nome_assento1, font=("Arial", 8, "bold"), bg=cor_fundo, fg=cor_texto, state="normal")
            b1.config(command=lambda b=b1: alternar_assento(b))
            b1.grid(row=f_idx + 1, column=c_idx, padx=4, pady=4)

def criar_botoes_sala2():
    
    for widget in frame_assentos2.winfo_children():
        widget.destroy()
        
    
    global assentos_no_banco2
    assentos_no_banco2 = buscar_assentos_ocupados_sala2()

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
            else:
                cor_fundo = '#2FA572'  
                
            cor_texto = '#FFFFFF'
            
            b2 = tk.Button(frame_assentos2, text=nome_assento2, font=("Arial", 8, "bold"), bg=cor_fundo, fg=cor_texto, state="normal")
            b2.config(command=lambda b=b2: alternar_assento(b))
            b2.grid(row=f_idx2 + 1, column=c_idx2, padx=4, pady=4)

def criar_botoes_sala3():
    for widget in frame_assentos3.winfo_children():
        widget.destroy()
        
    global assentos_no_banco3
    assentos_no_banco3 = buscar_assentos_ocupados_sala3()

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
            else:
                cor_fundo = '#2FA572'  
                
            cor_texto = '#FFFFFF'
            
            b3 = tk.Button(frame_assentos3, text=nome_assento3, font=("Arial", 8, "bold"), bg=cor_fundo, fg=cor_texto, state="normal")
            b3.config(command=lambda b=b3: alternar_assento(b))
            b3.grid(row=f_idx3 + 1, column=c_idx3, padx=4, pady=4)

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
    assento_texto = btn['text']
    if btn['bg'] != '#2980b9':
        btn.orig_cor = btn['bg']  
        btn.config(bg='#2980b9', fg="white")
        if assento_texto not in nome:
            nome.append(assento_texto)
    else:
        cor_retorno = getattr(btn, 'orig_cor', '#2FA572')
        btn.config(bg=cor_retorno, fg="white")
        if assento_texto in nome:
            nome.remove(assento_texto)

def registrar_historico(cur, sala, acao, fila, coluna):
    cur.execute(
        "INSERT INTO historico (sala, fila, numero_cadeira, acao) VALUES (%s, %s, %s, %s);",
        (sala, fila, coluna, acao)
    )

def reservar1():
    if not nome:
        messagebox.showwarning("Aviso", "Nenhum assento selecionado!")
        return
    
    assentos_para_reservar = [(assento[0], int(assento[1:])) for assento in nome]
    
    try:
        with psycopg.connect(**DB_CONFIG) as conex:
            with conex.cursor() as cur:
                query = "UPDATE assentos_sala1 SET ocupado = true WHERE fila = %s AND numero_cadeira = %s AND ocupado = false;"
                for fila, coluna in assentos_para_reservar:
                    cur.execute(query, (fila, coluna))
                    if cur.rowcount > 0:
                        registrar_historico(cur, 1, "RESERVA", fila, coluna)
                conex.commit()
        
        # ALTERADO: a mensagem agora aparece depois do commit
        messagebox.showinfo("Reserva concluída!", f"Os seguintes assentos foram reservados na sala 1: \n{nome}")
        nome.clear() 
        irsala1()    
    except Exception as error:
        print(f"Perdão! Erro ao reservar assentos na database: {error}")

def reservar2():
    if not nome:
        messagebox.showwarning("Aviso", "Nenhum assento selecionado!")
        return
    
    assentos_para_reservar = [(assento[0], int(assento[1:])) for assento in nome]
    
    try:
        with psycopg.connect(**DB_CONFIG) as conex:
            with conex.cursor() as cur:
                
                query = "UPDATE assentos_sala2 SET ocupado = true WHERE fila = %s AND numero_cadeira = %s AND ocupado = false;"
                for fila, coluna in assentos_para_reservar:
                    cur.execute(query, (fila, coluna))
                    if cur.rowcount > 0:  
                        registrar_historico(cur, 2, "RESERVA", fila, coluna)
                conex.commit()
        
        
        messagebox.showinfo("Reserva concluída!", f"Os seguintes assentos foram reservados na sala 2: \n{nome}")
        nome.clear()
        irsala2() 
    except Exception as error:
        print(f"Perdão! Erro ao reservar assentos na database: {error}")

def reservar3():
    if not nome:
        messagebox.showwarning("Aviso", "Nenhum assento selecionado!")
        return
    
    assentos_para_reservar = [(assento[0], int(assento[1:])) for assento in nome]
    
    try:
        with psycopg.connect(**DB_CONFIG) as conex:
            with conex.cursor() as cur:
                query = "UPDATE assentos_sala3 SET ocupado = true WHERE fila = %s AND numero_cadeira = %s AND ocupado = false;"
                for fila, coluna in assentos_para_reservar:
                    cur.execute(query, (fila, coluna))
                    if cur.rowcount > 0:
                        registrar_historico(cur, 3, "RESERVA", fila, coluna)
                conex.commit()
        
        
        messagebox.showinfo("Reserva concluída!", f"Os seguintes assentos foram reservados na sala 3: \n{nome}")
        nome.clear()
        irsala3() 
    except Exception as error:
        print(f"Perdão! Erro ao reservar assentos na database: {error}")

def cancelar1():
    if not nome:
        messagebox.showwarning("Aviso", "Nenhum assento selecionado para cancelar!")
        return
        
    assentos_para_cancelar = [(assento[0], int(assento[1:])) for assento in nome]
    
    try:
        with psycopg.connect(**DB_CONFIG) as conex:
            with conex.cursor() as cur:
                
                query = "UPDATE assentos_sala1 SET ocupado = false WHERE fila = %s AND numero_cadeira = %s AND ocupado = true;"
                for fila, coluna in assentos_para_cancelar:
                    cur.execute(query, (fila, coluna))
                    if cur.rowcount > 0:  
                        registrar_historico(cur, 1, "CANCELAMENTO", fila, coluna)
                conex.commit()
        
        
        messagebox.showinfo("Cancelamento concluído!", f"Os seguintes assentos foram cancelados na sala 1: \n{nome}")
        nome.clear()
        irsala1() 
        
    except Exception as errorC:
        print(f"Perdão! Erro ao cancelar assentos na database: {errorC}")

def cancelar2():
    if not nome:
        messagebox.showwarning("Aviso", "Nenhum assento selecionado para cancelar!")
        return
        
    assentos_para_cancelar = [(assento[0], int(assento[1:])) for assento in nome]
    
    try:
        with psycopg.connect(**DB_CONFIG) as conex:
            with conex.cursor() as cur:
                
                query = "UPDATE assentos_sala2 SET ocupado = false WHERE fila = %s AND numero_cadeira = %s AND ocupado = true;"
                for fila, coluna in assentos_para_cancelar:
                    cur.execute(query, (fila, coluna))
                    if cur.rowcount > 0:  
                        registrar_historico(cur, 2, "CANCELAMENTO", fila, coluna)
                conex.commit()
        
        
        messagebox.showinfo("Cancelamento concluído!", f"Os seguintes assentos foram cancelados na sala 2: \n{nome}")
        nome.clear()
        irsala2()
        
    except Exception as errorC:
        print(f"Perdão! Erro ao cancelar assentos na database: {errorC}")

def cancelar3():
    if not nome:
        messagebox.showwarning("Aviso", "Nenhum assento selecionado para cancelar!")
        return
        
    assentos_para_cancelar = [(assento[0], int(assento[1:])) for assento in nome]
    
    try:
        with psycopg.connect(**DB_CONFIG) as conex:
            with conex.cursor() as cur:
                query = "UPDATE assentos_sala3 SET ocupado = false WHERE fila = %s AND numero_cadeira = %s AND ocupado = true;"
                for fila, coluna in assentos_para_cancelar:
                    cur.execute(query, (fila, coluna))
                    if cur.rowcount > 0:  
                        registrar_historico(cur, 3, "CANCELAMENTO", fila, coluna)
                conex.commit()
        
        
        messagebox.showinfo("Cancelamento concluído!", f"Os seguintes assentos foram cancelados na sala 3: \n{nome}")
        nome.clear()
        irsala3()
        
    except Exception as errorC:
        print(f"Perdão! Erro ao cancelar assentos na database: {errorC}")


def carregar_historico():
    for item in tabela_historico.get_children():
        tabela_historico.delete(item)
    try:
        with psycopg.connect(**DB_CONFIG) as conex:
            with conex.cursor() as cur:
                cur.execute("""
                    SELECT data_hora, sala, fila, numero_cadeira, acao
                    FROM historico
                    ORDER BY data_hora DESC, id DESC;
                """)
                for data_hora, sala, fila, numero, acao in cur.fetchall():
                    tabela_historico.insert(
                        "", "end",
                        values=(data_hora.strftime("%d/%m/%Y %H:%M:%S"), f"Sala {sala}", f"{fila}{numero}", acao),
                        tags=(acao,)
                    )
    except Exception as e:
        print(f"Perdão! Erro ao consultar o histórico: {e}")
        messagebox.showerror("Erro", "Não foi possível carregar o histórico.")

def sumirtudo():
    frame_menu.pack_forget()
    
    frame_sala1.pack_forget()
    frame_sala2.pack_forget()
    frame_sala3.pack_forget()
    frame_historico.pack_forget() 

def irmenu():
    sumirtudo()
    frame_menu.pack(fill="both", expand=True)

def irsala1():
    sumirtudo()
    global assentos_no_banco1
    criar_botoes_sala1()
    frame_sala1.pack(fill="both", expand=True)

def irsala2():
    sumirtudo()
    global assentos_no_banco2
    criar_botoes_sala2()
    frame_sala2.pack(fill="both", expand=True)

def irsala3():
    sumirtudo()
    global assentos_no_banco3
    criar_botoes_sala3()
    frame_sala3.pack(fill="both", expand=True)

def irhistorico():
    sumirtudo()
    carregar_historico()
    frame_historico.pack(fill="both", expand=True)

        
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

titulo_menu = tk.Label(frame_menu, text="Gerenciador de Cinema", font=("Comic Sans MS", 14), fg="#FF0000")
titulo_menu.place(x=395, y=30)

botao1menu = tk.Button(frame_menu, text="Ir para a sala 1", bg="#1F10E9", fg="#FFFFFF", command=irsala1)
botao1menu.place(x=500, y=100)

botao2menu = tk.Button(frame_menu, text="Ir para a sala 2", bg="#1F10E9", fg="#FFFFFF", command=irsala2)
botao2menu.place(x=500, y=130)

botao3menu = tk.Button(frame_menu, text="Ir para a sala 3", bg="#1F10E9", fg="#FFFFFF", command=irsala3)
botao3menu.place(x=500, y=160)


botaohistoricomenu = tk.Button(frame_menu, text="Ver histórico", bg="#1F10E9", fg="#FFFFFF", command=irhistorico)
botaohistoricomenu.place(x=500, y=190)

frame_sala1 = tk.Frame(app)

titulo_sala1 = tk.Label(frame_sala1, text="Filme Atual - Minecraft", font=("Comic Sans MS", 14))
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

botao1sala1 = tk.Button(frame_sala1, text="Voltar ao menu", bg="#1F10E9", fg="#FFFFFF", command=irmenu)
botao1sala1.place(x=600, y=130)
botaocancelar1 = tk.Button(frame_sala1, text="Cancelar", bg="#E41515", fg="#FFFFFF", command=cancelar1)
botaocancelar1.place(x=600, y=100)
botaoreservar1 = tk.Button(frame_sala1, text="Reservar", bg="#2A9733", fg="#FFFFFF", command=reservar1)
botaoreservar1.place(x=600, y=70)

frame_sala2 = tk.Frame(app)

titulo_sala2 = tk.Label(frame_sala2, text="Filme Atual - Minecraft (Dos Criadores de IASIP)", font=("Comic Sans MS", 14))
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
        else:
            cor_fundo = '#2FA572' 
            
        cor_texto = '#FFFFFF'
        
        b2 = tk.Button(frame_assentos2, text=nome_assento2, font=("Arial", 8, "bold"), bg=cor_fundo, fg=cor_texto, state="normal")
        b2.config(command=lambda a=b2: alternar_assento(a))
        b2.grid(row=f_idx2 + 1, column=c_idx2, padx=4, pady=4)

botao1sala2 = tk.Button(frame_sala2, text="Voltar ao menu", bg="#1F10E9", fg="#FFFFFF", command=irmenu)
botao1sala2.place(x=600, y=130)
botaocancelar2 = tk.Button(frame_sala2, text="Cancelar", bg="#E41515", fg="#FFFFFF", command=cancelar2)
botaocancelar2.place(x=600, y=100)
botaoreservar2 = tk.Button(frame_sala2, text="Reservar", bg="#2A9733", fg="#FFFFFF", command=reservar2)
botaoreservar2.place(x=600, y=70)

frame_sala3 = tk.Frame(app)

titulo_sala3 = tk.Label(frame_sala3, text="Filme Atual - Authentic o Filme", font=("Comic Sans MS", 14))
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
        else:
            cor_fundo = '#2FA572'  
            
        cor_texto = '#FFFFFF'
        
        b3 = tk.Button(frame_assentos3, text=nome_assento3, font=("Arial", 8, "bold"), bg=cor_fundo, fg=cor_texto, state="normal")
        b3.config(command=lambda c=b3: alternar_assento(c))
        b3.grid(row=f_idx3 + 1, column=c_idx3, padx=4, pady=4)

botao1sala3 = tk.Button(frame_sala3, text="Voltar ao menu", bg="#1F10E9", fg="#FFFFFF", command=irmenu)
botao1sala3.place(x=600, y=130)
botaocancelar3 = tk.Button(frame_sala3, text="Cancelar", bg="#E41515", fg="#FFFFFF", command=cancelar3)
botaocancelar3.place(x=600, y=100)
botaoreservar3 = tk.Button(frame_sala3, text="Reservar", bg="#2A9733", fg="#FFFFFF", command=reservar3)
botaoreservar3.place(x=600, y=70)

frame_historico = tk.Frame(app)

titulo_historico = tk.Label(frame_historico, text="Histórico de Reservas e Cancelamentos", font=("Comic Sans MS", 14))
titulo_historico.pack(pady=15)

botao_voltar_historico = tk.Button(frame_historico, text="Voltar ao menu", bg="#1F10E9", fg="#FFFFFF", command=irmenu)
botao_voltar_historico.pack(side="bottom", pady=10)

frame_tabela_historico = tk.Frame(frame_historico)
frame_tabela_historico.pack(fill="both", expand=True, padx=20)

tabela_historico = ttk.Treeview(frame_tabela_historico, columns=("data", "sala", "assento", "acao"), show="headings")
for col, texto, largura in [("data", "Data/Hora", 200), ("sala", "Sala", 100),
                            ("assento", "Assento", 100), ("acao", "Ação", 150)]:
    tabela_historico.heading(col, text=texto)
    tabela_historico.column(col, width=largura, anchor="center")

tabela_historico.tag_configure("RESERVA", foreground="#2FA572")
tabela_historico.tag_configure("CANCELAMENTO", foreground="#FF0000")

scroll_historico = ttk.Scrollbar(frame_tabela_historico, orient="vertical", command=tabela_historico.yview)
tabela_historico.configure(yscrollcommand=scroll_historico.set)

tabela_historico.pack(side="left", fill="both", expand=True)
scroll_historico.pack(side="right", fill="y")

app.mainloop()
