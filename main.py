from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
import docx
from spacetype import Room, Apartment, MultistoryBuilding

#Глобальные настройки
Window.size = (250, 200)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = "Калькулятор строительства"

class MyApp(App):
    def __init__(self):
        super.__init__()
        

def calculate_and_save_report():
    building_type = building_type_var.get()
    length = float(length_entry.get())
    width = float(width_entry.get())
    height = float(height_entry.get())
    
    if building_type == "Комната":
        building = Room(length, width, height)
        total_vol = building.calc_vol()
        heat_power = building.calc_heat_power()
    elif building_type == "Квартира":
        num_rooms = int(rooms_entry.get())
        building = Apartment(length, width, height, num_rooms)
        total_vol = building.calc_total_vol()
        heat_power = building.calc_heat_power()
    else:  # Многоэтажный дом
        num_floors = int(floors_entry.get())
        num_units_per_floor = int(units_entry.get())
        building = MultistoryBuilding(length, width, height, num_floors, num_units_per_floor)
        total_vol = building.calc_total_vol()
        heat_power = building.calc_heat_power()

    # Отображение результатов
    result_label.config(text=f"Общий объем: {total_vol} кв.м\nТепловая мощность: {heat_power} Вт")

    # Сохранение результатов в отчет .docx
    doc = docx.Document()
    doc.add_heading('Результаты расчетов', level=1)
    doc.add_paragraph(f"Общая площадь: {total_vol} куб.м")
    doc.add_paragraph(f"Тепловая мощность: {heat_power} Вт")
    doc.save('report.docx')
    
    messagebox.showinfo("Сохранение", "Результаты сохранены в отчет.docx ")