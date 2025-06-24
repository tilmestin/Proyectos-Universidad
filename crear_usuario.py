import tkinter as tk
from tkinter import messagebox

def crearUsuario(cerrarVentana):
    cerrarVentana.withdraw()  # Oculta la ventana principal

    ventana_crear = tk.Toplevel()
    ventana_crear.title('Crear Usuario - Kali York')

    # Configurar tamaño y posición
    ancho_pantalla = ventana_crear.winfo_screenwidth()
    alto_pantalla = ventana_crear.winfo_screenheight()
    ancho_ventana = 800
    alto_ventana = 500
    pos_x = round(ancho_pantalla / 2 - ancho_ventana / 2)
    pos_y = round(alto_pantalla / 2 - alto_ventana / 2) - 30
    ventana_crear.geometry(f'{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}')
    ventana_crear.configure(bg='#1e1e1e')

    grupo = tk.Frame(ventana_crear, bg="#313030", bd=5, relief="groove")
    grupo.pack(ipadx='20', ipady='20', pady=(50, 60))

    # Etiquetas
    tk.Label(grupo, text='Bienvenido a Kali York', bg="#1271dd", fg="#ffffff", font=("Arial", 16)).pack(fill='x', pady=10)
    tk.Label(grupo, text='Ingresa tus Datos para Crear tu Usuario:', bg='#3b3b3b', fg='white', font=('Arial', 12)).pack(fill='x', pady=10)

    # Entradas
    tk.Label(grupo, text='Usuario:', bg='#1271dd', fg='white', font=('Arial', 12)).pack()
    entrada_usuario = tk.Entry(grupo, font=('Arial', 12))
    entrada_usuario.pack(pady=5, ipadx=10, ipady=5)

    tk.Label(grupo, text='Contraseña:', bg='#1271dd', fg='white', font=('Arial', 12)).pack()
    entrada_contrasena1 = tk.Entry(grupo, font=('Arial', 12), show='*')
    entrada_contrasena1.pack(pady=5, ipadx=10, ipady=5)

    tk.Label(grupo, text='Confirmar Contraseña:', bg='#1271dd', fg='white', font=('Arial', 12)).pack()
    entrada_contrasena2 = tk.Entry(grupo, font=('Arial', 12), show='*')
    entrada_contrasena2.pack(pady=5, ipadx=10, ipady=5)

    # Función para guardar usuario en `usuarios.txt`
    def registrar_usuario():
        usuario = entrada_usuario.get().strip()
        clave1 = entrada_contrasena1.get().strip()
        clave2 = entrada_contrasena2.get().strip()

        if not usuario or not clave1 or not clave2:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        if clave1 != clave2:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return

        # Verificar si el usuario ya existe
        try:
            with open("usuarios.txt", "r") as file:
                for linea in file:
                    if linea.split(",")[0] == usuario:
                        messagebox.showerror("Error", "El usuario ya existe.")
                        return
        except FileNotFoundError:
            pass  # Si el archivo no existe, no hay problema

        # Guardar nuevo usuario
        try:
            with open("usuarios.txt", "a") as file:
                file.write(f"{usuario},{clave1}\n")
            messagebox.showinfo("Éxito", "Usuario creado correctamente.")
            ventana_crear.destroy()
            cerrarVentana.deiconify()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el usuario: {e}")

    # Botón de creación
    tk.Button(grupo, text="Crear Usuario", bg="#9e2a2a", fg="white", font=("Arial", 12),
              command=registrar_usuario).pack(pady=15)

    # Volver a la ventana principal
    def volver():
        ventana_crear.destroy()
        cerrarVentana.deiconify()

    tk.Button(grupo, text="Volver", command=volver).pack()

    ventana_crear.protocol("WM_DELETE_WINDOW", volver)