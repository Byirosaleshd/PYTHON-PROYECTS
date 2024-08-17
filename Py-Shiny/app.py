from shiny.express import input, render, ui

ui.input_text("name", "¿Cuál es tu nombre?", value="Mundo")

@render.text
def greeting():
    return f"Hola, {input.name()}!"
