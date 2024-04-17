from tkinter import *
from tkinter import messagebox
from gtts import gTTS
from playsound import playsound
import os

root = Tk()
root.geometry('500x300')
root.title('Text To Audio Converter')

selected_lang = StringVar(root)
selected_lang.set("en")  # Define o valor padrão

# Função para criar o arquivo de áudio e reproduzi-lo
def criar_audio():
    texto = entrada1.get()
    nome_audio = entrada2.get() + '.mp3'
    linguagem = selected_lang.get()

    if texto.strip() == '':
        messagebox.showerror("Erro", "Por favor, insira um texto.")
    else:
        # Verifica se já existe um arquivo de áudio com o mesmo nome e o exclui
        if os.path.exists(nome_audio):
            os.remove(nome_audio)
        
        # Cria o arquivo de áudio
        sp = gTTS(text=texto, lang=linguagem)
        sp.save(nome_audio)
        
        # Para qualquer áudio em reprodução e reproduz o novo áudio
        try:
            playsound.stop()
        except:
            pass
        playsound(nome_audio)

# Função para exibir a mensagem de ajuda com as opções disponíveis
def mostrar_opcoes():
    opcoes = """
    Linguagens disponíveis:
    - Inglês (EUA): en
    - Inglês (Reino Unido): en-uk
    - Francês: fr
    - Alemão: de
    - Italiano: it
    - Espanhol: es
    - Português (Brasil): pt-br
    - Russo: ru
    - Japonês: ja
    - Coreano: ko
    - Chinês (simplificado): zh
    - Chinês (tradicional): zh-tw
    """
    messagebox.showinfo("Opções de Linguagem", opcoes)

entrada1 = Entry(root, fg='green')
entrada1.place(relx=0.1, rely=0.2, relheight=0.1)

texto1 = Label(root, text='Texto')
texto1.place(relx=0.19, rely=0.13)

entrada2 = Entry(root, fg='green')
entrada2.place(relx=0.1, rely=0.43, relheight=0.1)

texto2 = Label(root, text='Nome Do Audio')
texto2.place(relx=0.13, rely=0.36)

opcoes_linguagem = [
    "en", "en-uk", "fr", "de", "it", "es", "pt-br", "ru", "ja", "ko", "zh", "zh-tw"
]

dropdown = OptionMenu(root, selected_lang, *opcoes_linguagem)
dropdown.place(relx=0.1, rely=0.65)

# Botões
btn_help = Button(root, text="Ajuda", command=mostrar_opcoes)
btn_help.place(relx=0.3, rely=0.65)

btn_play = Button(root, text="Reproduzir", command=criar_audio)
btn_play.place(relx=0.4, rely=0.65)

root.mainloop()
