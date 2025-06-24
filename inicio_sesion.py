import tkinter as tk
from tkinter import messagebox
from inventario import abrir_inventario

usuarios = {
    "admin": "admin123",
    "supervisor": "supervisor456"
}

def validar_empleado(usuario, contraseña):
    try:
        with open("usuarios.txt", "r") as file:
            for linea in file:
                credenciales = linea.strip().split(",")
                if usuario == credenciales[0] and contraseña == credenciales[1]:
                    return True
    except FileNotFoundError:
        return False
    return False

def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    pos_x = round(pantalla_ancho / 2 - ancho / 2)
    pos_y = round(pantalla_alto / 2 - alto / 2)
    ventana.geometry(f'{ancho}x{alto}+{pos_x}+{pos_y}')

def inicioSesion(ventanaPrincipal):
    ventana_login = tk.Toplevel(ventanaPrincipal)  
    ventana_login.title('Login - Kali York')
    centrar_ventana(ventana_login, 800, 500)
    ventana_login.configure(bg='#1e1e1e')

    grupo = tk.Frame(ventana_login, bg="#313030", bd=5, relief="groove")
    grupo.pack(ipadx='20', ipady='20', pady=(40, 30))

    tk.Label(grupo, text='Bienvenido a Kali York', bg="#1271dd", fg="#ffffff", font=("Arial", 16)).pack(fill='x', pady=10)
    
    tk.Label(grupo, text='Usuario:', bg='#1271dd', fg='white', font=('Arial', 12)).pack()
    entrada_usuario = tk.Entry(grupo, font=('Arial', 12))
    entrada_usuario.pack(pady=5, ipadx=10, ipady=5)

    tk.Label(grupo, text='Contraseña:', bg='#1271dd', fg='white', font=('Arial', 12)).pack()
    entrada_contrasena = tk.Entry(grupo, font=('Arial', 12), show='*')
    entrada_contrasena.pack(pady=5, ipadx=10, ipady=5)

    def login_como_rol():
        usuario = entrada_usuario.get().strip()
        clave = entrada_contrasena.get().strip()

        if not usuario or not clave:
            messagebox.showerror("Error", "Debe ingresar usuario y contraseña.")
            return

        if usuario in usuarios and usuarios[usuario] == clave or validar_empleado(usuario, clave):
            messagebox.showinfo("Acceso concedido", f"Bienvenido {usuario}!")
            ventana_login.destroy()  # Cierra la ventana de login antes de abrir el inventario
            ventanaPrincipal.withdraw()  # Oculta la ventana principal
            abrir_inventario()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    tk.Button(grupo, text="Iniciar Sesión", bg="#9e2a2a", fg="white", font=("Arial", 12), command=login_como_rol).pack(pady=15)