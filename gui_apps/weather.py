import flet as ft 
import requests

def main(page: ft.Page):
    page.title = "Weather"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    user_data = ft.TextField(width=400 , label = "Please input city")
    weather_data = ft.Text('')
    
    def GetInfo(e):
        if len(user_data.value) < 2:
            return 
        API = "224b9c25f8a55f9e01e72f8a4a986241"
        URL = f"https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric"
        res = requests.get(URL).json()
        temperature = res['main']['temp']
        weather_data.value = 'Погода:' + str(temperature)
        page.update()
        

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()
    
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY , on_click=change_theme),
                ft.Text("Weather")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data] , alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data] , alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton(text="Get" , on_click=GetInfo)] , alignment=ft.MainAxisAlignment.CENTER),
        
    )
    
ft.app(target=main)