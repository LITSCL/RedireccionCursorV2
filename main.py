import pyautogui
import keyboard
from tkinter import Tk, Button

#Variable para almacenar la posición del cursor.
posicion_cursor_guardada: object = None

#Función para guardar la posición actual del cursor.
def guardar_posicion() -> None:
    global posicion_cursor_guardada
    posicion_cursor_guardada = pyautogui.position()
    print(f"Posición guardada: {posicion_cursor_guardada}")

#Función para restaurar el cursor a la posición guardada.
def restaurar_posicion() -> None:
    if (posicion_cursor_guardada):
        pyautogui.moveTo(posicion_cursor_guardada[0], posicion_cursor_guardada[1])
        print("Cursor restaurado a la posición guardada")

#Configuración de la ventana.
root: object = Tk()
root.title("Gestor de Posición del Cursor")

#Botón para guardar la posición.
btn_guardar = Button(root, text = "Guardar Posición (Ctrl+Q)", command = guardar_posicion)
btn_guardar.pack()

#Botón para restaurar la posición.
btn_restaurar = Button(root, text = "Restaurar Posición (Ctrl+W)", command = restaurar_posicion)
btn_restaurar.pack()

#Función para manejar eventos de teclado.
def tecla_presionada(tecla: object) -> None:
    try:
        if (keyboard.is_pressed("ctrl+q")):
            guardar_posicion()
        elif (keyboard.is_pressed("ctrl+w")):
            restaurar_posicion()
    except Exception:
        print("Error")

#Configuración del listener de teclado.
keyboard.hook(tecla_presionada)

#Inicia el bucle de la interfaz gráfica.
root.mainloop()
