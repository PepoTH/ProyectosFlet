import flet as ft

def main(page: ft.Page):
    page.window_resizable = False
    page.window_width = 400
    page.window_height = 800
    page.padding = 40

    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.window_center()

    container = ft.Container(ft.Column([
        ft.Text("Prueba")
    ]),bgcolor="red",width=page.window_width*0.80,height=page.window_height*0.7)

    page.add(ft.Text("Facturas",weight=ft.FontWeight.BOLD,size=30),container)
    
ft.app(target=main)