import tkinter as tk
from tkinter import ttk
from inicio_sesion import inicioSesion
from crear_usuario import crearUsuario

ventanaPrincipal = tk.Tk()
ventanaPrincipal.title('Kali York')
anchoPantalla = ventanaPrincipal.winfo_screenwidth()
altoPantalla = ventanaPrincipal.winfo_screenheight()
anchoVentana = 800
altoVentana = 500
posicionx = round(anchoPantalla/2 - anchoVentana/2)
posiciony = round(altoPantalla/2 - altoVentana/2) - 30
ventanaPrincipal.geometry(f'{anchoVentana}x{altoVentana}+{posicionx}+{posiciony}')
ventanaPrincipal.configure(bg="#313131")

grupo = tk.Frame(ventanaPrincipal, bg="#313030", bd=5, relief="groove")
grupo.pack(ipadx='20', ipady='20', pady=(50, 60))

info = tk.Label(grupo, text='¡Bienvenido a Kali York, la mejor marca de ropa del mercado!', bg='#1271dd', fg='#ffffff', font='Arial', relief='groove', bd=5)
info.pack(ipadx='50', ipady='15', pady=(20, 10))

info2 = tk.Label(grupo, text='¿Qué desea realizar a continuación?', bg='#1271dd', font='Arial', fg='#ffffff', relief='groove', bd=5)
info2.pack(ipadx='50', ipady='15')

loginFrame = tk.Frame(grupo, bg="#313030")
loginFrame.pack(side="left", padx=10)

iniciarSesion = tk.Button(grupo, text='Iniciar Sesión', fg="#ffffff", bg='#9e2a2a', font=('Arial', 10, "bold"), relief='ridge',
                          command=lambda: inicioSesion(ventanaPrincipal))
iniciarSesion.pack(side='left', ipadx='50', ipady='15', expand=True)

creaUsuario = tk.Button(grupo, text='Registro', fg="#ffffff", bg='#9e2a2a', font=('Arial', 10, "bold"), relief='ridge',
                        command=lambda: crearUsuario(ventanaPrincipal))
creaUsuario.pack(side='right', ipadx='50', ipady='15', expand=True)

ventanaPrincipal.mainloop()






