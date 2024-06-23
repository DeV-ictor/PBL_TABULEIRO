#DECLARAÇÃO

#IMPORT

from tkinter import *
import customtkinter as ctk
from PIL import Image
import os
import module
import json

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

class RulesWindow(ctk.CTkToplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry('450x600')
        self.title('Regras')

        self.rule_1 = ctk.CTkLabel(self, text='Regra 1. ').place(x=0, y=0)
        self.rule_1 = ctk.CTkLabel(self, text='Regra 2. ')
        self.rule_1 = ctk.CTkLabel(self, text='Regra 3. ')
        self.rule_1 = ctk.CTkLabel(self, text='Regra 4. ')
        self.rule_1 = ctk.CTkLabel(self, text='Regra 5. ')

class RankingWindow(ctk.CTkToplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry('600x300')
        self.title('Regras')

        self.rule_1 = ctk.CTkLabel(self, text='Regra 1. ').place(x=0, y=0)
        self.rule_1 = ctk.CTkLabel(self, text='Regra 2. ')
        self.rule_1 = ctk.CTkLabel(self, text='Regra 3. ')
        self.rule_1 = ctk.CTkLabel(self, text='Regra 4. ')
        self.rule_1 = ctk.CTkLabel(self, text='Regra 5. ')

class App(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title('Jogos dos Números')
        self.geometry('1000x700')
        self.resizable(width=False, height=False)

        self.topFrame()
        self.appearance()
        self.leftSidedFrame()
        self.centerFrame()

        self.rules_window = None

    def appearance(self):

        self.theme_label = ctk.CTkLabel(self, text='Tema', text_color=['green', '#fff'], bg_color='transparent', font=('Roboto bold', 24)).place(x=48, y=600)
        self.theme_opt = ctk.CTkOptionMenu(self, values=['System', 'Light', 'Dark'], font=('Roboto bold', 16), dropdown_font=('Roboto bold', 16), anchor='center', command=self.app_change).place(x=20, y=630)

    def app_change(self, theme):

        ctk.set_appearance_mode(theme)

    def topFrame(self):

        top_frame = ctk.CTkFrame(self, width=1000, height=70, corner_radius=0, fg_color='darkgreen', bg_color='transparent').place(x=0, y=0)

        rules_button = ctk.CTkButton(top_frame, width=150, height=40, text='Regras', text_color='#fff', font=('Roboto bold', 18), bg_color='darkgreen', fg_color='green', corner_radius=10, command=self.open_rules).place(x=750, y=15)

    def open_rules(self):

        if self.rules_window is None or not self.rules_window.winfo_exists():
            
            self.rules_window = RulesWindow(self)

        else:

            self.rules_window.focus()

    def leftSidedFrame(self):

        lfs_frame = ctk.CTkFrame(self, width=300, height=450, corner_radius=0, fg_color='transparent').place(x=75, y=120)

        #BUTTONS

        play_button = ctk.CTkButton(lfs_frame, width=300, height=70, text='Jogar', fg_color='darkgreen', corner_radius=25, text_color=['#fff', '#fff'], font=('Roboto bold', 48)).place(x=80, y=150)

        load_button = ctk.CTkButton(lfs_frame, width=300, height=70, text='Carregar', fg_color='darkgreen', corner_radius=25, text_color=['#fff', '#fff'], font=('Roboto bold', 48)).place(x=80, y=250)

        ranking_button = ctk.CTkButton(lfs_frame, width=300, height=70, text='Ranking', fg_color='darkgreen', corner_radius=25, text_color=['#fff', '#fff'], font=('Roboto bold', 48)).place(x=80, y=350)

        leave_button = ctk.CTkButton(lfs_frame, width=300, height=70, text='Sair', fg_color='darkgreen', corner_radius=25, text_color=['#fff', '#fff'], font=('Roboto bold', 48)).place(x=80, y=500)

    def centerFrame(self):

        center_frame = ctk.CTkFrame(self, width=500, height=500, corner_radius=0, fg_color='#000').place(x=450, y=100)

        custom = ctk.CTkLabel(center_frame, text='', text_color=['green', '#fff'], font=('Roboto bold', 104)).place(x=470, y=150)

if __name__ == "__main__":
    main = App()
    main.mainloop()