import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import random
from string import digits
from validaCpf import valida_cpf

#-----------------------------------------------------
def format_cpf(entry):
    # Remove caracteres não numéricos
    cpf = ''.join(c for c in entry.get() if c.isdigit())

    # Completa com zeros à esquerda se o CPF tiver menos de 11 dígitos
    cpf = cpf.zfill(11)

    # Verifica se o CPF está vazio ou contém apenas zeros
    if not cpf or cpf == '0'*11:
        entry.delete(0, 'end')  # Limpa o conteúdo do widget
    else:
        # Formata o CPF com pontos e traço
        formatted_cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
        entry.delete(0, 'end')  # Limpa o conteúdo do widget
        entry.insert(0, formatted_cpf)  # Insere o CPF formatado no widget

def a_cadaTecla(event):
    # Função chamada a cada tecla pressionada
    allowed_chars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    char = event.char

    if char in allowed_chars or event.keysym in ('BackSpace', 'Delete'):
        # Permite a entrada de dígitos, a tecla Backspace/Delete

        # Remove todos os caracteres não numéricos
        current_text = ''.join(c for c in cpf_entry.get() if c.isdigit())

        # Limita a entrada a no máximo 11 dígitos
        if len(current_text) < 11:
            cpf_entry.delete(0, 'end')
            cpf_entry.insert(0, current_text)
        else:
            if event.keysym in ('BackSpace', 'Delete'):
                return  # Permite a exclusão mesmo após atingir 11 dígitos
            else:
                return "break"  # Impede a entrada de mais dígitos

    else:
        # Ignora todas as outras teclas
        return "break"

def on_enter(event):
    cpf = ''.join(c for c in cpf_entry.get() if c.isdigit())

    # Verifica se o campo de CPF está vazio
    if not cpf:
        # Campo vazio, pode prosseguir para o próximo passo
        print('Próximo passo (sem CPF)')
        ativar_entrada_hora()

    try:
        if valida_cpf(cpf):
            format_cpf(cpf_entry)
            print('Próximo passo')
            ativar_entrada_hora()
        else:
            exibir_erro('CPF inválido')
    except ValueError as e:
        exibir_erro(str(e))

def ativar_entrada_hora():
    # Coloque aqui a lógica para ativar a entrada de horas
    # Configurar o foco para a caixa de lista de horários
    optionmenu_de_horas.focus()

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

        self.iconbitmap("imagens/Image_Icon_marca.ico")


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
    if todos_campos_preenchidos() == True:
        if funcao_ESCOLHER_AREA_DE_TRABALHO != "Função ex.: Vendas":
            cadastrar_funcionario()
        return "break"
    print('option menu função Area De Trabalho vazia')
    return "break"


def todos_campos_preenchidos():
    nome_value = nome_entry.get()
    funcao_value = funcao_ESCOLHER_AREA_DE_TRABALHO.get()

    print("Valor do Nome:", repr(nome_value))
    print("Valor da Área de Trabalho:", repr(funcao_value))

    # Verifica se todos os campos obrigatórios estão preenchidos
    return bool(nome_value.strip() and funcao_value.strip() != "Função ex.: Vendas")



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
cpf_entry.bind('<Key>', a_cadaTecla)
cpf_entry.bind('<Return>', on_enter)
cpf_entry.bind("<Tab>", on_enter)


# Botão cadastro
ctk.CTkButton(quadro, text="Cadastrar",command=cadastrar_funcionario).place(x=25, y=395)


# Botão Fechar  
ctk.CTkButton(quadro,fg_color="#D4D4D4" ,text="cancelar",text_color=("#4E4E4E"),hover_color=("#B3B3B3"), command=janela.destroy).place(x=185, y=395)

#____________________________________________________________________________________________________

janela.mainloop()  
