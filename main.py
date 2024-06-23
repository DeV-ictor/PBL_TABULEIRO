#DECLARAÇÃO

#IMPORT

import customtkinter as ctk
from PIL import Image
import os
import module
import json

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('green')

class CenterApp(ctk.CTkLabel):

    def __init__(self, master):

        set_img = ctk.CTkImage(light_image=Image.open('PBL_TABULEIRO/files/set.png'), dark_image=Image.open('PBL_TABULEIRO/files/set.png'), size=(500,500))
        super().__init__(master, width=500, height=500, corner_radius=0, image=set_img, text='')


class TopFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master, width=1000, height=70, corner_radius=0, fg_color='green', bg_color='transparent')

        #REGRAS INICIO

        rules_button = ctk.CTkButton(self, width=150, height=40, text='Regras', text_color='#fff', font=('Roboto bold', 24), bg_color='transparent', fg_color='darkgreen', corner_radius=20, command='').place(x=750, y=15)

        #REGRAS FIM

class LeftSidedFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master, width=325, height=450, corner_radius=5, fg_color='transparent', bg_color='transparent', border_width=0)

        play_button = ctk.CTkButton(self, width=300, height=70, text='Jogar', fg_color='darkgreen', corner_radius=25, text_color=['#fff', '#fff'], font=('Roboto bold', 48)).place(x=10, y=20)

        load_button = ctk.CTkButton(self, width=300, height=70, text='Carregar', fg_color='darkgreen', corner_radius=25, text_color=['#fff', '#fff'], font=('Roboto bold', 48)).place(x=10, y=120)

        ranking_button = ctk.CTkButton(self, width=300, height=70, text='Ranking', fg_color='darkgreen', corner_radius=25, text_color=['#fff', '#fff'], font=('Roboto bold', 48)).place(x=10, y=220)

        leave_button = ctk.CTkButton(self, width=300, height=70, text='Sair', fg_color='darkgreen', corner_radius=25, text_color=['#fff', '#fff'], font=('Roboto bold', 48)).place(x=10, y=360)


class BottomFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master, width=1005, height=100, fg_color='green', corner_radius=0)

        self.theme_label = ctk.CTkLabel(self, text='Tema', text_color='#fff', bg_color='transparent', font=('Roboto bold', 24)).place(x=48, y=10)
        self.theme_opt = ctk.CTkOptionMenu(self, values=['Sistema', 'Claro', 'Escuro'], font=('Roboto bold', 16), dropdown_font=('Roboto bold', 16), anchor='center', command=self.app_change).place(x=20, y=40)

    def app_change(self, theme):

        if theme == 'Claro':
            ctk.set_appearance_mode('Light')

        elif theme == 'Escuro':
            ctk.set_appearance_mode('Dark')

        elif theme == 'Sistema':
            ctk.set_appearance_mode('System')

class App(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title('Jogo dos Números')
        self.geometry('1000x700')
        self.resizable(width=False, height=False)

        set_img = ctk.CTkImage(light_image=Image.open('PBL_TABULEIRO/files/set.png'), dark_image=Image.open('PBL_TABULEIRO/files/set.png'), size=(350, 650))
        set = ctk.CTkLabel(self, width=500, height=500, corner_radius=0, image=set_img, text='').place(x=450, y=0)

        self.top_frame = TopFrame(self).place(x=0, y=0)
        self.lsframe = LeftSidedFrame(self).place(x=70, y=100)
        self.bottomframe = BottomFrame(self).place(x=0, y=605)
        #self.centerframe = CenterApp(self).place(x=450, y=80)

        #self.buttons()

    def buttons(self):

        play_button = ctk.CTkButton(self, width=300, height=70, text='Jogar', fg_color='darkgreen', bg_color='transparent', border_spacing=3, border_width=2, corner_radius=25, text_color=['#fff', '#fff'], font=('Roboto bold', 48)).place(x=80, y=120)

        load_button = ctk.CTkButton(self, width=300, height=70, text='Carregar', fg_color='darkgreen', bg_color='darkgreen', border_spacing=3, border_width=2, corner_radius=25, text_color=['#fff', '#fff'], font=('Roboto bold', 48)).place(x=80, y=220)

        ranking_button = ctk.CTkButton(self, width=300, height=70, text='Ranking', fg_color='darkgreen', bg_color='darkgreen', border_spacing=3, border_width=2, corner_radius=25, text_color=['#fff', '#fff'], font=('Roboto bold', 48)).place(x=80, y=320)

        leave_button = ctk.CTkButton(self, width=300, height=70, text='Sair', fg_color='darkgreen', bg_color='darkgreen', border_spacing=3, border_width=2, corner_radius=25, text_color=['#fff', '#fff'], font=('Roboto bold', 48)).place(x=80, y=470)



if __name__ == "__main__":
    main = App()
    main.mainloop()