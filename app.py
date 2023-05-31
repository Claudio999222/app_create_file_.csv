import os
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import re
import csv
from datetime import date
import logging


def koch_csv_App():
    pass

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class koch_csv(App):
    def build(self):
        layout = FloatLayout()

        self.window = GridLayout()
        self.window.cols = 1
        Window.size = (840, 480)
        Window.minimum_height = 480
        Window.maximum_height = 480
        Window.minimum_width = 840
        Window.maximum_width = 840

        background_image = Image(source="25101.jpg", allow_stretch=True, keep_ratio=True)
        layout.add_widget(background_image)

        foreground_image = Image(source="download.png")
        foreground_image.pos = (0, layout.height - foreground_image.height)
        layout.add_widget(foreground_image)

        options = 'Saldatura', 'Piega', 'Punzonatura', 'Laser', 'Montaggio Valvole'
        spinner = Spinner(text='Seleziona Mansione', values=options, size_hint=(0.2, 0.10), size=(20, 10),
                          pos_hint={'center_x': 0.15, 'center_y': 0.90})
        layout.add_widget(spinner)

        options1 = 'Mattina', 'Pomeriggio', 'Notte'
        spinner1 = Spinner(text='Seleziona Turno', values=options1, size_hint=(0.2, 0.10), size=(20, 10),
                           pos_hint={'center_x': 0.15, 'center_y': 0.70})
        layout.add_widget(spinner1)

        self.text_input0 = TextInput(text='KG-0000000000', size_hint=(0.20, 0.07), size=(20, 10),
                                     pos_hint={'center_x': 0.38, 'center_y': 0.90})
        layout.add_widget(self.text_input0)

        self.text_input1 = TextInput(text='Marcatura', size_hint=(0.20, 0.07), size=(20, 10),
                                pos_hint={'center_x': 0.61, 'center_y': 0.90})
        layout.add_widget(self.text_input1)

        self.text_input2 = TextInput(text='Pezzi', size_hint=(0.20, 0.07), size=(20, 10),
                                pos_hint={'center_x': 0.84, 'center_y': 0.90})
        layout.add_widget(self.text_input2)

        self.text_input3 = TextInput(text='Cognome', size_hint=(0.20, 0.07), size=(20, 10),
                                     pos_hint={'center_x': 0.84, 'center_y': 0.70})
        layout.add_widget(self.text_input3)

        self.text_input4 = TextInput(text='Sales Order', size_hint=(0.20, 0.07), size=(20, 10),
                                     pos_hint={'center_x': 0.38, 'center_y': 0.70})
        layout.add_widget(self.text_input4)

        self.text_input5 = TextInput(text='Marcatura KG', size_hint=(0.20, 0.07), size=(20, 10),
                                     pos_hint={'center_x': 0.61, 'center_y': 0.70})
        layout.add_widget(self.text_input5)

        button = Button(text='Esporta', size_hint=(0.20, 0.07), size=(20, 10),
                        pos_hint={'center_x': 0.84, 'center_y': 0.10})
        button.bind(on_press=lambda x: self.get_input(self.text_input0.text, self.text_input1.text, self.text_input2.text,
                                                      self.text_input3.text, self.text_input4.text,
                                                      self.text_input5.text, spinner.text, spinner1.text))
        layout.add_widget(button)

        self.text_input0.bind(focus=self.on_text_input_focus0)
        self.text_input1.bind(focus=self.on_text_input_focus1)
        self.text_input2.bind(focus=self.on_text_input_focus2)
        self.text_input3.bind(focus=self.on_text_input_focus3)
        self.text_input4.bind(focus=self.on_text_input_focus4)
        self.text_input5.bind(focus=self.on_text_input_focus5)

        self.checkbox0 = CheckBox(active=False, size_hint=(0.1, 0.1), pos_hint={'center_x': 0.29, 'center_y': 0.83})
        self.checkbox0.bind(active=self.on_checkbox_active)
        layout.add_widget(self.checkbox0)

        self.checkbox1 = CheckBox(active=False, size_hint=(0.1, 0.1), pos_hint={'center_x': 0.75, 'center_y': 0.63})
        self.checkbox1.bind(active=self.on_checkbox_active0)
        layout.add_widget(self.checkbox1)

        self.checkbox2 = CheckBox(active=False, size_hint=(0.1, 0.1), pos_hint={'center_x': 0.29, 'center_y': 0.63})
        self.checkbox2.bind(active=self.on_checkbox_active1)
        layout.add_widget(self.checkbox2)

        self.checkbox3 = CheckBox(active=False, size_hint=(0.1, 0.1), pos_hint={'center_x': 0.52, 'center_y': 0.63})
        self.checkbox3.bind(active=self.on_checkbox_active2)
        layout.add_widget(self.checkbox3)

        label1 = Label(text='<--Blocco Cella', size_hint=(0.2, 0.1), pos_hint={'center_x': 0.365, 'center_y': 0.83})
        label1.color = (0, 0, 0, 1)
        layout.add_widget(label1)

        label2 = Label(text='<--Blocco Cella', size_hint=(0.2, 0.1), pos_hint={'center_x': 0.825, 'center_y': 0.63})
        label2.color = (0, 0, 0, 1)
        layout.add_widget(label2)

        label3 = Label(text='<--Blocco Cella', size_hint=(0.2, 0.1), pos_hint={'center_x': 0.365, 'center_y': 0.63})
        label3.color = (0, 0, 0, 1)
        layout.add_widget(label3)

        label4 = Label(text='<--Blocco Cella', size_hint=(0.2, 0.1), pos_hint={'center_x': 0.595, 'center_y': 0.63})
        label4.color = (0, 0, 0, 1)
        layout.add_widget(label4)

        self.popup = Popup(title="ERRORE MARCATURA", content=Label(text="---MARCATURA INESISTENTE!---"),
                           size_hint=(None, None),
                           size=(400, 200))

        self.popup0 = Popup(title="ERRORE MANSIONE", content=Label(text="---INSERISCI MANSIONE!---"),
                            size_hint=(None, None),
                            size=(400, 200))

        self.popup1 = Popup(title="ERRORE TURNO", content=Label(text="---INSERISCI TURNO!---"), size_hint=(None, None),
                            size=(400, 200))

        self.popup2 = Popup(title="ERRORE COMMESSA", content=Label(text="---INSERISCI COMMESSA!---"),
                            size_hint=(None, None),
                            size=(400, 200))

        self.popup3 = Popup(title="ERRORE MARCATURA", content=Label(text="---INSERISCI MARCATURA!---"),
                            size_hint=(None, None),
                            size=(400, 200))

        self.popup4 = Popup(title="ERRORE PEZZI", content=Label(text="---INSERISCI PEZZI!---"), size_hint=(None, None),
                            size=(400, 200))

        self.popup5 = Popup(title="ERRORE COGNOME", content=Label(text="---INSERISCI COGNOME!---"),
                            size_hint=(None, None),
                            size=(400, 200))

        self.popup6 = Popup(title="ERRORE PEZZI ", content=Label(text="---FORMATO ERRATO!---"), size_hint=(None, None),
                            size=(400, 200))

        self.popup7 = Popup(title="ERRORE COGNOME ", content=Label(text="---FORMATO ERRATO!---"),
                            size_hint=(None, None),
                            size=(400, 200))

        self.popup8 = Popup(title="ERRORE COMMESSA ", content=Label(text="---FORMATO ERRATO!---"),
                            size_hint=(None, None),
                            size=(400, 200))
        self.popup9 = Popup(title="ERRORE SALES ORDER ", content=Label(text="---FORMATO ERRATO!---"),
                            size_hint=(None, None),
                            size=(400, 200))
        self.popup10 = Popup(title="ERRORE SALES ORDER ", content=Label(text="---INSERISCI SALES ORDER!---"),
                             size_hint=(None, None),
                             size=(400, 200))
        self.popup11 = Popup(title="ERRORE MARCATURA KG ", content=Label(text="---INSERISCI MARCATURA KG!---"),
                             size_hint=(None, None),
                             size=(400, 200))
        self.popup12 = Popup(title="ERRORE MARCATURA KG ", content=Label(text="---FORMATO ERRATO!---"),
                             size_hint=(None, None),
                             size=(400, 200))
        self.popup13 = Popup(title="ERRORE NONE ", content=Label(text="---INSERIMENTO NON CARICATO!---"),
                             size_hint=(None, None),
                             size=(400, 200))

        return layout

    def on_checkbox_active(self, instance, value):
        self.text_input0.disabled = value

    def on_checkbox_active0(self, instance, value):
        self.text_input3.disabled = value

    def on_checkbox_active1(self, instance, value):
        self.text_input4.disabled = value

    def on_checkbox_active2(self, instance, value):
        self.text_input5.disabled = value

    def on_text_input_focus0(self, instance, value):
        if value:
            if instance.text == 'KG-0000000000':
                instance.text = ""

        else:
            if instance.text == "":
                instance.text = 'KG-0000000000'

    def on_text_input_focus1(self, instance, value):
        if value:
            if instance.text == 'Marcatura':
                instance.text = ""

        else:
            if instance.text == "":
                instance.text = 'Marcatura'

    def on_text_input_focus2(self, instance, value):
        if value:
            if instance.text == 'Pezzi':
                instance.text = ""

        else:
            if instance.text == "":
                instance.text = 'Pezzi'

    def on_text_input_focus3(self, instance, value):
        if value:
            if instance.text == 'Cognome':
                instance.text = ""

        else:
            if instance.text == "":
                instance.text = 'Cognome'

    def on_text_input_focus4(self, instance, value):
        if value:
            if instance.text == 'Sales Order':
                instance.text = ""

        else:
            if instance.text == "":
                instance.text = 'Sales Order'

    def on_text_input_focus5(self, instance, value):
        if value:
            if instance.text == 'Marcatura KG':
                instance.text = ""

        else:
            if instance.text == "":
                instance.text = 'Marcatura KG'

    def clear_text_input0(self, checkbox0):
        if not checkbox0.active:
            self.text_input0.text = ''

    def clear_text_input1(self, checkbox1):
        if not checkbox1.active:
            self.text_input3.text = ''

    def clear_text_input2(self, checkbox2):
        if not checkbox2.active:
            self.text_input4.text = ''

    def clear_text_input3(self, checkbox3):
        if not checkbox3.active:
            self.text_input5.text = ''

    def check_format_Marcatura(self, input_string, input1):
        pattern = r'^[A-Za-z]\d{3}$'
        pattern1 = r'^[A-Za-z]-\d{3}$'
        pattern2 = r'^[A-Za-z]{2}\d{3}$'
        pattern3 = r'^[A-Za-z]{2}-\d{3}$'
        pattern4 = r'^[A-Za-z]-\d{3}[A-Za-z]$'
        pattern5 = r'^[A-Za-z]\d{3}[A-Za-z]$'
        pattern6 = r'^[A-Za-z]{2}\d{3}[A-Za-z]$'
        pattern7 = r'^[A-Za-z]{2}-\d{3}[A-Za-z]$'
        pattern8 = r'^[A-Za-z]-\d{3}[A-Za-z]{2}$'
        pattern9 = r'^[A-Za-z]\d{3}[A-Za-z]{2}$'
        pattern10 = r'^[A-Za-z]{2}\d{3}[A-Za-z]{2}$'
        pattern11 = r'^[A-Za-z]{2}-\d{3}[A-Za-z]{2}$'
        pattern12 = r'^\d{3}[A-Za-z]$'
        pattern13 = r'^\d{3}[A-Za-z]{2}$'
        pattern14 = r'^\d{3}$'

        match = re.match(pattern, input_string)
        match1 = re.match(pattern1, input_string)
        match2 = re.match(pattern2, input_string)
        match3 = re.match(pattern3, input_string)
        match4 = re.match(pattern4, input_string)
        match5 = re.match(pattern5, input_string)
        match6 = re.match(pattern6, input_string)
        match7 = re.match(pattern7, input_string)
        match8 = re.match(pattern8, input_string)
        match9 = re.match(pattern9, input_string)
        match10 = re.match(pattern10, input_string)
        match11 = re.match(pattern11, input_string)
        match12 = re.match(pattern12, input_string)
        match13 = re.match(pattern13, input_string)
        match14 = re.match(pattern14, input_string)

        inp = None

        if bool(match) == True:
            inp = input1[0].upper() + '-' + input1[1:]
        elif bool(match1) == True:
            inp = input1[0].upper() + input1[1:]
        elif bool(match2) == True:
            inp = (input1[0] + input1[1]).upper() + '-' + input1[2:]
        elif bool(match3) == True:
            inp = (input1[0] + input1[1]).upper() + input1[2:]
        elif bool(match4) == True:
            inp = input1[0].upper() + '-' + input1[1:].lower()
        elif bool(match5) == True:
            inp = input1[0].upper() + '-' + input1[1:].lower()
        elif bool(match6) == True:
            inp = (input1[0] + input1[1]).upper() + '-' + input1[2:].lower()
        elif bool(match7) == True:
            inp = (input1[0] + input1[1]).upper() + input1[2:].lower()
        elif bool(match8) == True:
            inp = input1[0].upper() + '-' + input1[1:].lower()
        elif bool(match9) == True:
            inp = input1[0].upper() + '-' + input1[1:].lower()
        elif bool(match10) == True:
            inp = (input1[0] + input1[1]).upper() + '-' + input1[2:].lower()
        elif bool(match11) == True:
            inp = (input1[0] + input1[1]).upper() + input1[2:].lower()
        elif bool(match12) == True:
            inp = input1.lower()
        elif bool(match13) == True:
            inp = input1.lower()
        elif bool(match14) == True:
            inp = input1

        else:
            self.popup.open()

        return inp

    def check_format_pezzi(self, input_string, input2):
        pattern = r'^\d$'
        pattern1 = r'^\d{2}$'
        pattern2 = r'^\d{3}$'
        pattern3 = r'^\d{4}$'

        match = re.match(pattern, input_string)
        match1 = re.match(pattern1, input_string)
        match2 = re.match(pattern2, input_string)
        match3 = re.match(pattern3, input_string)

        inp1 = None

        if bool(match) == True:
            inp1 = input2
        elif bool(match1) == True:
            inp1 = input2
        elif bool(match2) == True:
            inp1 = input2
        elif bool(match3) == True:
            inp1 = input2


        else:
            self.popup6.open()

        return inp1

    def check_format_cognome(self, input_string, input3):
        pattern = r'^[A-Za-z]$'
        pattern1 = r'^[A-Za-z]{2}$'
        pattern2 = r'^[A-Za-z]{3}$'
        pattern3 = r'^[A-Za-z]{4}$'
        pattern4 = r'^[A-Za-z]{5}$'
        pattern5 = r'^[A-Za-z]{6}$'
        pattern6 = r'^[A-Za-z]{7}$'
        pattern7 = r'^[A-Za-z]{8}$'
        pattern8 = r'^[A-Za-z]{9}$'
        pattern9 = r'^[A-Za-z]{10}$'
        pattern10 = r'^[A-Za-z]{2} [A-Za-z]{2}$'
        pattern11 = r'^[A-Za-z]{2} [A-Za-z]{3}$'
        pattern12 = r'^[A-Za-z]{2} [A-Za-z]{4}$'
        pattern13 = r'^[A-Za-z]{2} [A-Za-z]{5}$'
        pattern14 = r'^[A-Za-z]{2} [A-Za-z]{6}$'
        pattern15 = r'^[A-Za-z]{2} [A-Za-z]{7}$'
        pattern16 = r'^[A-Za-z]{2} [A-Za-z]{8}$'
        pattern17 = r'^[A-Za-z]{2} [A-Za-z]{9}$'
        pattern18 = r'^[A-Za-z]{3} [A-Za-z]{2}$'
        pattern19 = r'^[A-Za-z]{3} [A-Za-z]{3}$'
        pattern20 = r'^[A-Za-z]{3} [A-Za-z]{4}$'
        pattern21 = r'^[A-Za-z]{3} [A-Za-z]{5}$'
        pattern22 = r'^[A-Za-z]{3} [A-Za-z]{6}$'
        pattern23 = r'^[A-Za-z]{3} [A-Za-z]{7}$'
        pattern24 = r'^[A-Za-z]{3} [A-Za-z]{8}$'
        pattern25 = r'^[A-Za-z]{3} [A-Za-z]{9}$'

        match = re.match(pattern, input_string)
        match1 = re.match(pattern1, input_string)
        match2 = re.match(pattern2, input_string)
        match3 = re.match(pattern3, input_string)
        match4 = re.match(pattern4, input_string)
        match5 = re.match(pattern5, input_string)
        match6 = re.match(pattern6, input_string)
        match7 = re.match(pattern7, input_string)
        match8 = re.match(pattern8, input_string)
        match9 = re.match(pattern9, input_string)
        match10 = re.match(pattern10, input_string)
        match11 = re.match(pattern11, input_string)
        match12 = re.match(pattern12, input_string)
        match13 = re.match(pattern13, input_string)
        match14 = re.match(pattern14, input_string)
        match15 = re.match(pattern15, input_string)
        match16 = re.match(pattern16, input_string)
        match17 = re.match(pattern17, input_string)
        match18 = re.match(pattern18, input_string)
        match19 = re.match(pattern19, input_string)
        match20 = re.match(pattern20, input_string)
        match21 = re.match(pattern21, input_string)
        match22 = re.match(pattern22, input_string)
        match23 = re.match(pattern23, input_string)
        match24 = re.match(pattern24, input_string)
        match25 = re.match(pattern25, input_string)

        inp3 = None

        if bool(match) == True:
            inp3 = input3[0].upper() + input3[1:].lower()
        elif bool(match1) == True or bool(match2) == True or bool(match3) == True or bool(match4) == True or bool(
                match5) == True or bool(match6) == True or bool(match7) == True or bool(match8) == True or bool(
            match9) == True:
            inp3 = input3[0].upper() + input3[1:].lower()
        elif bool(match10) == True or bool(match11) == True or bool(match12) == True or bool(match13) == True or bool(
                match14) == True or bool(match15) == True or bool(match16) == True or bool(match17) == True:
            inp3 = input3[0].upper() + (input3[1] + input3[2]).lower() + input3[3].upper() + input3[4:].lower()
        elif bool(match18) == True or bool(match19) == True or bool(match20) == True or bool(match21) == True or bool(
                match22) == True or bool(match23) == True or bool(match24) == True or bool(match25) == True:
            inp3 = input3[0].upper() + (input3[1] + input3[2] + input3[3]).lower() + input3[4].upper() + input3[
                                                                                                         5:].lower()

        else:
            self.popup7.open()

        return inp3

    def check_format_KG(self, input_string, input0):
        inp4 = None

        if input0 != (input0[0] + input0[1]).upper() + input0[2:] and input0[2] == '-' and input0[0].isalpha() and \
                input0[1].isalpha():
            inp4 = (input0[0] + input0[1]).upper() + input0[2:]
        elif input0[3].isalpha() or input0[4].isalpha() or input0[5].isalpha() or input0[6].isalpha():
            self.popup8.open()
        elif input0 != (input0[0] + input0[1]).upper() + input0[2:] and input0[2] != '-' and input0[0].isalpha() and \
                input0[1].isalpha():
            inp4 = (input0[0] + input0[1]).upper() + '-' + input0[2:]
        elif input0[0].isalpha() == False and input0[1].isalpha() == False and input0[0] == '-':
            inp4 = 'KG' + input0
        elif input0[0].isalpha() == False and input0[1].isalpha() == False and input0[2] != '-':
            inp4 = 'KG-' + input0
        elif input0[0].isalpha() and input0[1].isalpha() == False and input0[1] == '-':
            inp4 = 'KG' + input0[1:]
        elif input0[0].isalpha() and input0[1].isalpha() == False and input0[1] != '-':
            inp4 = 'KG-' + input0[1:]

        else:
            self.popup8.open()

        return inp4

    def check_format_mark_KG(self, input_string, input5):
        pattern = r'^\d$'
        pattern1 = r'^\d{2}$'
        pattern2 = r'^\d{3}$'

        match = re.match(pattern, input_string)
        match1 = re.match(pattern1, input_string)
        match2 = re.match(pattern2, input_string)

        inp5 = None

        if bool(match) == True:
            inp5 = input5
        elif bool(match1) == True:
            inp5 = input5
        elif bool(match2) == True:
            inp5 = input5

        else:
            self.popup12.open()

        return inp5

    def check_format_sales_order(self, input_string, input4):
        pattern = r'^[A-Za-z]{3}\d+$'
        pattern1 = r'^[A-Za-z]{4}\d+$'

        inp6 = None

        match = re.match(pattern, input_string)
        match1 = re.match(pattern1, input_string)

        if bool(match) == True:
            inp6 = (input4[0] + input4[1] + input4[2]).upper() + input4[3:]
        elif bool(match1) == True:
            inp6 = (input4[0] + input4[1] + input4[2] + input4[3]).upper() + input4[4:]
        else:
            self.popup9.open()

        return inp6


    def get_input(self, input0, input1, input2, input3, input4, input5, selected_option, selected_option1):

        global inp00
        global inp000
        global inp0000
        global inp00000
        global inp000000
        global inp0000000

        if selected_option == 'Seleziona Mansione' or selected_option == '':
            self.popup0.open()
        if selected_option1 == 'Seleziona Turno' or selected_option1 == '':
            self.popup1.open()

        inp00 = None
        inp000 = None
        inp0000 = None
        inp00000 = None
        inp000000 = None
        inp0000000 = None


        if input0 == 'KG-0000000000' or input0 == '':
            self.popup2.open()
        else:
            inp00 = self.check_format_KG(input0, input0)

        if input1 == 'Marcatura' or input1 == '':
            self.popup3.open()
        else:
            inp000 = self.check_format_Marcatura(input1, input1)
            print(inp000)

        if input2 == 'Pezzi' or input2 == '':
            self.popup4.open()

        else:
            inp0000 = self.check_format_pezzi(input2, input2)
            print(inp0000)

        if input3 == 'Cognome' or input3 == '':
            self.popup5.open()

        else:
            inp00000 = self.check_format_cognome(input3, input3)
            print(inp00000)

        if input4 == 'Sales Order' or input4 == '':
            self.popup9.open()

        else:
            inp000000 = self.check_format_sales_order(input4, input4)
            print(inp000000)

        if input5 == 'Marcatura KG' or input5 == '':
            self.popup11.open()

        else:
            inp0000000 = self.check_format_mark_KG(input5, input5)
            print(inp0000000)

        if inp00 == None or inp000 == None or inp0000 == None or inp00000 == None or inp000000 == None or inp0000000 == None or selected_option == 'Seleziona Mansione' or selected_option1 == 'Seleziona Turno':
            self.popup13.open()

        if inp00 != None and inp000 != None and inp0000 != None and inp00000 != None and inp000000 != None and inp0000000 != None and selected_option != 'Seleziona Mansione' and selected_option1 != 'Seleziona Turno':
            file_path = "dati.csv"
            data_corrente = date.today().strftime("%d-%m-%Y")

            if os.path.exists('dati.csv'):
                mode = 'a'
            else:
                mode = 'w'


            if os.path.exists('dati.csv'):
                mode = 'a'
            else:
                mode = 'w'


            with open('dati.csv', mode=mode, newline='') as file:
                writer = csv.writer(file)

                if mode == 'w':
                    writer.writerow(
                        ["Data", "Cognome", "Mansione", "Turno", "Sales Order", "KG", "Marcatura KG", "Marcatura",
                         "Pezzi"])

                writer.writerow(
                    [data_corrente, inp00000, selected_option, selected_option1, inp000000, inp00, inp0000000, inp000,
                     inp0000])

            if not self.checkbox0.active:
                self.text_input0.text = 'KG-0000000000'

            self.text_input1.text = 'Marcatura'

            self.text_input2.text = 'Pezzi'

            if not self.checkbox1.active:
                self.text_input3.text = 'Cognome'

            if not self.checkbox2.active:
                self.text_input4.text = 'Sales Order'

            if not self.checkbox3.active:
                self.text_input5.text = 'Marcatura KG'


if __name__ == '__main__':
    koch_csv().run()
