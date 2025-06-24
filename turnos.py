import tkinter as tk
from tkinter import messagebox
import inventario
import os

def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    pos_x = round(pantalla_ancho / 2 - ancho / 2)
    pos_y = round(pantalla_alto / 2 - alto / 2)
    ventana.geometry(f'{ancho}x{alto}+{pos_x}+{pos_y}')
    ventana.resizable(False, False)

def abrir_turnos():
    ventana_turnos = tk.Toplevel()
    ventana_turnos.title("Gestión de Turnos")
    centrar_ventana(ventana_turnos, 650, 550)
    ventana_turnos.configure(bg="#313131")
    ventana_turnos.resizable(False, False)

    # Botón para volver al inventario
    btn_inventario = tk.Button(ventana_turnos, text="Inventario", fg="#ffffff", bg="#1271dd", font=('Arial', 12), command=lambda: cambiar_a_inventario(ventana_turnos))
    btn_inventario.pack(anchor="nw", padx=10, pady=10)

    # Botón para iniciar turno
    btn_iniciar_turno = tk.Button(ventana_turnos, text="Iniciar Turno", fg="#ffffff", bg="#2a9e5c", font=('Arial', 12), command=iniciar_turno)
    btn_iniciar_turno.pack(anchor="nw", padx=10, pady=10)

    # Historial de turnos
    historial_frame = tk.Frame(ventana_turnos, bg="#313131")
    historial_frame.pack(pady=10)
    lista_historial = tk.Listbox(historial_frame, width=60, height=10)
    lista_historial.pack(pady=5)

    # Cargar historial
    cargar_historial(lista_historial)

def cargar_historial(lista_historial):
    lista_historial.delete(0, tk.END)
    if os.path.exists("historial_turnos.txt"):
        with open("historial_turnos.txt", "r") as file:
            for linea in file:
                lista_historial.insert(tk.END, linea.strip())

def iniciar_turno():
    ventana_turno = tk.Toplevel()
    ventana_turno.title("Iniciar Turno")
    centrar_ventana(ventana_turno, 400, 300)
    ventana_turno.configure(bg="#313131")

    tk.Label(ventana_turno, text="Hora de Entrada:", fg="white", bg="#313131", font=('Arial', 12)).pack(pady=5)
    entry_inicio = tk.Entry(ventana_turno, font="Arial")
    entry_inicio.pack(pady=5)

    tk.Label(ventana_turno, text="Hora de Salida:", fg="white", bg="#313131", font=('Arial', 12)).pack(pady=5)
    entry_salida = tk.Entry(ventana_turno, font="Arial")
    entry_salida.pack(pady=5)

    tk.Label(ventana_turno, text="Cantidad de Ropa Sacada:", fg="white", bg="#313131", font=('Arial', 12)).pack(pady=5)
    entry_ropa = tk.Entry(ventana_turno, font="Arial")
    entry_ropa.pack(pady=5)

    tk.Button(ventana_turno, text="Guardar Turno", fg="#ffffff", bg='#2a9e5c', font=('Arial', 12),
              command=lambda: guardar_turno(entry_inicio.get(), entry_salida.get(), entry_ropa.get(), ventana_turno)).pack(pady=10)

def guardar_turno(hora_inicio, hora_salida, cantidad_ropa, ventana_turno):
    if not hora_inicio or not hora_salida or not cantidad_ropa.isdigit():
        messagebox.showerror("Error", "Ingrese información válida.")
        return

    with open("historial_turnos.txt", "a") as file:
        file.write(f"Turno: {hora_inicio} - {hora_salida}, Ropa retirada: {cantidad_ropa}\n")

    ventana_turno.destroy()
    messagebox.showinfo("Éxito", "Turno guardado correctamente.")

def cambiar_a_inventario(ventana_turnos):
    ventana_turnos.destroy()
    inventario.abrir_inventario()