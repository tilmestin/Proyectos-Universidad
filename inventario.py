import tkinter as tk
from tkinter import ttk, messagebox
import os
import turnos

def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    pos_x = round(pantalla_ancho / 2 - ancho / 2)
    pos_y = round(pantalla_alto / 2 - alto / 2)
    ventana.geometry(f'{ancho}x{alto}+{pos_x}+{pos_y}')
    ventana.resizable(False, False)

def abrir_inventario():
    ventana_inventario = tk.Toplevel()
    ventana_inventario.title("Gestión de Inventario")
    centrar_ventana(ventana_inventario, 670, 580)  # Tamaño ajustado
    ventana_inventario.configure(bg="#313131")
    ventana_inventario.resizable(False, False)

    # Botón para cambiar a Turnos
    btn_turnos = tk.Button(ventana_inventario, text="Turnos", fg="#ffffff", bg="#1271dd", font=('Arial', 12), command=lambda: cambiar_a_turnos(ventana_inventario))
    btn_turnos.pack(anchor="nw", padx=10, pady=10)

    frame_contenido = tk.Frame(ventana_inventario, bg="#313131")
    frame_contenido.pack(pady=10)

    tabla = ttk.Treeview(frame_contenido, columns=("ID", "Producto", "Cantidad"), show="headings")
    tabla.heading("ID", text="ID")
    tabla.heading("Producto", text="Producto")
    tabla.heading("Cantidad", text="Cantidad")
    tabla.pack(pady=10)

    def cargar_inventario():
        tabla.delete(*tabla.get_children())

        if not os.path.exists("inventario.txt"):
            open("inventario.txt", "w").close()

        with open("inventario.txt", "r") as file:
            inventario = [linea.strip().split(",") for linea in file]

        nuevo_inventario = []
        for i, datos in enumerate(inventario):
            if len(datos) == 3:
                nuevo_inventario.append([str(i + 1), datos[1], datos[2]])

        for datos in nuevo_inventario:
            tabla.insert("", "end", values=datos)

        return nuevo_inventario

    frame_entrada = tk.Frame(frame_contenido, bg="#313131")
    frame_entrada.pack(pady=10)

    tk.Label(frame_entrada, text="Producto:", fg="white", bg="#313131", font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=5)
    entry_producto = tk.Entry(frame_entrada, font="Arial")
    entry_producto.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_entrada, text="Cantidad:", fg="white", bg="#313131", font=('Arial', 12)).grid(row=1, column=0, padx=5, pady=5)
    entry_cantidad = tk.Entry(frame_entrada, font="Arial")
    entry_cantidad.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_entrada, text="Eliminar Producto:", fg="white", bg="#313131", font=('Arial', 12)).grid(row=2, column=0, padx=5, pady=5)
    entry_eliminar_producto = tk.Entry(frame_entrada, font="Arial")
    entry_eliminar_producto.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame_entrada, text="Cantidad a Eliminar:", fg="white", bg="#313131", font=('Arial', 12)).grid(row=3, column=0, padx=5, pady=5)
    entry_eliminar_cantidad = tk.Entry(frame_entrada, font="Arial")
    entry_eliminar_cantidad.grid(row=3, column=1, padx=5, pady=5)

    def agregar_item():
        producto = entry_producto.get().strip()
        cantidad = entry_cantidad.get().strip()

        if not producto or not cantidad.isdigit():
            messagebox.showerror("Error", "Ingrese un producto y una cantidad válida.")
            return

        inventario = cargar_inventario()
        nuevo_id = len(inventario) + 1

        with open("inventario.txt", "a") as file:
            file.write(f"{nuevo_id},{producto},{cantidad}\n")

        cargar_inventario()
        messagebox.showinfo("Éxito", f"Producto {producto} agregado con {cantidad} unidades.")
        entry_producto.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)

    def eliminar_item():
        producto = entry_eliminar_producto.get().strip()
        cantidad_eliminar = entry_eliminar_cantidad.get().strip()

        if not producto or not cantidad_eliminar.isdigit():
            messagebox.showerror("Error", "Ingrese un producto y una cantidad válida para eliminar.")
            return

        cantidad_eliminar = int(cantidad_eliminar)
        inventario = cargar_inventario()
        nuevo_inventario = []

        eliminado = False
        for datos in inventario:
            if len(datos) == 3 and datos[1] == producto:
                cantidad_actual = int(datos[2])

                if cantidad_eliminar >= cantidad_actual:
                    eliminado = True
                    continue
                else:
                    datos[2] = str(cantidad_actual - cantidad_eliminar)
                    eliminado = True

            nuevo_inventario.append(datos)

        if eliminado:
            with open("inventario.txt", "w") as file:
                for i, datos in enumerate(nuevo_inventario):
                    file.write(f"{i+1},{datos[1]},{datos[2]}\n")

            cargar_inventario()
            messagebox.showinfo("Éxito", f"{cantidad_eliminar} unidades de {producto} eliminadas.")
        else:
            messagebox.showerror("Error", "El producto no existe o la cantidad ingresada es incorrecta.")

        entry_eliminar_producto.delete(0, tk.END)
        entry_eliminar_cantidad.delete(0, tk.END)

    tk.Button(frame_contenido, text="Agregar", fg="#ffffff", bg='#2a9e5c', font=('Arial', 12), command=agregar_item).pack(pady=10)
    tk.Button(frame_contenido, text="Eliminar", fg="#ffffff", bg='#9e2a2a', font=('Arial', 12), command=eliminar_item).pack(pady=10)

    cargar_inventario()

def cambiar_a_turnos(ventana_inventario):
    ventana_inventario.destroy()
    turnos.abrir_turnos()








