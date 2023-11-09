import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import random
from string import digits
#-----------------------------------------------------


def cadastrar_funcionario():
    # obtém os valores inseridos nos campos
    global cargo_ger_ou_super_ou_Freela
    nome = nome_entry.get()
    funcao = funcao_ESCOLHER_AREA_DE_TRABALHO.get()
    nascimento = nascimento_entry.get()
    data_admissao = data_admissao_entry.get()
    cargo = cargo_ger_ou_super_ou_Freela
    cpf = cpf_entry.get()
    entrada = horario_var.get()

    # verifica se os campos obrigatórios foram preenchidos
    if not nome:
            exibir_erro("Preencha os campos obrigatórios.")
            return
    elif funcao == "Função ex.: Vendas":
            messagebox.showinfo("Importante", "Defina Função do Funcionário.")
            return
    elif entrada == "00:00":
            messagebox.showinfo("Importante","Defina o Horário de entrada do Funcionário.")
            return
            

    # lê a planilha existente
    '''df = pd.read_excel("banco_de_dados.xlsx")

    # gera o ID único
    id_unico = gerar_id_unico(df)

    # exibe uma janela pop-up com o número de ID gerado
    exibir_id_unico(id_unico)


    # cria um novo DataFrame com os dados a serem adicionados
    novo_funcionario = pd.DataFrame(
        {
            "ID": [id_unico],
            "Nome": [nome],
            "Função": [funcao],
            "Nascimento": [nascimento],
            "Data de Admissão": [data_admissao],
            "Cargo/Hierarquia": [cargo],
            "CPF": [cpf],
            "Entrada": [entrada],
        }
    )'''

    # concatena o novo funcionário com o DataFrame existente
    '''df = pd.concat([df, novo_funcionario], ignore_index=True)

    # salva o DataFrame atualizado na planilha
    df.to_excel("banco_de_dados.xlsx", index=False)'''

    # limpa os campos após o cadastro
    nome_entry.delete(0, END)
    funcao_ESCOLHER_AREA_DE_TRABALHO.set("Função ex.: Vendas")
    nascimento_entry.delete(0, END)
    data_admissao_entry.delete(0, END)
    radio_ESCOLHER_CARGO.set(0)
    cpf_entry.delete(0, END)
    horario_var.set("00:00")
    

    # move o foco para o próximo campo
    nome_entry.focus()


class Extrajanela(Toplevel):
    def __init__(self, id_unico):
        super().__init__()

        self.geometry("500x250")
        self.title("ID Funcionário")
        self.configure(background="#f2f2f2")  # Definindo cor de fundo

        self.iconbitmap("imagens/Image_Icon_marca.ico")  #Icone


        # Estilo para os rótulos
        label_style = {
            "bg": "#f2f2f2",
            "fg": "#333333",
            "pady": 10
        }

        # Rótulo "Anote o ID!"
        label_anote_id = Label(self, text="Cadastrado Finalizado com susseco!\nAnote este ID, porque ele será usado pelo\n funcionário para cadastrar seu ponto!", **label_style, width=100, font=("Arial", 15))
        label_anote_id.pack()

        # Rótulo para exibir o ID
        label_id = Label(self, text=str(id_unico),**label_style, font=("Impact", 20))
        label_id.pack()

        # Botão "Ok. Já Anotado"
        button_ok = ctk.CTkButton(self, text="Ok. Já Anotado", command=self.destroy)
        button_ok.pack(pady=20)

#_____________________________________________________________________________________________________________
def formatar_cpf(event):
    
    def numerar_cpf():
        for a in cpf_digitado:
            a = int(a)
            cpf_numerado.append(a)
        return 

    def quantidade():
        if len(cpf_digitado) < 11 or len(cpf_digitado) > 11:
            return False
        else:
            return True
    '''def primeiro_digito():
        if len(cpf_numerado) < 11 or len(cpf_numerado) > 11:
            return False
        else:
            acumulador = 0
            resultado = 0
            controlador = 10
            for numeros in cpf_numerado[0:9]:
                resultado = numeros * controlador
                acumulador += resultado
                controlador = controlador - 1
            acumulador = acumulador * 10 % 11
            if acumulador == 10:
                acumulador = 0
            if acumulador == cpf_numerado[9]:
                return True
            else:
                return False
    def segundo_digito():
        if len(cpf_numerado) < 11 or len(cpf_numerado) > 11:
            return False
        else:
            acumulador2 = 0
            resultado2 = 0
            controlador2 = 11
            for numeros2 in cpf_numerado[0:10]:
                resultado2 = numeros2 * controlador2
                acumulador2 += resultado2
                controlador2 = controlador2 - 1
            acumulador2 = acumulador2 * 10 % 11
            if acumulador2 == 10:
                acumulador2 = 0
            if acumulador2 == cpf_numerado[10]:
                return False
            else:
                return True'''


    cpf_digitado = cpf_entry.get()
    cpf_numerado = []
    cpf_digitado = cpf_digitado.replace('.', '').replace('-','')
    
    numerar_cpf()
    quantidade()
    primeiro_digito()
    segundo_digito()
   
    if quantidade() == True and primeiro_digito() == True and segundo_digito() == True:
        proximo_campo(event)
    elif cpf_digitado == "":
        proximo_campo(event)
    else:
        exibir_erro("CPF Inválido.")
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Função para atualizar a cor do rótulo (ESTÁ USANDO: RADIO)
def obter_estilo():
    # Verificar o sistema operacional atual
    system = ctk.get_appearance_mode()

    # Definir o modo com base no sistema operacional
    if system == 'Light':
        modo_atual = "light"  # Definir como "light" se for Windows
    else:
        modo_atual = "dark"  # Definir como "dark" para outros sistemas operacionais

    # Definir os dicionários de estilo para os modos "light" e "dark"
    estilo_light = {"text_color": "#585858"}
    estilo_dark = {"text_color": "#7C7373"}
    estilo_light_opmenu = {"fg_color":"#E1E1E1","button_color":"#E1E1E1", "button_hover_color":"#D0D0D0","text_color":"#585858"}
    estilo_dark_opmenu = {"fg_color":"#555555","button_color":"#555555", "button_hover_color":"#D0D0D0","text_color":"#f2f2f2"}
    # Definir o dicionário de estilo com base no modo atual
    if modo_atual == "light":
        return estilo_light, estilo_light_opmenu
    else:
        return estilo_dark, estilo_dark_opmenu
#------------------------------------------------------
def proximo_campo(event):
    # pula para o próximo campo
    event.widget.tk_focusNext().focus()
    if todos_campos_preenchidos():
        if funcao_ESCOLHER_AREA_DE_TRABALHO != "Função ex.: Vendas":
            cadastrar_funcionario()
        return "break"
    
    return "break"


def todos_campos_preenchidos():
    # verifica se todos os campos obrigatórios estão preenchidos
    return bool(nome_entry.get() and funcao_ESCOLHER_AREA_DE_TRABALHO.get())


def exibir_erro(mensagem):
    messagebox.showerror("Ops", mensagem)
    return


def formatar_data_admissao(event):
    # obtém a data digitada sem as barras
    data_digitada = data_admissao_entry.get()
    data_digitada = data_digitada.replace(" ", "").replace(',','').replace('.', '')
    try:
        # # verifica se a data digitada possui 8 dígitos após remover espaços
        if len(data_digitada) == 8:
            # formata a data para "dd/mm/yyyy"
            data_formatada = datetime.strptime(data_digitada, "%d%m%Y").strftime("%d/%m/%Y")
            data_admissao_entry.delete(0, END)
            data_admissao_entry.insert(0, data_formatada)
            proximo_campo(event)

        elif data_digitada.strip() == "":
            proximo_campo(event)
        else:
            # verifica se a data digitada está no formato "dd/mm/yyyy"
            datetime.strptime(data_digitada, "%d/%m/%Y")
            proximo_campo(event)
    except ValueError:
        # mostra uma mensagem de erro caso a data não esteja no formato correto
        exibir_erro("Formato Data inválido.")


def formatar_data_nasc(event):
    # obtém a data digitada sem as barras
    data_digitada = nascimento_entry.get()
    data_digitada = data_digitada.replace(" ", "").replace(',','').replace('.', '')
    try:
        # # verifica se a data digitada possui 8 dígitos após remover espaços         
        if len(data_digitada) == 8:
                # formata a data para "dd/mm/yyyy"
                data_formatada = datetime.strptime(data_digitada, "%d%m%Y").strftime("%d/%m/%Y")
                nascimento_entry.delete(0, END)
                nascimento_entry.insert(0, data_formatada)
                proximo_campo(event)
        
        elif data_digitada.strip() == "":
            proximo_campo(event)
        else:
            # verifica se a data digitada está no formato "dd/mm/yyyy"
            datetime.strptime(data_digitada, "%d/%m/%Y")
            proximo_campo(event)
    except ValueError:
        # mostra uma mensagem de erro caso a data não esteja no formato correto
        exibir_erro("Formato Data inválido.")

def gerar_id_unico(df):
    # gera um ID único de dois dígitos
    while True:
        id_unico = random.choice(digits[1:]) + random.choice(digits)
        if id_unico not in df['ID'].values:
            return id_unico
          

#*****************************************************
janela = ctk.CTk ()
janela.geometry("700x450")
janela.title("Janela de Cadastro")
janela.resizable(False,False)

img = PhotoImage(file="imagens/cadastro.png")
label_img = ctk.CTkLabel(master=janela, image= img, text="")
label_img.place(x=15, y=80)

quadro = ctk.CTkFrame(master=janela, width=350, height=450)
quadro.pack(side=RIGHT)

#!!!!!Título "Sistema de cadstro!!!!!!!!"
label_Principal_do_quadro_esquerdo = ctk.CTkLabel(master=quadro, text="Sistema de Cadastro", font=("Roboto", 20)). place(x=25, y=5)

# ☐ campo nome do funcio
label_Descritiva_do_entry = ctk.CTkLabel(quadro, text="*Nome").place(x=25, y=40)
nome_entry = ctk.CTkEntry(master=quadro, placeholder_text="*Nome do Funcionário*", width=300, font=("Roboto", 14))
nome_entry.place(x=25, y=60)
nome_entry.focus()
#____________________________________________________________________________________________________
funcao_ESCOLHER_AREA_DE_TRABALHO = ctk.StringVar(value="Função ex.: Vendas")
funcao_setor_opcao_selecianada = ""
def option_Event (funcao_escolhida):
    global funcao_setor_opcao_selecianada
    fc = funcao_ESCOLHER_AREA_DE_TRABALHO.get()
    if fc == "Administrativo":
        funcao_setor_opcao_selecianada = "Administrativo"
    elif fc == "Almoxarifado":
        funcao_setor_opcao_selecianada = "Almoxarifado"
    elif fc == "Operador de Caixa":
        funcao_setor_opcao_selecianada = "Operador de Caixa"
    elif fc == "Vendas":
        funcao_setor_opcao_selecianada = "Vendas"
    elif fc == "Repositor":
        funcao_setor_opcao_selecianada = "Repositor"
    elif fc == "Segurança":
        funcao_setor_opcao_selecianada = "Segurança"
    else:
        funcao_setor_opcao_selecianada = ""
ctk.CTkLabel(quadro, text="*Função").place(x=25, y=90)
optionmenu_de_Funca_Setor = ctk.CTkOptionMenu(quadro,
                values=["Administrativo","Almoxarifado","Operador de Caixa","Vendas","Repositor","Segurança"],command=option_Event,variable=funcao_ESCOLHER_AREA_DE_TRABALHO,width=300, corner_radius=10)
optionmenu_de_Funca_Setor.place(x=25, y=110)




ctk.CTkLabel(quadro, text="Nascimento (opcional)").place(x=25, y=140)
nascimento_entry = ctk.CTkEntry(quadro,width=125, placeholder_text="00/00/0000")
nascimento_entry.place(x=25, y=160)

ctk.CTkLabel(quadro, text="Admissão (opcional)").place(x=200, y=140)
data_admissao_entry = ctk.CTkEntry(quadro, width=125,placeholder_text="00/00/0000")
data_admissao_entry.place(x=200, y=160)

ctk.CTkLabel(quadro, text="Cargo (opicional)").place(x=25, y=195)

radio_ESCOLHER_CARGO = ctk.IntVar(value=0)
cargo_ger_ou_super_ou_Freela = None
def radio_EVENT():
    global cargo_ger_ou_super_ou_Freela  # Indicando que a variável é global

    v = radio_ESCOLHER_CARGO.get()

    if v == 1:
        cargo_ger_ou_super_ou_Freela = "Gerente"
    elif v == 2:
        cargo_ger_ou_super_ou_Freela = "Supervisor"
    elif v == 3:
        cargo_ger_ou_super_ou_Freela = "Freelancer"
    else:
        cargo_ger_ou_super_ou_Freela = "NDA"  # Defina um valor padrão para outros casos

radio1 = ctk.CTkRadioButton(quadro, text="Gerente",command=radio_EVENT, variable=radio_ESCOLHER_CARGO, value=1,fg_color="green",hover_color="#B9ECB9")
radio2 = ctk.CTkRadioButton(quadro, text="Supervisor", command=radio_EVENT, variable=radio_ESCOLHER_CARGO ,value=2,fg_color="green",hover_color="#B9ECB9")
radio3 = ctk.CTkRadioButton(quadro, text="Freelancer",command=radio_EVENT, variable=radio_ESCOLHER_CARGO ,value=3,fg_color="green",hover_color="#B9ECB9")
radio4 = ctk.CTkRadioButton(quadro, text="NDA", command=radio_EVENT, variable=radio_ESCOLHER_CARGO ,value=0,fg_color="green",hover_color="#B9ECB9")

radio1.place(x=25, y=220)
radio2.place(x=200, y=220)
radio3.place(x=25, y=250)
radio4.place(x=200, y=250)    



ctk.CTkLabel(quadro, text="CPF (opcional)").place(x=25, y=275)
cpf_entry = ctk.CTkEntry(quadro, placeholder_text="000.000.000-00", width=300)
cpf_entry.place(x=25, y=295)

horario_var = ctk.StringVar(value="00:00")
hora_entrada = ""
def option_Event (hora_escolhida):
    global hora_entrada
    hr = horario_var.get()
    if hr == "7:00":
        hora_entrada = "7:00"
    elif hr == "9:00":
        hora_entrada = "9:00"
    else:
        hora_entrada = ""
ctk.CTkLabel(quadro, text="Horário de Entrada*").place(x=25, y=325)
optionmenu_de_horas = ctk.CTkOptionMenu(quadro,
                values=["7:00", "9:00"],command=option_Event,variable=horario_var,width=300, corner_radius=10)
optionmenu_de_horas.place(x=25, y=345)


# adiciona os eventos de teclado para pular entre os campos
nome_entry.bind("<Return>", proximo_campo)
nascimento_entry.bind("<Return>", formatar_data_nasc)
data_admissao_entry.bind("<Return>", formatar_data_admissao)
cpf_entry.bind("<Return>", formatar_cpf)

# Botão cadastro
ctk.CTkButton(quadro, text="Cadastrar",command=cadastrar_funcionario).place(x=25, y=395)


# Botão Fechar  
ctk.CTkButton(quadro,fg_color="#D4D4D4" ,text="cancelar",text_color=("#4E4E4E"),hover_color=("#B3B3B3"), command=janela.destroy).place(x=185, y=395)

#____________________________________________________________________________________________________

janela.mainloop()  
