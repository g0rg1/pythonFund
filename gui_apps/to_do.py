from flet import * 
import flet as ft 

def main(page:ft.Page):
        BG = "#041955"
        FWG = "#97b4ff"
        PG = "#3450a1"
        PINK = "eb06ff"
        page_1 = Container()
        page_2 = Row(
            controls=Container(
                width=400,
                height=550,
                bgcolor=FWG,
                border_radius=35,
                padding=padding.only(
                    top=50 , left=20,
                    right=20 , bottom=5
                )
            )
        )
        
        
        container = Container(
            
            width = 800 , height=550 , bgcolor=BG , border_radius=35,content=Stack(
                controls=[
                    page_1,
                    page_2
                    
                ]
            )
            
        )
        page.add(container)
        
        
app(target=main)
    