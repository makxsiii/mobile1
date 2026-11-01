from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from instructions import *
from ruffier import *

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lab = Label(text=txt_instruction, size_hint=(.9, .9), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='left')
        name = Label(text='Введите имя:', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        age = Label(text='Введите возраст:', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        self.tiname = TextInput(text='', multiline=False)
        self.tiage = TextInput(text='', multiline=False)  # Убрали global, сделали свойством класса
        
        self.btn = Button(text='Начать', size_hint=(.2, .2), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        self.btn.on_press = self.next
        
        vl = BoxLayout(orientation='vertical')
        hl1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        hl2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        
        hl1.add_widget(name)
        hl1.add_widget(self.tiname)
        hl2.add_widget(age)
        hl2.add_widget(self.tiage)
        
        vl.add_widget(lab)
        vl.add_widget(hl1)
        vl.add_widget(hl2)
        vl.add_widget(self.btn)
        self.add_widget(vl)

    def next(self):
        try:
            self.manager.age = int(self.tiage.text)
            self.manager.name = self.tiname.text
            self.manager.current = 'second'
        except ValueError:
            print("Ошибка: возраст должен быть числом!")


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lab = Label(text=txt_test1, size_hint=(.9, .9), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='left')
        res = Label(text='Введите результат:', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        self.tires = TextInput(text='', multiline=False)
        
        self.btn = Button(text='Продолжить', size_hint=(.2, .2), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        self.btn.on_press = self.next
        
        vl = BoxLayout(orientation='vertical')
        hl = BoxLayout(size_hint=(0.8, None), height='30sp')
        hl.add_widget(res)
        hl.add_widget(self.tires)
        vl.add_widget(lab)
        vl.add_widget(hl)
        vl.add_widget(self.btn)
        self.add_widget(vl)

    def next(self):
        try:
            self.manager.P1 = int(self.tires.text)
            self.manager.current = 'thirst'
        except ValueError:
            print("Ошибка: введите число!")


class ThirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lab = Label(text=txt_sits, size_hint=(.9, .9), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='left')
        self.btn = Button(text='Продолжить', size_hint=(.2, .2), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        self.btn.on_press = self.next
        
        vl = BoxLayout(orientation='vertical')
        vl.add_widget(lab)
        vl.add_widget(self.btn)
        self.add_widget(vl)

    def next(self):
        self.manager.current = 'fourth'


class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lab = Label(text=txt_test3)
        res = Label(text='Результат:')
        resrelax = Label(text='Результат после отдыха:')
        
        self.tires1 = TextInput(text='', multiline=False)
        self.tiresrelax = TextInput(text='', multiline=False)
        
        self.btn = Button(text='Завершить', size_hint=(.2, .2), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        self.btn.on_press = self.next
        
        vl = BoxLayout(orientation='vertical')
        hl1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        hl2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        
        hl1.add_widget(res)
        hl1.add_widget(self.tires1)
        hl2.add_widget(resrelax)
        hl2.add_widget(self.tiresrelax)
        
        vl.add_widget(lab)
        vl.add_widget(hl1)
        vl.add_widget(hl2)
        vl.add_widget(self.btn)
        self.add_widget(vl)

    def next(self):
        try:
            self.manager.P2 = int(self.tires1.text)
            self.manager.P3 = int(self.tiresrelax.text)
            self.manager.current = 'fifth'
        except ValueError:
            print("Ошибка: введите числа в оба поля!")


class FifthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lab = Label(text='Расчет...', halign='center')
        try:
            P1 = self.manager.P1
            P2 = self.manager.P2
            P3 = self.manager.P3
            age = self.manager.age
            result_text = test(P1, P2, P3, age)
            self.lab.text = result_text
        except Exception as e:
            self.lab.text = f"Ошибка при расчете: {e}"
        vl = BoxLayout(orientation='vertical')
        vl.add_widget(self.lab)
        self.add_widget(vl)


class Check(App):
    def build(self):
        sm = ScreenManager()
        sm.age = 0
        sm.P1 = 0
        sm.P2 = 0
        sm.P3 = 0
        
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirstScreen(name='thirst'))
        sm.add_widget(FourthScreen(name='fourth'))
        sm.add_widget(FifthScreen(name='fifth'))
        return sm

if __name__ == '__main__':
    app = Check()
    app.run()
